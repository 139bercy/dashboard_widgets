# Ce fichier contient toutes les informations pertinentes pour générer un graphique :
# - la méthode d'obtention des données
# - l'emplacement du graphique dans la configuration (volet, panneau, description, etc. -> mix contenant des informations de mise en forme)

import utils.fileManager as fm
import utils.formalismManager as form
import pandas as pd

class pageafa2021:

    def __init__(self,datasetName):
        self.datasetName = datasetName
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

    def analyseTypeFaits_FamilleInfractions(self):
        
        # Data
        dict = {
            "Corruption" : 71,
            "Détournement de fonds publics" : 67,
            "Prise illégale d'intérêts" : 67,
            "Favoritisme" : 64,
            "Trafic d'influence" : 18,
            "Concussion" : 13,
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseTypeFaits_FamilleInfractions"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_PublicPrive(self):
        return

    def analyseSecteursActivite_Public(self):
        return

    def analyseSecteursActivite_Prive(self):
        return

    def repartitionPrevenus_repartition(self):
        return

    def repartitionPrevenus_ageMoyen(self):
        return

    def repartitionPrevenus_nbMoyen(self):
        return

    def NatureSexePrevenus_Nature(self):
        return

    def NatureSexePrevenus_Sexe(self):
        return

    def qualiteCSPPrevenus_qualite(self):
        return

    def qualiteCSPPrevenus_CSP(self):
        return

    def caracsProcedure_origine(self):
        return

    def caracsProcedure_dureeProcedure(self):
        return

    def caracsProcedure_dureePrevention(self):
        return

    def analyseDJ_sens(self):
        return

    def analysePeines_type(self):
        return

    def sanctionPenales_physiquesMoyenneAmende(self):
        return

    def sanctionPenales_physiquesMoyenneEmprisonnement(self):
        return

    def sanctionPenales_moralesMoyenneAmende(self):
        return

    def sanctionPenales_confiscations(self):
        return
        