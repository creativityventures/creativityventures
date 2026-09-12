"""Base : idempotence locale d une intention."""
import unittest
def accept(seen,nonce):
 if nonce in seen:return seen,False
 return seen|{nonce},True
class Tests(unittest.TestCase):
 def test_new_nonce(self):self.assertEqual(accept(set(),3),({3},True))
 def test_replay_rejected(self):self.assertEqual(accept({3},3),({3},False))
if __name__=='__main__':unittest.main()
