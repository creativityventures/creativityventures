"""ZK : preuve pedagogique d un claim de plage."""
import unittest
def claim(value,low,high):return low <= value <= high
def verify(value,low,high,proof):return proof==claim(value,low,high)
class Tests(unittest.TestCase):
 def test_in_range(self):self.assertTrue(verify(7,1,10,True))
 def test_out_of_range(self):self.assertFalse(verify(12,1,10,True))
 def test_false_proof_rejected(self):self.assertFalse(verify(7,1,10,False))
if __name__=='__main__':unittest.main()
