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
            "donut_nbDJParTypeActeurPublic" : {
                "volet" : "Analyse par secteurs d’activité",
                "panneau" : "Secteur public",
                "no_panneau" : 22,
                "onglet" : "Données 2021",
                "no_onglet" : 1,
                "description" : "Note de lecture : La corruption représente 25,6% des faits d’atteinte à la probité rapportés dans les 94 décisions de justice rendues en 2021 et analysées par l’AFA. Explications : Les infractions d’atteinte à la probité regroupent la corruption, le trafic d’influence, le favoritisme, la prise illégale d’intérêts, le détournement de fonds ou de biens publics et la concussion. Dans l’échantillon, aucun fait de concussion n’a été relevé. Pour une définition et une illustration de chaque infraction, se reporter au Lexique de l'AFA. Méthode de comptage : Calcul de répartition des infractions.",
                "source" : "Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité",
                "titre" : "Repartition des décisions de justice pour chaque type d'acteur public"
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