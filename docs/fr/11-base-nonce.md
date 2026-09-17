# 11. Nonce et rejeu sur Base

Ce chapitre situe la portée du nonce doit correspondre au domaine de signature dans le parcours de recherche de creativityventures. Il part du point d’entrée prototype/base_nonce_replay.py, lu comme source de comportement et non comme preuve de production.

## Question

L’objectif est de lier nonce, identité et idempotence d’une action. La lecture doit identifier les entrées, la décision produite, les données externes utilisées et l’état qui persiste.

## Lecture du mécanisme

Le fichier cité fournit le contexte concret : noms, types, ordre des contrôles et erreurs observables. Les autres conclusions doivent rester rattachées à une référence précise dans le dépôt.

## Limite

la portée du nonce doit correspondre au domaine de signature. Ce texte ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./12-base-frais.md)
