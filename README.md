# creativity ventures

Researching verifiable, confidential and scalable onchain systems. Focus: STARK, SNARK, FHE, Base AI agents and Hyperliquid / HyperEVM infrastructure.

## Parcours français

Le parcours documentaire français rassemble 73 chapitres source-grounded sur les prototypes de preuve, les invariants et les frontières de confiance. Consulter le [sommaire français](docs/fr/README.md) pour suivre les contributions dans l’ordre.

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

## Navigation technique

- [Architecture de recherche](docs/ARCHITECTURE.md) — couches de preuve, invariants et décision.
- [Modèle de menaces](docs/THREAT-MODEL.md) — surfaces Base, Hyperliquid, HyperEVM, ZK et FHE.
- [Sources officielles](docs/SOURCES.md) — références primaires à consulter.
- [Matrice de couverture](docs/COVERAGE.md) — mécanismes, prototypes, invariants et limites.
- [Références fichier/fonction](docs/REFERENCES.md) — points d’entrée précis dans les prototypes.
- [Prototypes](prototype/) — exemples Python autonomes et documentaires.

Les contrôles automatisés de syntaxe et de structure sont définis dans [.github/workflows/light-checks.yml](.github/workflows/light-checks.yml). Ils ne constituent pas un audit de sécurité.
