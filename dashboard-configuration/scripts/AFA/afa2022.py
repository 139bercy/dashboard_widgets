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
        dict = {'Corruption': 54, 'Favoritisme': 32, "Trafic d'influence": 30, 'Détournement de fonds publics': 26, "Prise illégale d'intérêts": 22, 'Concussion': 3}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseTypeFaits_FamilleInfractions"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_PublicPrive(self):
        
        # Data
        dict = {'Public': 92, 'Privé': 92}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_PublicPrive"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_Public(self):

        # Data
        dict = {'Collectivités - mairies': 31, 'Etat - administration centrale': 22, 'Non renseigne': 10, 'Etablissement public': 7, 'Collectivités régionales': 7, 'Fonction publique hospitaliere': 6, 'Collectivités départementales': 6, 'Etat - deconcentre': 3}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_Public"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseSecteursActivite_Prive(self):

        # Data
        dict = {'Construction': 19, 'Non renseigne': 9, 'Activités immobilières': 8, 'Activités spécialisées, scientifiques et techniques': 8, 'Hébergement et restauration': 7, 'Activités de services administratifs et de soutien': 6, 'Autres activités de services': 5, 'Arts, spectacles et activités récréatives': 4, "Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné": 3, 'Transports et entreposage': 3, "Commerce ; réparation d'automobiles et de motocycles": 3, "Activités financières et d'assurance": 3, 'Agriculture sylviculture et pêche': 2, 'Santé humaine et action sociale': 1}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseSecteursActivite_Prive"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_repartition(self):

        # Data
        dict = {'Corruption': 54, 'Favoritisme': 32, "Trafic d'influence": 29, 'Détournement de fonds publics': 26, "Prise illégale d'intérêts": 22, 'Concussion': 3}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_repartition"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_ageMoyen(self):
        
        # Data
        dict = {
            "Age moyen des prévenus" : 45.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_ageMoyen"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def repartitionPrevenus_nbMoyen(self):
        
        # Data
        dict = {
            "Nombre moyen de prévenus par affaires" : 2.9
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["repartitionPrevenus_nbMoyen"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def NatureSexePrevenus_Nature(self):
        
        # Data
        dict = {
            "Personne physique" : 167,
            "Personne morale" : 8
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["NatureSexePrevenus_Nature"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def NatureSexePrevenus_Sexe(self):
        
        # Data
        dict = {'Hommes': 133, 'Femmes': 34}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["NatureSexePrevenus_Sexe"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def qualiteCSPPrevenus_qualite(self):
        
        # Data
        dict = {'Agents publics': 66, 'Dirigeants de societe': 46, 'Employes': 19, 'Particuliers': 18, 'Elus': 14, 'Personne morale de droit prive': 5, 'Personne morale de droit public ': 1}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["qualiteCSPPrevenus_qualite"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def qualiteCSPPrevenus_CSP(self):
        
        # Data
        dict = {"Cadres d'entreprise": 44, 'Cadres de la fonction publique, professions intellectuelles et  artistiques': 37, 'Employés de la fonction publique': 31, 'Non renseigne': 20, "Chefs d'entreprise de 10 salariés ou plus": 6, "Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés": 5, 'Employés de commerce': 4, 'Ouvriers qualifiés': 3, 'Inactifs divers (autres que retraités)': 3, 'Techniciens': 2, "Employés administratifs d'entreprise": 2, 'Professions libérales et assimilés': 2, 'Commerçants et assimilés': 1, 'Inactifs divers (y compris retraités)': 1, 'Contremaîtres, agents de maîtrise': 1, 'Anciens cadres et professions intermédiaires': 1, 'Agriculteurs exploitants': 1}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["qualiteCSPPrevenus_CSP"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_origine(self):
        
        # Data
        dict = {'Non renseigne': 26, 'Article 40 al.2': 13, 'Plainte': 11, 'Dossier connexe justice': 3, 'Signalement au procureur par une association  ou un particulier ': 3, 'Citation directe': 3, 'Lettre anonyme ': 1, 'Enquete / audit interne': 1}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_origine"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_dureeProcedure(self):
        
        # Data
        dict = {
            "Durée moyenne de la procédure" : 4.78
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_dureeProcedure"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def caracsProcedure_dureePrevention(self):

        # Data
        dict = {
            "Durée moyenne de la période de prévention" : 1066.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["caracsProcedure_dureePrevention"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analyseDJ_sens(self):
        
        # Data
        dict = {'Déclaration de culpabilité': 255, 'Relaxe ': 98, 'Autre ': 2}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analyseDJ_sens"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def analysePeines_type(self):
        
        # Data
        dict = {'Emprisonnement ': 53, 'Emprisonnement et amende': 52, 'Amende ': 22}
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["analysePeines_type"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.donut_data(self.datasetName, series)
        conf = form.donut_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_physiquesMoyenneAmende(self):
        
        # Data
        dict = {
            "Montant moyen des amendes des prévenus physiques" : 23227.5
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_physiquesMoyenneAmende"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_physiquesMoyenneEmprisonnement(self):
        
        # Data
        dict = {
            "Durée moyenne de l'emprisonnement des prévenus physiques" : 15.2
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_physiquesMoyenneEmprisonnement"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_moralesMoyenneAmende(self):
        
        # Data
        dict = {
            "Montant moyen des amendes des prévenus moraux" : 25000.0
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_moralesMoyenneAmende"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]

    def sanctionPenales_confiscations(self):
        
        # Data
        dict = {
            "Montant moyen des confiscations" : 34672.0
        }
        series = pd.Series(dict)

        # Formalisation
        orgInfos = self.organisationPage["sanctionPenales_confiscations"]
        series.name = orgInfos["titre"] + " | 2022"
        data = form.box_data(self.datasetName, series)
        conf = form.box_conf(self.datasetName, series, orgInfos)
        
        return [data,conf]
        