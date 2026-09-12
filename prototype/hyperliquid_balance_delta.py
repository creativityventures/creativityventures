"""Hyperliquid : rapprochement d un delta de solde."""
import unittest
def reconcile(before,after,delta,tolerance=0):return abs((after-before)-delta)<=tolerance
class Tests(unittest.TestCase):
 def test_exact_delta(self):self.assertTrue(reconcile(100,125,25))
 def test_unexplained_delta(self):self.assertFalse(reconcile(100,125,20))
 def test_tolerance(self):self.assertTrue(reconcile(100,125,24,1))
if __name__=='__main__':unittest.main()
