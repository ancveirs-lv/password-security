from __future__ import annotations
import json, urllib.request, urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'data/sources.json').read_text())['sources']
fail=0
for x in items:
    req=urllib.request.Request(x['url'],headers={'User-Agent':'Mozilla/5.0 password-security-link-check'})
    try:
        with urllib.request.urlopen(req,timeout=20) as r:
            code=getattr(r,'status',200)
            print(f'OK   {code} {x["id"]}')
    except urllib.error.HTTPError as e:
        if e.code in (403,429): print(f'WARN {e.code} {x["id"]}: rate-limited or bot-blocked')
        else: print(f'FAIL {e.code} {x["id"]}'); fail+=1
    except Exception as e:
        print(f'FAIL --- {x["id"]}: {type(e).__name__}: {e}'); fail+=1
raise SystemExit(1 if fail else 0)
