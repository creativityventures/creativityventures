"""Deterministic policy model for expiring access to encrypted handles."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Request:
    requester: str
    handle: str
    scope: str
    now: int

@dataclass(frozen=True)
class Grant:
    requester: str
    handle: str
    scope: str
    expires_at: int
    revoked: bool = False

def decide(request: Request, grant: Grant | None) -> str:
    if grant is None:
        return "deny:no-grant"
    if grant.revoked:
        return "deny:revoked"
    if grant.requester != request.requester or grant.handle != request.handle:
        return "deny:principal-or-handle-mismatch"
    if grant.scope != request.scope:
        return "deny:scope-mismatch"
    if request.now >= grant.expires_at:
        return "deny:expired"
    return "allow"

if __name__ == "__main__":
    req = Request("alice", "h-1", "decrypt", 99)
    print(decide(req, Grant("alice", "h-1", "decrypt", 100)))
