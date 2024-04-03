# Ce fichier contient toutes les informations pertinentes pour générer un graphique :
# - la méthode d'obtention des données
# - l'emplacement du graphique dans la configuration (volet, panneau, description, etc. -> mix contenant des informations de mise en forme)

import utils.fileManager as fm
import utils.formalismManager as form
import pandas as pd

class pageafa2021:

    def __init__(self):
        self.organisationPage = {
            "analyseTypeFaits_FamilleInfractions" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par type de faits",
                "no_panneau" : 1,
                "onglet" : "Familles d'infractions",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "analyseSecteursActivite_PublicPrive" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Répartition par secteurs d'activité",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "analyseSecteursActivite_Public" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur public",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "analyseSecteursActivite_Prive" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur privé",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "repartitionPrevenus_repartition" : {
                "volet" : "Données 2021",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Répartition des prévenus",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "repartitionPrevenus_ageMoyen" : {
                "volet" : "Données 2021",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "repartitionPrevenus_nbMoyen" : {
                "volet" : "Données 2021",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Indicateurs",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "NatureSexePrevenus_Nature" : {
                "volet" : "Données 2021",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Nature",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "NatureSexePrevenus_Sexe" : {
                "volet" : "Données 2021",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Sexe",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "qualiteCSPPrevenus_qualite" : {
                "volet" : "Données 2021",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Qualité",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "qualiteCSPPrevenus_CSP" : {
                "volet" : "Données 2021",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Catégorie socio-professionnelle",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "caracsProcedure_origine" : {
                "volet" : "Données 2021",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Origine de l'affaire",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "caracsProcedure_dureeProcedure" : {
                "volet" : "Données 2021",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "caracsProcedure_dureePrevention" : {
                "volet" : "Données 2021",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Indicateurs",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "analyseDJ_sens" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse de la décision judiciaire",
                "no_panneau" : 7,
                "onglet" : "Sens de la décision",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "analysePeines_type" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse de la peine",
                "no_panneau" : 8,
                "onglet" : "Types de peine",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "sanctionPenales_physiquesMoyenneAmende" : {
                "volet" : "Données 2021",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes physiques",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "sanctionPenales_physiquesMoyenneEmprisonnement" : {
                "volet" : "Données 2021",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes physiques",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "sanctionPenales_moralesMoyenneAmende" : {
                "volet" : "Données 2021",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes morales",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            },
            "sanctionPenales_confiscations" : {
                "volet" : "Données 2021",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Confiscations pénales",
                "no_onglet" : 4,
                "description" : "Description ",
                "source" : "source",
                "titre" : "titre"
            }
        }

    ##############
    # Graphiques #
    ##############

    def analyseTypeFaits_FamilleInfractions():

    def analyseSecteursActivite_PublicPrive():

    def analyseSecteursActivite_Public():

    def analyseSecteursActivite_Prive():

    def repartitionPrevenus_repartition():

    def repartitionPrevenus_ageMoyen():

    def repartitionPrevenus_nbMoyen():

    def NatureSexePrevenus_Nature():

    def NatureSexePrevenus_Sexe():

    def qualiteCSPPrevenus_qualite():

    def qualiteCSPPrevenus_CSP():

    def caracsProcedure_origine():

    def caracsProcedure_dureeProcedure():

    def caracsProcedure_dureePrevention():

    def analyseDJ_sens():

    def analysePeines_type():

    def sanctionPenales_physiquesMoyenneAmende():

    def sanctionPenales_physiquesMoyenneEmprisonnement():

    def sanctionPenales_moralesMoyenneAmende():

    def sanctionPenales_confiscations():
        

    