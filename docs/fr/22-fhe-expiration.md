# 22. Expiration d’accès FHE

Ce chapitre situe l’expiration applicative ne détruit pas nécessairement les ciphertexts dans le parcours de recherche de creativityventures. Il part du point d’entrée prototype/fhe_access_expiry.py, lu comme source de comportement et non comme preuve de production.

## Question

L’objectif est de gérer durée, horloge et révocation d’un accès chiffré. La lecture doit identifier les entrées, la décision produite, les données externes utilisées et l’état qui persiste.

## Lecture du mécanisme

Le fichier cité fournit le contexte concret : noms, types, ordre des contrôles et erreurs observables. Les autres conclusions doivent rester rattachées à une référence précise dans le dépôt.

## Limite

l’expiration applicative ne détruit pas nécessairement les ciphertexts. Ce texte ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./23-fhe-budget.md)
