# 19. Idempotence d’ordre Hyperliquid

Ce chapitre situe l’identifiant client doit survivre aux délais réseau dans le parcours de recherche de creativityventures. Il part du point d’entrée prototype/hyperliquid_order_idempotency.py, lu comme source de comportement et non comme preuve de production.

## Question

L’objectif est de éviter les doubles soumissions lors des retries. La lecture doit identifier les entrées, la décision produite, les données externes utilisées et l’état qui persiste.

## Lecture du mécanisme

Le fichier cité fournit le contexte concret : noms, types, ordre des contrôles et erreurs observables. Les autres conclusions doivent rester rattachées à une référence précise dans le dépôt.

## Limite

l’identifiant client doit survivre aux délais réseau. Ce texte ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./20-hyperliquid-intention.md)
