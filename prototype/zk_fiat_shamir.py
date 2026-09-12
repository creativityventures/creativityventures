"""ZK : transformee de Fiat-Shamir deterministe."""
import hashlib
import unittest
def challenge(statement,commitment):return hashlib.sha256((statement+':'+commitment).encode()).hexdigest()
def verify(statement,commitment,response):return response==challenge(statement,commitment)
class Tests(unittest.TestCase):
 def test_valid_response(self):self.assertTrue(verify('claim','commit',challenge('claim','commit')))
 def test_modified_statement_rejected(self):self.assertFalse(verify('other','commit',challenge('claim','commit')))
if __name__=='__main__':unittest.main()
