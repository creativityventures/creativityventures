# Matrice de couverture

| Domaine | Mécanisme | Prototype ou document | Invariant | Limite |
| --- | --- | --- | --- | --- |
| Base | autorité et contexte de chaîne | prototype/base_chain_context.py | réseau et identifiant cohérents | modèle local simplifié |
| Base | dépôt et retrait | prototype/base_deposit_withdrawal.py | transitions d’état explicites | pas d’appel réseau |
| Hyperliquid | nonce signé | prototype/hyperliquid_signed_nonce.py | intention unique | ne remplace pas la signature réelle |
| Hyperliquid | réconciliation | prototype/hyperliquid_reconciliation.py | état local traçable | données simulées |
| HyperEVM | frontière CoreWriter | prototype/hyperevm_core_boundary.py | action et confirmation séparées | pas de nœud RPC |
| ZK | trace AIR et engagement | prototype/zk_trace_air.py, prototype/zk_commitment.py | transitions et ouverture cohérentes | pas de système de preuve complet |
| FHE | paramètres et limites | docs/THREAT-MODEL.md | confidentialité et coût explicités | aucune opération chiffrée exécutée |

Le tableau mesure la couverture documentaire, pas la sécurité ni la maturité de production.
