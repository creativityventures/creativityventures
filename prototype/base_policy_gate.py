"""Base : filtre local avant autorisation d une action."""
import unittest
def allowed(action,limit): return isinstance(action,str) and bool(action.strip()) and isinstance(limit,int) and limit > 0
class PolicyTests(unittest.TestCase):
 def test_valid_action(self): self.assertTrue(allowed('bridge',100))
 def test_empty_action(self): self.assertFalse(allowed(' ',100))
 def test_invalid_limit(self): self.assertFalse(allowed('bridge',0))
if __name__ == '__main__': unittest.main()
