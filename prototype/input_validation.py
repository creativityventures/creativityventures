"""Garde-fous reutilisables pour les prototypes documentaires."""
import unittest

def require_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(field + " must be non-empty text")
    return value.strip()

def require_non_negative(value, field):
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(field + " must be a non-negative integer")
    return value

class ValidationTests(unittest.TestCase):
    def test_text_is_normalized(self):
        self.assertEqual(require_text("  Base  ", "network"), "Base")
    def test_empty_text_rejected(self):
        with self.assertRaises(ValueError): require_text(" ", "network")
    def test_boolean_is_not_integer(self):
        with self.assertRaises(ValueError): require_non_negative(True, "nonce")
    def test_negative_value_rejected(self):
        with self.assertRaises(ValueError): require_non_negative(-1, "nonce")

if __name__ == "__main__":
    unittest.main()
