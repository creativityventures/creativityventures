"""ZK : validation d un lot de claims avant aggregation."""
import unittest
def batch_ok(claims,minimum):return bool(claims) and all(isinstance(x,int) and x>=minimum for x in claims)
def aggregate(claims):return sum(claims) if claims else None
class Tests(unittest.TestCase):
 def test_valid_batch(self):self.assertEqual(aggregate([5,7]),12)
 def test_invalid_member_rejected(self):self.assertFalse(batch_ok([5,2],3))
 def test_empty_batch_rejected(self):self.assertIsNone(aggregate([]))
if __name__=='__main__':unittest.main()
