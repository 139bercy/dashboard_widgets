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

## Configuration des tableaux de bord

La configuration de chaque tableau de bord se fait en deux étapes : la configuration des données et la configuration de l'affichage des données.

### La configuration des données

Il est tout d'abord nécessaire de produire un fichier de configuration des données en CSV, à l'image de `france-relance.csv`, placé au sein du dossier `dashboard-configuration`. Ce fichier permet de définir de définir l'ordre d'affichage, les informations essentielles (titre, nom des variables, etc.) et les types de graphiques à insérer au sein de chaque panel. C'est ce fichier qui est transformé en JSON par le script `generate_configurations.py`.

### La configuration de l'affichage des données

La configuration de l'affichage des données s'effectue dans le dossier initulé du nom du projet, par exemple `france-relance`, lui-même placé dans le dossier `public`. Celui-ci se structure typiquement de la manière suivante :


```
├── france-relance
│   ├── Logo-France-Relance.png
│   ├── france-relance.css
│   ├── france-relance.description
│   └── line-chart-configuration.json
```

Les fichiers `Logo-France-Relance.png` et `france-relance.description` permettent respectivement d'afficher le logo du commandiaire sur les graphiques et d'introduire des paragraphes de présentation en introduction au tableau de bord. 

La configuration générale du style du tableau de bord est effectuée dans le fichier `france-relance.css`, tandis que les développements spécifiques à chacun des types de graphiques sont spécificés dans les fichiers de la forme de ce dernier : `line-chart-configuration.json`.


### Création des données (Schéma en cours de création ***todo***)

Voici le workflow général des données.

D'un csv ou d'un excel on en ressort un csv modele.
Ce csv model sera converti en json grâce aux fichier csvtojson.py ( Ce même fichier est paramétrable pour coller à chaque projet)
Ce même fichier json est intégré dans data.economie où chaque donnée aura un nom d'indicateurs unique.
Ainsi chacune des données de data.economie sera réucpérer grâce à ce code, à inscrire dans le ichiers de configuration des données en CSV (> afa.csv etc).