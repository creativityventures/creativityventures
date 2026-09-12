"""Hyperliquid : curseur monotone pour rejouer un flux sans doublon."""
import unittest
def advance(cursor,event):
 if not isinstance(event,int) or event <= cursor: return cursor,False
 return event,True
class CursorTests(unittest.TestCase):
 def test_new_event_advances(self): self.assertEqual(advance(10,11),(11,True))
 def test_duplicate_does_not_advance(self): self.assertEqual(advance(10,10),(10,False))
 def test_old_event_does_not_advance(self): self.assertEqual(advance(10,9),(10,False))
if __name__ == '__main__': unittest.main()
