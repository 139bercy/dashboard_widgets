# Ce fichier contient toutes les informations pertinentes pour générer un graphique :
# - la méthode d'obtention des données
# - l'emplacement du graphique dans la configuration (volet, panneau, description, etc. -> mix contenant des informations de mise en forme)

import utils.fileManager as fm
import utils.formalismManager as form
import pandas as pd

class pageafa2022:

    def __init__(self,datasetName):
        self.datasetName = datasetName
        self.organisationPage = {
            "analyseTypeFaits_FamilleInfractions" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par type de faits",
                "no_panneau" : 1,
                "onglet" : "Familles d'infractions",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Répartition des infractions par familles"
            },
            "analyseSecteursActivite_PublicPrive" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Répartition par secteurs d'activité",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Répartition entre le public et le privé"
            },
            "analyseSecteursActivite_Public" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur public",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Secteur public"
            },
            "analyseSecteursActivite_Prive" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur privé",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Secteur privé"
            },
            "repartitionPrevenus_repartition" : {
                "volet" : "Données 2022",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Répartition des prévenus",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Répartition des prévenus par familles"
            },
            "repartitionPrevenus_ageMoyen" : {
                "volet" : "Données 2022",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Age moyen des prévenus",
                "unite" : "ans"
            },
            "repartitionPrevenus_nbMoyen" : {
                "volet" : "Données 2022",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Nombre moyen de prévenus par affaire",
                "unite" : "personnes"
            },
            "NatureSexePrevenus_Nature" : {
                "volet" : "Données 2022",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Nature",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Nature des prévenus"
            },
            "NatureSexePrevenus_Sexe" : {
                "volet" : "Données 2022",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Sexe",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Sexe des prévenus physiques"
            },
            "qualiteCSPPrevenus_qualite" : {
                "volet" : "Données 2022",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Qualité",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Qualité des prévenus"
            },
            "qualiteCSPPrevenus_CSP" : {
                "volet" : "Données 2022",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Catégorie socio-professionnelle",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Catégorie socio-professionnelle des prévenus"
            },
            "caracsProcedure_origine" : {
                "volet" : "Données 2022",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Origine de l'affaire",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Origine de l'affaire"
            },
            "caracsProcedure_dureeProcedure" : {
                "volet" : "Données 2022",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Durée de la procédure",
                "unite" : "ans"
            },
            "caracsProcedure_dureePrevention" : {
                "volet" : "Données 2022",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Durée de la période de prévention",
                "unite" : "jours"
            },
            "analyseDJ_sens" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse de la décision judiciaire",
                "no_panneau" : 7,
                "onglet" : "Sens de la décision",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Sens de la décision"
            },
            "analysePeines_type" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse de la peine",
                "no_panneau" : 8,
                "onglet" : "Types de peine",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Types de peine"
            },
            "sanctionPenales_physiquesMoyenneAmende" : {
                "volet" : "Données 2022",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes physiques",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Montant moyen de l'amende pour les personnes physiques",
                "unite" : "€"
            },
            "sanctionPenales_physiquesMoyenneEmprisonnement" : {
                "volet" : "Données 2022",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes physiques",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Durée moyenne de l'emprisonnement pour les personnes physiques",
                "unite" : "mois"
            },
            "sanctionPenales_moralesMoyenneAmende" : {
                "volet" : "Données 2022",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes morales",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Montant moyen de l'amende pour les personnes morales",
                "unite" : "€"
            },
            "sanctionPenales_confiscations" : {
                "volet" : "Données 2022",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Confiscations pénales",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Montant moyen des confiscations",
                "unite" : "€"
            }
        }

    ##############
    # Graphiques #
    ##############

    def analyseTypeFaits_FamilleInfractions(self):
        
        # Data
        dict = {
            "Corruption" : 14,
            "Favoritisme" : 8,
            "Trafic d'influence" : 6,
            "Prise illégale d'intérêts" : 3,
            "Détournement de fonds publics" : 1
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseTypeFaits_FamilleInfractions"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_PublicPrive(self):
        
        # Data
        dict = {
            "Public" : 6,
            "Privé" : 5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_PublicPrive"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_Public(self):

        # Data
        dict = {
            "COLLECTIVITÉS - MAIRIES" : 3,
            "ETABLISSEMENT PUBLIC" : 1,
            "ETAT - ADMINISTRATION CENTRALE" : 1,
            "COLLECTIVITÉS RÉGIONALES" : 1,
            "FONCTION PUBLIQUE HOSPITALIERE" : 1
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_Public"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_Prive(self):

        # Data
        dict = {
            "CONSTRUCTION" : 2,
            "AUTRES ACTIVITÉS DE SERVICES" : 2,
            "PRODUCTION ET DISTRIBUTION D'ÉLECTRICITÉ, DE GAZ, DE VAPEUR ET D'AIR CONDITIONNÉ" : 1,
            "ACTIVITÉS IMMOBILIÈRES" : 1,
            "AGRICULTURE SYLVICULTURE ET PÊCHE" : 1,
            "TRANSPORTS ET ENTREPOSAGE" : 1,
            "HÉBERGEMENT ET RESTAURATION" : 1
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_Prive"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_repartition(self):

        # Data
        dict = {
            "Corruption" : 14,
            "Favoritisme" : 8,
            "Trafic d'influence" : 6,
            "Prise illégale d'intérêts" : 3,
            "Détournement de fonds publics" : 1
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_repartition"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_ageMoyen(self):
        
        # Data
        dict = {
            "Age moyen des prévenus" : 0.0
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_ageMoyen"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_nbMoyen(self):
        
        # Data
        dict = {
            "Nombre moyen de prévenus par affaires" : 3.625
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_nbMoyen"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def NatureSexePrevenus_Nature(self):
        
        # Data
        dict = {
            "Personne physique" : 27,
            "Personne morale" : 2
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["NatureSexePrevenus_Nature"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def NatureSexePrevenus_Sexe(self):
        
        # Data
        dict = {
            "Homme" : 22,
            "Femme" : 5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["NatureSexePrevenus_Sexe"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def qualiteCSPPrevenus_qualite(self):
        
        # Data
        dict = {
            "DIRIGEANTS DE SOCIETE" : 14,
            "AGENTS PUBLICS" : 7,
            "ELUS" : 3,
            "EMPLOYES" : 3,
            "PERSONNE MORALE DE DROIT PRIVE" : 2
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["qualiteCSPPrevenus_qualite"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def qualiteCSPPrevenus_CSP(self):
        
        # Data
        dict = {
            "CADRES D'ENTREPRISE" : 10,
            "CADRES DE LA FONCTION PUBLIQUE, PROFESSIONS INTELLECTUELLES ET  ARTISTIQUES" : 9,
            "CHEFS D'ENTREPRISE DE 10 SALARIÉS OU PLUS" : 4,
            "EMPLOYÉS DE COMMERCE" : 1,
            "OUVRIERS QUALIFIÉS" : 1,
            "EMPLOYÉS DE LA FONCTION PUBLIQUE" : 1,
            "COMMERÇANTS ET ASSIMILÉS" : 1
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["qualiteCSPPrevenus_CSP"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_origine(self):
        
        # Data
        dict = {
            "ARTICLE 40 al.2" : 4,
            "PLAINTE" : 2,
            "NON RENSEIGNE" : 2
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_origine"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_dureeProcedure(self):
        
        # Data
        dict = {
            "Durée moyenne de la procédure" : 5.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_dureeProcedure"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_dureePrevention(self):

        # Data
        dict = {
            "Durée moyenne de la période de prévention" : 1520.7
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_dureePrevention"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseDJ_sens(self):
        
        # Data
        dict = {
            "CONDAMNATION" : 41,
            "RELAXE" : 18
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseDJ_sens"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analysePeines_type(self):
        
        # Data
        dict = {
            "EMPRISONNEMENT ET AMENDE" : 18,
            "EMPRISONNEMENT" : 17,
            "AMENDE" : 6
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analysePeines_type"]
        series.name = orgInfos["titre"]
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_physiquesMoyenneAmende(self):
        
        # Data
        dict = {
            "Montant moyen des amendes des prévenus physiques" : 13954.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_physiquesMoyenneAmende"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_physiquesMoyenneEmprisonnement(self):
        
        # Data
        dict = {
            "Durée moyenne de l'emprisonnement des prévenus physiques" : 14.3
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_physiquesMoyenneEmprisonnement"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_moralesMoyenneAmende(self):
        
        # Data
        dict = {
            "Montant moyen des amendes des prévenus moraux" : 0.0
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_moralesMoyenneAmende"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_confiscations(self):
        
        # Data
        dict = {
            "Montant moyen des confiscations" : 0.0
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_confiscations"]
        series.name = orgInfos["titre"]
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]
        