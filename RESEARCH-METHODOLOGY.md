# Research methodology

This repository documents verifiable, confidential and scalable onchain systems with a source-first approach. The goal is to make each explanation useful for review, not to imply an audit or production readiness.

## 1. Establish the scope

Name the component, version or commit being studied. State what is covered and what is intentionally outside the review.

## 2. Trace claims to evidence

Prefer upstream source files, specifications and official documentation. Record the relevant path, symbol, invariant or configuration value. Separate directly observed behavior from interpretation and open questions.

## 3. Model trust and threats

Describe who can call the component, which inputs are attacker-controlled, where trust changes, and which assumptions depend on operators, bridges, or external services. For ZK and FHE topics, include the relevant cryptographic parameters and failure boundaries.

## 4. Check invariants

Follow value flow, authorization, state transitions, replay protection, freshness and failure handling. For proving systems, track the relation between trace, constraints, transcript and verification. For agents and RPC systems, track tool permissions, untrusted text, provenance and approval boundaries.

## 5. Report limitations

Mark missing evidence, untested paths, version sensitivity and unresolved questions. Documentation must not claim that tests passed, an audit was completed, or a system is safe unless that result is independently established.

## Review outcome

A useful contribution leaves a reader with a clear source trail, an explicit threat model and a short list of limits that can guide deeper review.
