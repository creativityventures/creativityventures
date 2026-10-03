"""Canonical domain separation for documentary ZK transcripts."""
import unittest
from hashlib import sha256

def encode_parts(parts: list[bytes]) -> bytes:
    """Length-prefix every part so that distinct part lists never share an encoding.

    Joining parts with a separator byte is ambiguous as soon as a part can
    contain that byte, which proof bytes routinely do.
    """
    out = len(parts).to_bytes(8, "big")
    for part in parts:
        out += len(part).to_bytes(8, "big") + part
    return out

def transcript_digest(domain: str, circuit_id: str, public_inputs: list[str], proof: bytes) -> str:
    if not domain or not circuit_id:
        raise ValueError("domain and circuit_id are required")
    parts = [domain.encode(), circuit_id.encode(), *(x.encode() for x in public_inputs), proof]
    return sha256(encode_parts(parts)).hexdigest()

def same_context(left: tuple[str, str], right: tuple[str, str]) -> bool:
    return left == right

class DomainSeparationTests(unittest.TestCase):
    def test_digest_is_deterministic(self):
        self.assertEqual(
            transcript_digest("payments-v1", "circuit-7", ["42"], b"proof"),
            transcript_digest("payments-v1", "circuit-7", ["42"], b"proof"),
        )

    def test_domain_changes_digest(self):
        self.assertNotEqual(
            transcript_digest("payments-v1", "circuit-7", ["42"], b"proof"),
            transcript_digest("payments-v2", "circuit-7", ["42"], b"proof"),
        )

    def test_zero_byte_in_proof_does_not_shift_a_boundary(self):
        self.assertNotEqual(
            transcript_digest("d", "c", ["a"], b"\x00b"),
            transcript_digest("d", "c", ["a", ""], b"b"),
        )

    def test_moving_bytes_between_inputs_changes_digest(self):
        self.assertNotEqual(
            transcript_digest("d", "c", ["ab", "c"], b""),
            transcript_digest("d", "c", ["a", "bc"], b""),
        )

    def test_missing_domain_rejected(self):
        with self.assertRaises(ValueError):
            transcript_digest("", "circuit-7", [], b"proof")

if __name__ == "__main__":
    unittest.main()
