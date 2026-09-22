import json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.validate import validate
class Tests(unittest.TestCase):
    def test_validation(self): self.assertEqual(validate(),[])
    def test_rule_count_and_parity(self):
        en=json.loads((ROOT/'data/guidance.en.json').read_text())['rules']
        lv=json.loads((ROOT/'data/guidance.lv.json').read_text())['rules']
        self.assertEqual(len(en),10); self.assertEqual([x['id'] for x in en],[x['id'] for x in lv])
    def test_space_rule(self):
        en=json.loads((ROOT/'data/guidance.en.json').read_text())['rules']
        x=next(i for i in en if i['id']=='P05')
        self.assertIn('not magic',x['guidance'].lower())
    def test_service_rules_present(self):
        en=json.loads((ROOT/'data/guidance.en.json').read_text())['rules']
        self.assertTrue(any(x['audience']=='service' for x in en))
if __name__=='__main__': unittest.main()
