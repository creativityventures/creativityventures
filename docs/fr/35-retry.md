# 35. Retries contrôlés

Ce chapitre situe répéter une écriture sans idempotence peut doubler l’action dans le parcours de recherche de creativityventures. Il part du point d’entrée RESEARCH-METHODOLOGY.md, lu comme source de comportement et non comme preuve de production.

## Question

L’objectif est de décrire quand répéter une lecture ou une écriture. La lecture doit identifier les entrées, la décision produite, les données externes utilisées et l’état qui persiste.

## Lecture du mécanisme

Le fichier cité fournit le contexte concret : noms, types, ordre des contrôles et erreurs observables. Les autres conclusions doivent rester rattachées à une référence précise dans le dépôt.

## Limite

répéter une écriture sans idempotence peut doubler l’action. Ce texte ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./36-timeouts.md)
