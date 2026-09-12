# Références fichier/fonction

## Prototypes locaux

- Base : base_chain_context.py:chain_context, base_deposit_withdrawal.py:transition.
- Hyperliquid : hyperliquid_signed_nonce.py:accept_nonce, hyperliquid_reconciliation.py:reconcile.
- HyperEVM : hyperevm_core_boundary.py:confirm, hyperevm_corewriter.py:valid, hyperevm_dex_transfer.py:net_amount.
- ZK : zk_trace_air.py:air_ok, zk_commitment.py:commit et opens, zk_proof_verifier.py:digest et verify.
- Méthode transversale : research_invariants.py:assess.

## Lecture recommandée

Commencer par docs/ARCHITECTURE.md, poursuivre avec docs/THREAT-MODEL.md, puis comparer chaque fonction aux sources listées dans docs/SOURCES.md. Les noms de fonctions désignent les points d’entrée du prototype ; ils ne prétendent pas reproduire une implémentation de production.
