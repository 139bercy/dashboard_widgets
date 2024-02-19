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
            },
            "box_ageMoyenPrevenus" : {
                "volet" : "Répartition des prévenus",
                "panneau" : "Indicateurs prévenus",
                "no_panneau" : 32,
                "onglet" : "Données 2021",
                "no_onglet" : 1,
                "description" : "Note de lecture 1 : Au sein de l’échantillon de 94 décisions de justice, rendues en 2021 et analysées par l’AFA, l’âge moyen des prévenus au moment du début de la période de prévention des faits qui leur sont reprochés, est de 45 ans. Note de lecture 2 : Au sein de l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, il y a en moyenne 3 prévenus par affaire. Explications : La période de prévention correspond à la durée de temps pendant laquelle les infractions pénales reprochées à un prévenu ont été commises. Elle peut être d’un jour pour les infractions se consommant immédiatement, mais peut également durer plusieurs années. Méthode de comptage : Moyennes réalisées à partir des données concernant les prévenus.",
                "source" : "Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité",
                "titre" : "Age moyen des prévenus",
                "unite" : "ans"
            },
            "box_nbMoyenPrevenusParAffaire" : {
                "volet" : "Répartition des prévenus",
                "panneau" : "Indicateurs prévenus",
                "no_panneau" : 32,
                "onglet" : "Données 2021",
                "no_onglet" : 1,
                "description" : "Note de lecture 1 : Au sein de l’échantillon de 94 décisions de justice, rendues en 2021 et analysées par l’AFA, l’âge moyen des prévenus au moment du début de la période de prévention des faits qui leur sont reprochés, est de 45 ans. Note de lecture 2 : Au sein de l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, il y a en moyenne 3 prévenus par affaire. Explications : La période de prévention correspond à la durée de temps pendant laquelle les infractions pénales reprochées à un prévenu ont été commises. Elle peut être d’un jour pour les infractions se consommant immédiatement, mais peut également durer plusieurs années. Méthode de comptage : Moyennes réalisées à partir des données concernant les prévenus.",
                "source" : "Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité",
                "titre" : "Nombre moyen de prévenus par affaire",
                "unite" : "prévenus"
            }
        }

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
    
        # Formalisation
        orgInfos = self.organisationPage["donut_nbDJParSecteur"]
        result.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, result)
        conf = form.donut_conf(self.datasetName, result, orgInfos)
        
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
    
        # Formalisation
        orgInfos = self.organisationPage["donut_nbDJParTypeActeurPublic"]
        result.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, result)
        conf = form.donut_conf(self.datasetName, result, orgInfos)
        
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
    
        # Formalisation
        orgInfos = self.organisationPage["donut_nbDJParTypeActeurPrive"]
        result.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, result)
        conf = form.donut_conf(self.datasetName, result, orgInfos)
        
        return [data,conf]

    def box_ageMoyenPrevenus(self,normal=False):
        # Création de la série
        moyenneAge = self.data.ageMomentFaits.mean()
        result = pd.Series({"Age moyen des prévenus" : moyenneAge})

        # Formalisation
        orgInfos = self.organisationPage["box_ageMoyenPrevenus"]
        result.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, result)
        conf = form.box_conf(self.datasetName, result, orgInfos)
        return [data,conf]

    def box_nbMoyenPrevenusParAffaire(self,normal=False): # Compte les personnes morales comme des prévenus
        # Création de la série
        gensParFiche = self.data.groupby('fiche')
        moyenneGensParFiche = gensParFiche.personne.count().mean()
        result = pd.Series({"Nombre moyen de prévenus par affaire" : moyenneGensParFiche})
        
        # Formalisation
        orgInfos = self.organisationPage["box_nbMoyenPrevenusParAffaire"]
        result.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, result)
        conf = form.box_conf(self.datasetName, result, orgInfos)
        return [data,conf]