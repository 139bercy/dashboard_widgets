# Composant du tableau de bord pour France Relance

Ce projet contient l'ensemble des composants utilisé pour la définition du [tableau de bord France Relance](https://www.economie.gouv.fr/plan-de-relance/tableau-de-bord).

Ces composants ont été développé à l'origine par [Etalab](https://www.etalab.gouv.fr/) pour le [tableau de bord pour le Covid 19](https://github.com/etalab/covid19-dashboard-widgets). Il sont été repris ici et adapté au besoin du Tableau de bord France Relance.

## Développement

### Installation des dépendances
```
npm install
```

### Démarrage d'un serveur de développement
```
npm run serve
```

### Génération d'une version de production
```
npm run build
```

## Intégration d'un nouveau projet

Si vous souhaitez intégrer un nouveau projet, il est nécessaire de mener plusieurs actions :
- Ajout d'un fichier `index-<nom du projet>.html` dans le dossier `public`
- Configuration de la CI en dupliquant les lignes `39` et `84` du fichier `.circleci/config.json` et utilisé le nom du nouveau fichier créé précédemment
- Duplication ou création du fichier de configuration dans `dashboard_configuration`. Ce fichier dépend fortement de ce que vous voulez afficher dans votre dashboard.
- Intégration de ce fichier dans la génération des configurations en duplicant la dernière ligne du fichier `dashboard-configuration/csv_to_json.py` et en y intégrant le nom du fichier créé dans l'étape précédente.
