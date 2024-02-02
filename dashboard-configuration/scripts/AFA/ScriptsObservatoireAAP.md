### fileManager.py

Ce fichier permet de gérer les transferts de données entre ici et l'espace MinIO fourni dans le datalab.

-----------------------------------

### Dossiers Panneaux

Chaque dossier correspond à un panneau/tableau/graphique. La modification d'un panneau se déroule en 3 étapes :
1) Ecriture du script de génération de nouveaux .csv (config) et .ndjson (données)
2) Génération du .csv et .ndjson
3) Remplacement

Ils contiennent éventuellement différents scripts selon les modifications voulues :
- Changement des données utilisées
- Modification de la description
- Etc.
