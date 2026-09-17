# 38. Sérialisation des messages

Ce chapitre situe un changement de sérialisation peut casser la compatibilité dans le parcours de recherche de creativityventures. Il part du point d’entrée prototype/base_cross_domain_message.py, lu comme source de comportement et non comme preuve de production.

## Question

L’objectif est de documenter les champs qui traversent une frontière. La lecture doit identifier les entrées, la décision produite, les données externes utilisées et l’état qui persiste.

## Lecture du mécanisme

Le fichier cité fournit le contexte concret : noms, types, ordre des contrôles et erreurs observables. Les autres conclusions doivent rester rattachées à une référence précise dans le dépôt.

## Limite

un changement de sérialisation peut casser la compatibilité. Ce texte ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./39-identite.md)
