"""Small model for reconciling retried order submissions.

A network retry must be correlated with the same client intent; a different
payload sharing an identifier is treated as a conflict.
"""
import unittest
from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Intent:
    client_id: str
    asset: str
    side: str
    size: str
    price: str

    def fingerprint(self) -> str:
        # Length-prefix each field: a "|" join lets a field containing "|" imitate
        # a different split of the same characters.
        fields = (self.client_id, self.asset, self.side, self.size, self.price)
        raw = b"".join(len(f.encode()).to_bytes(8, "big") + f.encode() for f in fields)
        return sha256(raw).hexdigest()

def reconcile(previous: Intent | None, retry: Intent) -> str:
    if previous is None:
        return "submit"
    if previous.fingerprint() == retry.fingerprint():
        return "same-intent: query status"
    if previous.client_id == retry.client_id:
        return "conflict: reject retry"
    return "new-intent: review correlation"

class IdempotencyTests(unittest.TestCase):
    def test_first_submission(self):
        self.assertEqual(reconcile(None, Intent("desk-42", "ETH", "buy", "1", "2000")), "submit")

    def test_identical_retry_queries_status(self):
        order = Intent("desk-42", "ETH", "buy", "1", "2000")
        self.assertEqual(reconcile(order, order), "same-intent: query status")

    def test_same_id_different_payload_is_a_conflict(self):
        first = Intent("desk-42", "ETH", "buy", "1", "2000")
        retry = Intent("desk-42", "ETH", "buy", "2", "2000")
        self.assertEqual(reconcile(first, retry), "conflict: reject retry")

    def test_separator_in_a_field_does_not_imitate_another_intent(self):
        first = Intent("a|b", "c", "buy", "1", "2000")
        other = Intent("a", "b|c", "buy", "1", "2000")
        self.assertNotEqual(first.fingerprint(), other.fingerprint())
        self.assertEqual(reconcile(first, other), "new-intent: review correlation")

if __name__ == "__main__":
    unittest.main()
