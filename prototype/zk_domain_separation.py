"""Canonical domain separation for documentary ZK transcripts."""
from hashlib import sha256

SEPARATOR = b"\x00"

def transcript_digest(domain: str, circuit_id: str, public_inputs: list[str], proof: bytes) -> str:
    if not domain or not circuit_id:
        raise ValueError("domain and circuit_id are required")
    parts = [domain.encode(), circuit_id.encode(), *(x.encode() for x in public_inputs), proof]
    return sha256(SEPARATOR.join(parts)).hexdigest()

def same_context(left: tuple[str, str], right: tuple[str, str]) -> bool:
    return left == right

if __name__ == "__main__":
    print(transcript_digest("payments-v1", "circuit-7", ["42"], b"proof"))
