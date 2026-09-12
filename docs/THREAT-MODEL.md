# Modèle de menaces transversal

Le modèle utilise quatre questions : qui peut agir, quelle donnée peut être hostile, quel invariant limite l’impact, et quelle preuve permet de vérifier le résultat.

| Surface | Menace principale | Invariant à vérifier | Réponse documentaire |
| --- | --- | --- | --- |
| Agent Base | prompt injection ou action non autorisée | l’action exécutable est explicitement approuvée | séparer lecture, préparation et signature |
| RPC HyperEVM | réponse obsolète ou ambiguë | chaîne, bloc et fraîcheur sont cohérents | conserver provenance et borne de fraîcheur |
| Hyperliquid | nonce réutilisé ou état divergent | une intention signée n’est acceptée qu’une fois | comparer journal local et état observé |
| ZK | trace valide mais contrainte incomplète | toutes les transitions sont couvertes par l’AIR | documenter domaine, engagement et vérification |
| FHE | paramètre inadéquat ou fuite par le contexte | calcul dans le budget et niveau de sécurité choisi | rendre paramètres et limites explicites |

Scénario : une entrée hostile traverse une frontière de confiance ; le système vérifie l’invariant, conserve une observation traçable, ou refuse l’action si elle est ambiguë.

Les scénarios sont des hypothèses de revue. Ils ne prétendent pas démontrer l’existence d’une vulnérabilité dans un protocole donné.
