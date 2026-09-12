# Architecture de recherche

Ce dépôt organise l’analyse autour de quatre couches :

1. Entrées et preuves : spécifications, code source, paramètres et observations horodatées.
2. Invariants : propriétés qui doivent rester vraies, comme l’autorité du wallet, la fraîcheur d’un état ou la cohérence d’une trace.
3. Frontières de confiance : séparation entre données hostiles, composants vérifiés, opérateur et utilisateur.
4. Décision : résultat documenté, limites connues et conditions qui exigeraient une nouvelle vérification.

Flux : Sources -> éléments de preuve -> invariants -> menaces et frontières -> décision documentée.

## Application aux sujets du profil

- Base : relier actions d’agent, autorité de wallet, politiques de transaction et confirmation L2.
- Hyperliquid / HyperEVM : distinguer état de marché, RPC, CoreWriter et provenance des événements.
- ZK : relier trace, contraintes, engagement, preuve et vérification sans confondre calcul et garantie.
- FHE : distinguer données chiffrées, opérations autorisées, paramètres et coût de déchiffrement.

Cette carte est un cadre d’analyse ; elle ne constitue ni un audit ni une garantie de production. Les conclusions doivent renvoyer au fichier et à la fonction observés.
