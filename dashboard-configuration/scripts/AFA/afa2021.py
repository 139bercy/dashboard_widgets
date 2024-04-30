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
                "titre" : "Répartition des infractions par familles"
            },
            "analyseSecteursActivite_PublicPrive" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Répartition par secteurs d'activité",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Répartition entre le public et le privé"
            },
            "analyseSecteursActivite_Public" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur public",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Secteur public"
            },
            "analyseSecteursActivite_Prive" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur privé",
                "no_onglet" : 3,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Secteur privé"
            },
            "repartitionPrevenus_repartition" : {
                "volet" : "Données 2021",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Répartition des prévenus",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Répartition des prévenus par familles"
            },
            "repartitionPrevenus_ageMoyen" : {
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Nature",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Nature des prévenus"
            },
            "NatureSexePrevenus_Sexe" : {
                "volet" : "Données 2021",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Sexe",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Sexe des prévenus physiques"
            },
            "qualiteCSPPrevenus_qualite" : {
                "volet" : "Données 2021",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Qualité",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Qualité des prévenus"
            },
            "qualiteCSPPrevenus_CSP" : {
                "volet" : "Données 2021",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Catégorie socio-professionnelle",
                "no_onglet" : 2,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Catégorie socio-professionnelle des prévenus"
            },
            "caracsProcedure_origine" : {
                "volet" : "Données 2021",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Origine de l'affaire",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Origine de l'affaire"
            },
            "caracsProcedure_dureeProcedure" : {
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
                "panneau" : "Analyse de la décision judiciaire",
                "no_panneau" : 7,
                "onglet" : "Sens de la décision",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Sens de la décision"
            },
            "analysePeines_type" : {
                "volet" : "Données 2021",
                "panneau" : "Analyse de la peine",
                "no_panneau" : 8,
                "onglet" : "Types de peine",
                "no_onglet" : 1,
                "description" : "Description ",
                "source" : "source",
                "titre" : "Types de peine"
            },
            "sanctionPenales_physiquesMoyenneAmende" : {
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
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
                "volet" : "Données 2021",
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
        dict = {'Corruption': 78, 'Favoritisme': 71, 'Détournement de fonds publics': 69, "Prise illégale d'intérêts": 69, "Trafic d'influence": 18, 'Concussion': 13}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseTypeFaits_FamilleInfractions"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_PublicPrive(self):
        
        # Data
        dict = {'Privé': 175, 'Public': 166}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_PublicPrive"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_Public(self):

        # Data
        dict = {'Collectivités - mairies': 67, 'Etablissement public': 37, 'Etat - administration centrale': 19, 'Non renseigne': 12, 'Collectivités régionales': 10, 'Etat - deconcentre': 10, 'Collectivités départementales': 9, 'Fonction publique hospitaliere': 2}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_Public"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_Prive(self):

        # Data
        dict = {'Construction': 30, 'Activités spécialisées, scientifiques et techniques': 19, 'Transports et entreposage': 12, 'Non renseigne': 10, 'Activités immobilières': 9, "Commerce ; réparation d'automobiles et de motocycles": 7, 'Hébergement et restauration': 7, 'Autres activités de services': 6, "Production et distribution d'eau ; assainissement, gestion des déchets et dépollution": 5, 'Activités de services administratifs et de soutien': 4, 'Information et communication': 3, 'Arts, spectacles et activités récréatives': 3, 'Santé humaine et action sociale': 3, 'Enseignement': 2, "Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné": 2, 'Industrie manufacturière': 2}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_Prive"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_repartition(self):

        # Data
        dict = {'Corruption': 71, 'Favoritisme': 68, 'Détournement de fonds publics': 58, "Prise illégale d'intérêts": 53, "Trafic d'influence": 18, 'Concussion': 13}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_repartition"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_ageMoyen(self):
        
        # Data
        dict = {
            "Age moyen des prévenus" : 45.1
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_ageMoyen"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_nbMoyen(self):
        
        # Data
        dict = {
            "Nombre moyen de prévenus par affaires" : 2.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_nbMoyen"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def NatureSexePrevenus_Nature(self):
        
        # Data
        dict = {'Personnes physiques': 307, 'Personnes morales': 26}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["NatureSexePrevenus_Nature"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def NatureSexePrevenus_Sexe(self):
        
        # Data
        dict = {'Hommes': 249, 'Femmes': 58}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["NatureSexePrevenus_Sexe"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def qualiteCSPPrevenus_qualite(self):
        
        # Data
        dict = {'Agents publics': 100, 'Dirigeants de societe': 81, 'Particuliers': 52, 'Elus': 44, 'Employes': 24, 'Personne morale de droit prive': 14, 'Personne morale de droit public ': 11}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["qualiteCSPPrevenus_qualite"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def qualiteCSPPrevenus_CSP(self):
        
        # Data
        dict = {'Cadres de la fonction publique, professions intellectuelles et  artistiques': 87, 'Employés de la fonction publique': 52, "Cadres d'entreprise": 50, 'Non renseigne': 32, "Chefs d'entreprise de 10 salariés ou plus": 17, "Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés": 15, 'Professions libérales et assimilés': 14, 'Inactifs divers (autres que retraités)': 14, 'Employés de commerce': 9, 'Commerçants et assimilés': 6, "Employés administratifs d'entreprise": 3, 'Ouvriers non qualifiés': 3, 'Personnels des services directs aux particuliers': 2, 'Contremaîtres, agents de maîtrise': 1, 'Ouvriers qualifiés': 1, 'Techniciens': 1}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["qualiteCSPPrevenus_CSP"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_origine(self):
        
        # Data
        dict = {'Non renseigne': 54, 'Article 40 al.2': 26, 'Plainte': 21, 'Lettre anonyme ': 14, 'Citation directe': 8, "Enquete d'initiative ": 4, 'Dossier connexe justice': 3, 'Signalement au procureur par une association  ou un particulier ': 2, 'Notification tracfin': 1, 'Enquete / audit interne': 1, 'Signalement hatvp': 1}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_origine"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_dureeProcedure(self):
        
        # Data
        dict = {
            "Durée moyenne de la procédure" : 4.2
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_dureeProcedure"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_dureePrevention(self):

        # Data
        dict = {
            "Durée moyenne de la période de prévention" : 953.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_dureePrevention"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseDJ_sens(self):
        
        # Data
        dict = {'Déclaration de culpabilité': 447, 'Relaxe ': 189, 'Autre ': 15, 'Extinction action publique': 7}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseDJ_sens"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analysePeines_type(self):
        
        # Data
        dict = {'Emprisonnement et amende': 90, 'Emprisonnement ': 79, 'Amende ': 58, 'Dispense de peine': 11, 'Autre': 2}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analysePeines_type"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_physiquesMoyenneAmende(self):
        
        # Data
        dict = {
            "Montant moyen des amendes des prévenus physiques" : 21607.3
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_physiquesMoyenneAmende"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_physiquesMoyenneEmprisonnement(self):
        
        # Data
        dict = {
            "Durée moyenne de l'emprisonnement des prévenus physiques" : 16.3
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_physiquesMoyenneEmprisonnement"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_moralesMoyenneAmende(self):
        
        # Data
        dict = {
            "Montant moyen des amendes des prévenus moraux" : 71125.0
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_moralesMoyenneAmende"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_confiscations(self):
        
        # Data
        dict = {
            "Montant moyen des confiscations" : 241255.2
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_confiscations"]
        series.name = orgInfos["titre"] + " | 2021"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]
        