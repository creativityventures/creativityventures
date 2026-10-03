"""HyperEVM : liaison minimale entre requete et recu."""
import hashlib
import unittest
def encode(*parts):return b''.join(len(p.encode()).to_bytes(8,'big')+p.encode() for p in parts)
def receipt_id(request_id,status):return hashlib.sha256(encode(str(request_id),status)).hexdigest()
def matches(request_id,status,proof):return proof==receipt_id(request_id,status)
class Tests(unittest.TestCase):
 def test_matching_receipt(self):self.assertTrue(matches(7,'confirmed',receipt_id(7,'confirmed')))
 def test_changed_status_rejected(self):self.assertFalse(matches(7,'failed',receipt_id(7,'confirmed')))
 def test_shifted_boundary_rejected(self):self.assertFalse(matches('7:x','y',receipt_id(7,'x:y')))
if __name__=='__main__':unittest.main()
