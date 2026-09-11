# creativity ventures

Researching verifiable, confidential and scalable onchain systems. Focus: STARK, SNARK, FHE, Base agents and Hyperliquid / HyperEVM infrastructure.

## Research workflow

This profile uses a source-first review method: define scope, trace claims to upstream evidence, model trust and threats, check invariants, and record limitations. See [RESEARCH-METHODOLOGY.md](RESEARCH-METHODOLOGY.md) for the full workflow.

The repository is a research notebook, not an audit report. Explanations distinguish observed implementation details from interpretation, and they do not claim tests, audits or production readiness unless those results are independently established.

## Featured technical work

- [AgentKit on Base](https://github.com/creativityventures/agentkit/tree/main/docs/fr) — wallet authority, typed actions, MCP, prompt injection, transaction policies and human approval.
- [HyperEVM MCP](https://github.com/creativityventures/hyperevm-mcp/tree/main/docs/fr) — read-only capabilities, SSRF resistance, hostile-data handling, freshness and auditable invariants.
- [Hyperliquid Node](https://github.com/creativityventures/node/tree/main/docs/fr) — HyperEVM RPC, local Info, snapshots, event provenance and replay-safe indexing.
- [Lambdaworks ZK](https://github.com/creativityventures/lambdaworks/tree/main/docs/fr) — AIR, FRI, Merkle, STARK and SNARK review map.
- [TFHE-rs](https://github.com/creativityventures/tfhe-rs/tree/main/docs/fr) — programmable bootstrapping, encrypted integers and parameter risk.
- [Base Nitro Validator](https://github.com/creativityventures/nitro-validator/tree/main/docs/fr) — CBOR, certificate chains, P-384, freshness and replay.

## Contribution principles

- Source-grounded explanations and explicit trust boundaries.
- One focused commit per technical chapter.
- Security limits and operational assumptions stated clearly.
- Documentation work does not claim an audit or production readiness.

See [CONTRIBUTING.md](CONTRIBUTING.md) for review expectations and [SECURITY.md](SECURITY.md) for reporting and handling boundaries.

Existing research also covers DeFi protocols, AMMs, lending systems and smart-contract primitives.
