"""ZK : verification pedagogique d un chemin Merkle."""
import hashlib
import unittest
def h(left,right): return hashlib.sha256((left+right).encode()).hexdigest()
def root(leaf,siblings):
 value=leaf
 for sibling in siblings: value=h(value,sibling)
 return value
def verify(leaf,siblings,expected): return root(leaf,siblings)==expected
class MerkleTests(unittest.TestCase):
 def test_valid_path(self):
  path=['b','c']; self.assertTrue(verify('a',path,root('a',path)))
 def test_modified_leaf_rejected(self): self.assertFalse(verify('x',['b','c'],root('a',['b','c'])))
if __name__ == '__main__': unittest.main()
