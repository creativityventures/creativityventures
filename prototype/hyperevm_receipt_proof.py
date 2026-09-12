"""HyperEVM : liaison minimale entre requete et recu."""
import hashlib
import unittest
def receipt_id(request_id,status):return hashlib.sha256((str(request_id)+':'+status).encode()).hexdigest()
def matches(request_id,status,proof):return proof==receipt_id(request_id,status)
class Tests(unittest.TestCase):
 def test_matching_receipt(self):self.assertTrue(matches(7,'confirmed',receipt_id(7,'confirmed')))
 def test_changed_status_rejected(self):self.assertFalse(matches(7,'failed',receipt_id(7,'confirmed')))
if __name__=='__main__':unittest.main()
