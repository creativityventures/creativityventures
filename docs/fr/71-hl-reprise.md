# 71. Reprise d’indexation

Ce chapitre situe un checkpoint trop tôt peut perdre des événements dans le parcours de recherche de creativityventures. Il part du point d’entrée prototype/hyperliquid_event_cursor.py, lu comme source de comportement et non comme preuve de production.

## Question

L’objectif est de définir checkpoint, relecture et détection de trou. La lecture doit identifier les entrées, la décision produite, les données externes utilisées et l’état qui persiste.

## Lecture du mécanisme

Le fichier cité fournit le contexte concret : noms, types, ordre des contrôles et erreurs observables. Les autres conclusions doivent rester rattachées à une référence précise dans le dépôt.

## Limite

un checkpoint trop tôt peut perdre des événements. Ce texte ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./72-limites.md)
