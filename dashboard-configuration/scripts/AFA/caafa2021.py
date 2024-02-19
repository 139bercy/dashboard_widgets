# Ce fichier contient toutes les informations pertinentes pour générer un graphique :
# - la méthode d'obtention des données
# - l'emplacement du graphique dans la configuration (volet, panneau, description, etc. -> mix contenant des informations de mise en forme)

import utils.fileManager as fm
import utils.formalismManager as form
import pandas as pd

class pagecaafa2021:

    def __init__(self, datasetName):
        self.datasetName = datasetName
        self.data = fm.import_excel(datasetName + ".xlsx",[1])
        form.prepareData(self.data)
        self.organisationPage = {
            "donut_nbDJParSecteur" : {
                "volet" : "Analyse par secteurs d’activité",
                "panneau" : "Répartition par secteurs d'activité",
                "no_panneau" : 21,
                "onglet" : "Données 2021",
                "no_onglet" : 1,
                "description" : "Note de lecture : 47,2% des prévenus concernés par les 94 décisions de justice rendues en 2021 et analysées par l’AFA, appartenaient au secteur public. Explications : Le secteur public comprend autant les agents publics (État, collectivités territoriales, établissements publics etc.) que les élus. Chaque secteur comprend à chaque fois les prévenus tant personnes physiques que personnes morales. Un prévenu est une personne poursuivie pénalement et qui n’a pas encore été jugée ou dont la condamnation n’est pas encore définitive. Méthode de comptage : Calcul de répartition des affaires. Les affaires mettant en cause des personnes tant du secteur privé que du secteur public sont comptabilisées dans les deux catégories.",
                "source" : "Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité",
                "titre" : "Répartition par secteurs d'activité"
            },
            "donut_nbDJParTypeActeurPublic" : {
                "volet" : "Analyse par secteurs d’activité",
                "panneau" : "Secteur public",
                "no_panneau" : 22,
                "onglet" : "Données 2021",
                "no_onglet" : 1,
                "description" : "Note de lecture : 9,3% des prévenus des 94 décisions de justice rendues en 2021 et analysées par l’AFA, étaient fonctionnaires de l’État travaillant au sein de l’administration centrale. Explications : Cette classification a été créée par l’AFA. Méthode de comptage : Calcul de répartition des prévenus appartenant au secteur public.",
                "source" : "Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité",
                "titre" : "Répartition au sein du secteur public"
            },
            "donut_nbDJParTypeActeurPrive" : {
                "volet" : "Analyse par secteurs d’activité",
                "panneau" : "Secteur privé",
                "no_panneau" : 23,
                "onglet" : "Données 2021",
                "no_onglet" : 1,
                "description" : "Note de lecture : 26,7% des prévenus des 94 décisions de justice rendues en 2021 et analysées par l’AFA, travaillaient dans le secteur de la construction. Explications : La classification correspond à la nomenclature d’activités française de l’INSEE (NAF rev.2 - Sections). Méthode de comptage : Calcul de répartition des prévenus appartenant au secteur privé.",
                "source" : "Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité",
                "titre" : "Répartition au sein du secteur privé"
            }
        }

    # utiliser cette fonction pour changer le jeu de données
    #@datasetName.setter
    #def datasetName(self, name):
        #if name not in MinIO:
        #    raise ValueError("Le fichier XXX n'existe pas")
        #self.datasetName = name
        #self.data = fm.import_excel(datasetName + ".xlsx",[1])
        #form.prepareData(self.data)

    # Graphiques
    #------------------------------------------------------------------------------------------------------------------------------------------------------#

    def donut_nbDJParSecteur(self,normal=False):
        # Création de la série
        FichesLieesPublic = self.data.loc[self.data.secteurPublic.notna()].groupby('fiche')
        FichesLieesPrive = self.data.loc[self.data.secteurPrive.notna()].groupby('fiche')
        FichesLieesParticuliers = self.data.loc[self.data.secteurPublic.isna() & self.data.secteurPrive.isna()].groupby('fiche')

        repartition = {
            "Secteur public" : FichesLieesPublic.ngroups,
            "Secteur privé" : FichesLieesPrive.ngroups,
            "Particuliers" : FichesLieesParticuliers.ngroups
        }
        
        result = pd.Series(repartition).sort_values(ascending=False)
    
        # Traduction
        orgInfos = self.organisationPage["donut_nbDJParSecteur"]
        
        # Création des lignes de data ( besoin uniquement du code = "datasetName + graphName + indicateur" et de la valeur )
        result.name = orgInfos["titre"]
        data = form.donut_createListData(self.datasetName, result)
    
        # Création des lignes de conf
        conf = form.donut_createListConf(self.datasetName, result, orgInfos)
        
        return [data,conf]
        
    def donut_nbDJParTypeActeurPublic(self,normal=False):
        # Création de la série
        FichesLieesPublic = self.data.loc[self.data.secteurPublic.notna()].groupby('fiche')
        ActeursParFiche = FichesLieesPublic.secteurPublic.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
        
        values = self.data.secteurPublic.dropna().unique()
        proportion = {key: 0 for key in values}
        for fiche in ActeursParFiche:
            for acteurPublic in fiche:
                proportion[acteurPublic] += 1
    
        result = pd.Series(proportion).sort_values(ascending=False)
    
        # Traduction
        orgInfos = self.organisationPage["donut_nbDJParTypeActeurPublic"]
        
        # Création des lignes de data ( besoin uniquement du code = "datasetName + graphName + indicateur" et de la valeur )
        result.name = orgInfos["titre"]
        data = form.donut_createListData(self.datasetName, result)
    
        # Création des lignes de conf
        conf = form.donut_createListConf(self.datasetName, result, orgInfos)
        
        return [data,conf]

    def donut_nbDJParTypeActeurPrive(self,normal=False):
        # Création de la série
        FichesLieesPrives = self.data.loc[self.data.secteurPrive.notna()].groupby('fiche')
        ActeursParFiche = FichesLieesPrives.secteurPrive.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
        
        values = self.data.secteurPrive.dropna().unique()
        proportion = {key: 0 for key in values}
        for fiche in ActeursParFiche:
            for acteurPrive in fiche:
                proportion[acteurPrive] += 1
    
        result = pd.Series(proportion).sort_values(ascending=False)
    
        # Traduction
        orgInfos = self.organisationPage["donut_nbDJParTypeActeurPrive"]
        
        # Création des lignes de data ( besoin uniquement du code = "datasetName + graphName + indicateur" et de la valeur )
        result.name = orgInfos["titre"]
        data = form.donut_createListData(self.datasetName, result)
    
        # Création des lignes de conf
        conf = form.donut_createListConf(self.datasetName, result, orgInfos)
        
        return [data,conf]