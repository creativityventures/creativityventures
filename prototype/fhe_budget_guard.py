"""FHE : garde-fou de budget avant une operation homomorphe."""
import unittest
def can_compute(noise,capacity,cost): return all(isinstance(x,int) and x >= 0 for x in (noise,capacity,cost)) and noise + cost <= capacity
class BudgetTests(unittest.TestCase):
 def test_operation_within_budget(self): self.assertTrue(can_compute(2,10,3))
 def test_operation_over_budget(self): self.assertFalse(can_compute(8,10,3))
 def test_negative_values_rejected(self): self.assertFalse(can_compute(-1,10,1))
if __name__ == '__main__': unittest.main()
