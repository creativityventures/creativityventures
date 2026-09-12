"""Hyperliquid : normalisation d une intention d ordre."""
import unittest
def intent(symbol,side,size):
 if not isinstance(symbol,str) or not symbol.strip() or side not in ('buy','sell') or size<=0:return None
 return (symbol.strip().upper(),side,size)
class Tests(unittest.TestCase):
 def test_valid_intent(self):self.assertEqual(intent(' eth ','buy',2),('ETH','buy',2))
 def test_invalid_side(self):self.assertIsNone(intent('ETH','hold',2))
if __name__=='__main__':unittest.main()
