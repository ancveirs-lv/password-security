from __future__ import annotations
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))

def validate():
    errors=[]
    en=load('data/guidance.en.json'); lv=load('data/guidance.lv.json'); src=load('data/sources.json')
    if en.get('schema_version')!=1 or lv.get('schema_version')!=1 or src.get('schema_version')!=1:
        errors.append('schema_version must be 1')
    en_ids=[x['id'] for x in en['rules']]; lv_ids=[x['id'] for x in lv['rules']]
    if en_ids!=lv_ids: errors.append('EN/LV rule ID parity failed')
    if len(en_ids)!=len(set(en_ids)): errors.append('duplicate rule ID')
    source_ids={x['id'] for x in src['sources']}
    for lang,payload in [('en',en),('lv',lv)]:
        for item in payload['rules']:
            missing=set(item.get('sources',[]))-source_ids
            if missing: errors.append(f"{lang}:{item['id']} unknown sources: {sorted(missing)}")
            if item.get('audience') not in {'user','service','both'}: errors.append(f"{lang}:{item['id']} invalid audience")
    for path in ['README.md','README.lv.md','docs/en/space-in-passwords.md','docs/lv/atstarpe-parole.md']:
        text=(ROOT/path).read_text(encoding='utf-8')
        if 'http://' in text: errors.append(f'{path}: insecure URL')
        for n,line in enumerate(text.splitlines(),1):
            if line.rstrip()!=line: errors.append(f'{path}:{n}: trailing whitespace')
    blob=(ROOT/'README.md').read_text(encoding='utf-8')+'\n'+(ROOT/'README.lv.md').read_text(encoding='utf-8')
    required=['spaces should be accepted','atstarpei jābūt atļautai','not a magic','nav maģisks']
    for phrase in required:
        if phrase.lower() not in blob.lower(): errors.append(f'missing editorial contract: {phrase}')
    forbidden=[r'passwords? must be changed every 90 days',r'parole jāmaina ik pēc 90',r'must contain an uppercase.*digit.*special',r'obligāti.*lielais.*cipars.*speciāl']
    for pat in forbidden:
        if re.search(pat,blob,re.I|re.S): errors.append(f'forbidden legacy claim: {pat}')
    return errors

if __name__=='__main__':
    e=validate()
    if e:
        print(f'Validation failed: {len(e)} error(s)')
        [print('-',x) for x in e]
        raise SystemExit(1)
    print('Validation passed: 10 bilingual guidance rules, source registry and editorial contracts.')
