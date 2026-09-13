"""Educational model of a Base L1 -> L2 message lifecycle.

This is a deterministic state machine, not a bridge client or security audit.
"""
from enum import Enum

class State(str, Enum):
    EMITTED = "emitted"
    INCLUDED = "included"
    RELAYED = "relayed"
    FINALIZED = "finalized"
    FAILED = "failed"

ALLOWED = {
    State.EMITTED: {State.INCLUDED, State.FAILED},
    State.INCLUDED: {State.RELAYED, State.FAILED},
    State.RELAYED: {State.FINALIZED, State.FAILED},
    State.FINALIZED: set(),
    State.FAILED: set(),
}

def transition(current: State, target: State) -> State:
    if target not in ALLOWED[current]:
        raise ValueError(f"invalid transition: {current.value} -> {target.value}")
    return target

if __name__ == "__main__":
    state = State.EMITTED
    for target in (State.INCLUDED, State.RELAYED, State.FINALIZED):
        state = transition(state, target)
    print(state.value)
