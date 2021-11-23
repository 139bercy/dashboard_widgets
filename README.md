# Composant du tableau de bord pour France Relance

Ce projet contient l'ensemble des composants utilisé pour la définition du [tableau de bord France Relance](https://www.economie.gouv.fr/plan-de-relance/tableau-de-bord).

Ces composants ont été développé à l'origine par [Etalab](https://www.etalab.gouv.fr/) pour le [tableau de bord pour le Covid 19](https://github.com/etalab/covid19-dashboard-widgets). Il sont été repris ici et adapté au besoin du Tableau de bord France Relance.

## Développement

### installation des requirements python
```
python3 -m venv venv
. venv/bin/activate
pip3 install -r dashboard-configuration/requirements.txt
```

### Génération du Json de configuration
#### A faire à chaque changement du CSV de configuration
```
python dashboard-configuration/generate_configurations.py
```

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
