# Tableaux de bord publics

Ce projet contient l'ensemble des éléments nécessaires à la réalisation de tableaux de bord publics. 

Ces composants ont été développé à l'origine par [Etalab](https://www.etalab.gouv.fr/) pour le [tableau de bord pour le Covid 19](https://github.com/etalab/covid19-dashboard-widgets). Ils ont initialement été repris ici, et adaptés pour l'élaboration du [tableau de bord France Relance](https://www.economie.gouv.fr/plan-de-relance/tableau-de-bord). Le travail en cours consiste à rendre modulaire ce projet, afin de permettre la production de tableaux de bord publics adaptés aux besoins de la commande.

## Installation et mise en production

Après avoir cloné ce projet, la première étape de l'installation consiste à installer les bibliothèques Python requises dans un nouvel environnement virtuel.

```
python3 -m venv venv
. venv/bin/activate
pip3 install -r dashboard-configuration/requirements.txt
```

Une fois l'installation des dépendances effectuée, il convient de relancer la génération du fichier JSON de configuration du tableau de bord. Cette étape est à répéter à chaque changement du fichier CSV de configuration.

```
python3 dashboard-configuration/generate_configurations.py
```

Enfin, après avoir lancé l'installation du projet avec la commande `npm install`, il est possible de :

1. Démarrer un serveur de développement, à l'aide de la commande : `npm run serve`
2. Générer la version de production dans le dossier `dist` à la racine du projet, par la commande : `npm run build`
