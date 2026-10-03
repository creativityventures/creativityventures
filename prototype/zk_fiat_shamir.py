"""ZK : transformee de Fiat-Shamir deterministe."""
import hashlib
import unittest
def encode(*parts):return b''.join(len(p.encode()).to_bytes(8,'big')+p.encode() for p in parts)
def challenge(statement,commitment):return hashlib.sha256(encode(statement,commitment)).hexdigest()
def verify(statement,commitment,response):return response==challenge(statement,commitment)
class Tests(unittest.TestCase):
 def test_valid_response(self):self.assertTrue(verify('claim','commit',challenge('claim','commit')))
 def test_modified_statement_rejected(self):self.assertFalse(verify('other','commit',challenge('claim','commit')))
 def test_shifted_boundary_rejected(self):self.assertNotEqual(challenge('a:b','c'),challenge('a','b:c'))
if __name__=='__main__':unittest.main()
