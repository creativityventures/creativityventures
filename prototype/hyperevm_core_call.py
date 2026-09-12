"""HyperEVM : validation d un appel CoreWriter borne."""
import unittest
def core_call(action,chain_id):
 if not isinstance(action,str) or not action.strip():return None
 if chain_id != 999:return None
 return {'action':action.strip(),'chain_id':chain_id}
class Tests(unittest.TestCase):
 def test_valid_call(self):self.assertEqual(core_call('transfer',999)['chain_id'],999)
 def test_wrong_chain_rejected(self):self.assertIsNone(core_call('transfer',1))
 def test_empty_action_rejected(self):self.assertIsNone(core_call(' ',999))
if __name__=='__main__':unittest.main()
