"""Small model for reconciling retried order submissions.

A network retry must be correlated with the same client intent; a different
payload sharing an identifier is treated as a conflict.
"""
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
        raw = "|".join((self.client_id, self.asset, self.side, self.size, self.price))
        return sha256(raw.encode()).hexdigest()

def reconcile(previous: Intent | None, retry: Intent) -> str:
    if previous is None:
        return "submit"
    if previous.fingerprint() == retry.fingerprint():
        return "same-intent: query status"
    if previous.client_id == retry.client_id:
        return "conflict: reject retry"
    return "new-intent: review correlation"

if __name__ == "__main__":
    order = Intent("desk-42", "ETH", "buy", "1", "2000")
    print(reconcile(order, order))
