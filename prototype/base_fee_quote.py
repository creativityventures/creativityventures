"""Base : calcul transparent d un budget de frais."""
import unittest
def budget(value,gas,price):
 if min(value,gas,price)<0:return None
 fee=gas*price
 return value-fee if value>=fee else None
class Tests(unittest.TestCase):
 def test_budget(self):self.assertEqual(budget(100,2,3),94)
 def test_insufficient_value(self):self.assertIsNone(budget(1,2,3))
if __name__=='__main__':unittest.main()
