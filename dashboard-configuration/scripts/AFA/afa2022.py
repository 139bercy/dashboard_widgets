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
                "description" : "Note de lecture : La corruption représente 25,6% des faits d’atteinte à la probité rapportés dans les 94 décisions de justice rendues en 2021 et analysées par l’AFA. Explications : Les infractions d’atteinte à la probité regroupent la corruption, le trafic d’influence, le favoritisme, la prise illégale d’intérêts, le détournement de fonds ou de biens publics et la concussion. Dans l’échantillon, aucun fait de concussion n’a été relevé. Pour une définition et une illustration de chaque infraction, se reporter au Lexique de l'AFA. Méthode de comptage : Calcul de répartition des infractions.",
                "source" : "source",
                "titre" : "Répartition des infractions par familles"
            },
            "analyseSecteursActivite_PublicPrive" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Répartition par secteurs d'activité",
                "no_onglet" : 1,
                "description" : "Note de lecture : 47,2% des prévenus concernés par les 94 décisions de justice rendues en 2021 et analysées par l’AFA, appartenaient au secteur public. Explications : Le secteur public comprend autant les agents publics (État, collectivités territoriales, établissements publics etc.) que les élus. Chaque secteur comprend à chaque fois les prévenus tant personnes physiques que personnes morales. Un prévenu est une personne poursuivie pénalement et qui n’a pas encore été jugée ou dont la condamnation n’est pas encore définitive. Méthode de comptage : Calcul de répartition des affaires. Les affaires mettant en cause des personnes tant du secteur privé que du secteur public sont comptabilisées dans les deux catégories.",
                "source" : "source",
                "titre" : "Répartition entre le public et le privé"
            },
            "analyseSecteursActivite_Public" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur public",
                "no_onglet" : 2,
                "description" : "Note de lecture : 9,3% des prévenus des 94 décisions de justice rendues en 2021 et analysées par l’AFA, étaient fonctionnaires de l’État travaillant au sein de l’administration centrale. Explications : Cette classification a été créée par l’AFA. Méthode de comptage : Calcul de répartition des prévenus appartenant au secteur public.",
                "source" : "source",
                "titre" : "Secteur public"
            },
            "analyseSecteursActivite_Prive" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse par secteurs d'activités",
                "no_panneau" : 2,
                "onglet" : "Secteur privé",
                "no_onglet" : 3,
                "description" : "Note de lecture : 26,7% des prévenus des 94 décisions de justice rendues en 2021 et analysées par l’AFA, travaillaient dans le secteur de la construction. Explications : La classification correspond à la nomenclature d’activités française de l’INSEE (NAF rev.2 - Sections). Méthode de comptage : Calcul de répartition des prévenus appartenant au secteur privé.",
                "source" : "source",
                "titre" : "Secteur privé"
            },
            "repartitionPrevenus_repartition" : {
                "volet" : "Données 2022",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Répartition des prévenus",
                "no_onglet" : 1,
                "description" : "Note de lecture : Au sein de l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, 26,6 % des prévenus renvoyés devant les juridictions pénales pour des infractions d’atteinte à la probité, l’ont été pour des faits de corruption. Un prévenu renvoyé devant les juridictions pénales pour des faits de corruption et de favoritisme est compté dans les deux catégories. Méthode de comptage : Calcul de répartition des prévenus.",
                "source" : "source",
                "titre" : "Répartition des prévenus par familles"
            },
            "repartitionPrevenus_ageMoyen" : {
                "volet" : "Données 2022",
                "panneau" : "Répartition des prévenus",
                "no_panneau" : 3,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Note de lecture 1 : Au sein de l’échantillon de 94 décisions de justice, rendues en 2021 et analysées par l’AFA, l’âge moyen des prévenus au moment du début de la période de prévention des faits qui leur sont reprochés, est de 45 ans.  Note de lecture 2 : Au sein de l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, il y a en moyenne 3 prévenus par affaire.  Explications :  La période de prévention correspond à la durée de temps pendant laquelle les infractions pénales reprochées à un prévenu ont été commises. Elle peut être d’un jour pour les infractions se consommant immédiatement, mais peut également durer plusieurs années. Méthode de comptage : Moyennes réalisées à partir des données concernant les prévenus.",
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
                "description" : "Note de lecture 1 : Au sein de l’échantillon de 94 décisions de justice, rendues en 2021 et analysées par l’AFA, l’âge moyen des prévenus au moment du début de la période de prévention des faits qui leur sont reprochés, est de 45 ans.  Note de lecture 2 : Au sein de l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, il y a en moyenne 3 prévenus par affaire.  Explications :  La période de prévention correspond à la durée de temps pendant laquelle les infractions pénales reprochées à un prévenu ont été commises. Elle peut être d’un jour pour les infractions se consommant immédiatement, mais peut également durer plusieurs années. Méthode de comptage : Moyennes réalisées à partir des données concernant les prévenus.",
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
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, 92,0% des prévenus jugés pour des faits d’atteinte à la probité étaient des personnes physiques. Explications : En droit français, une personne morale est un groupement doté de la personnalité juridique. Elle peut être composée d’une ou plusieurs personnes physiques ou morales. La personnalité juridique donne à cette personne morale des droits et des devoirs. Une personne morale peut être droit public (État, collectivités territoriales, établissements publics etc.) ou de droit privé (sociétés privées, associations etc.). Depuis 1994 les personnes morales, à l'exclusion de l'État, sont responsables pénalement des infractions commises, pour leur compte, par leurs organes ou représentants. Les établissements publics, les collectivités territoriales et leurs groupements ne sont responsables que pour les infractions commises dans l'exercice des activités susceptibles de faire l'objet de délégation de service public. Méthode de comptage : Calcul de répartition des prévenus selon leur nature.",
                "source" : "source",
                "titre" : "Nature des prévenus"
            },
            "NatureSexePrevenus_Sexe" : {
                "volet" : "Données 2022",
                "panneau" : "Nature et sexe des prévenus",
                "no_panneau" : 4,
                "onglet" : "Sexe",
                "no_onglet" : 2,
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice, rendues en 2021 et analysées par l’AFA, 78,7% des prévenus jugés pour des faits d’atteinte à la probité étaient des hommes. Méthode de comptage : Calcul de répartition des prévenus personnes physiques selon leur sexe.",
                "source" : "source",
                "titre" : "Sexe des prévenus physiques"
            },
            "qualiteCSPPrevenus_qualite" : {
                "volet" : "Données 2022",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Qualité",
                "no_onglet" : 1,
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, 27,2% des prévenus étaient des agents publics. Explications : Cette classification a été créée par l’AFA. La catégorie « particuliers » regroupe les prévenus auxquels on reproche des faits d’atteinte à la probité commis en dehors de leur activité professionnelle. Dans l’échantillon analysé, aucune personne morale de droit public n’a été renvoyée devant une juridiction pénale. Méthode de comptage : Calcul de répartition des prévenus selon leur qualité. Source : Analyse par l’AFA de 94 décisions de justice rendues en 2021 en matière d’atteintes à la probité.",
                "source" : "source",
                "titre" : "Qualité des prévenus"
            },
            "qualiteCSPPrevenus_CSP" : {
                "volet" : "Données 2022",
                "panneau" : "Qualité et catégorie socio-professionnelle (CSP) des prévenus",
                "no_panneau" : 5,
                "onglet" : "Catégorie socio-professionnelle",
                "no_onglet" : 2,
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice, rendues en 2021 et analysées par l’AFA, 6,5 % étaient des chefs d’entreprises d’au moins 10 salariés.  Explications : Cette classification correspond à la nomenclature PCS 2003 – Niveau 2 de l’INSEE qui comprend 24 postes. Méthode de comptage : Calcul de répartition des prévenus selon leur CSP.",
                "source" : "source",
                "titre" : "Catégorie socio-professionnelle des prévenus"
            },
            "caracsProcedure_origine" : {
                "volet" : "Données 2022",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Origine de l'affaire",
                "no_onglet" : 1,
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA :     •  12,8% des affaires avaient pour origine une plainte ;     • les signalements à l’autorité judiciaire, effectués par les autorités et administrations publiques dans le cadre de l’article 40 alinéa 2 du Code de procédure pénale, sont à l’origine de 25,5 % des procédures. La catégorie « AUTRE » contient essentiellement des signalements au procureur, des enquêtes/audits internes, et des enquêtes d’initiatives. Explications : Une enquête peut être ouverte, sur directive du parquet ou sur initiative des enquêteurs, à la suite de plusieurs faits : plainte, signalement, dénonciation anonyme, etc.  L’article 40 alinéa 2 du Code de procédure pénale dispose que « Toute autorité constituée, tout officier public ou fonctionnaire qui, dans l'exercice de ses fonctions, acquiert la connaissance d'un crime ou d'un délit est tenu d'en donner avis sans délai au procureur de la République et de transmettre à ce magistrat tous les renseignements, procès-verbaux et actes qui y sont relatifs. »  Méthode de comptage : Calcul de répartition des affaires selon leur origine.",
                "source" : "source",
                "titre" : "Origine de l'affaire"
            },
            "caracsProcedure_dureeProcedure" : {
                "volet" : "Données 2022",
                "panneau" : "Caractéristiques de la procédure",
                "no_panneau" : 6,
                "onglet" : "Indicateurs",
                "no_onglet" : 2,
                "description" : "Notes de lecture :  Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA :     • la durée moyenne de la procédure est de 5 ans;     • la durée moyenne de la période de prévention est de 2 ans.  Explications : Dans cette analyse, la durée de procédure s’entend comme la durée qui s’écoule depuis la fin de la période de prévention jusqu’à la date du jugement de première instance.  La période de prévention est la période durant laquelle les infractions pénales reprochées à un prévenu ont été commises. Elle peut être d’un jour pour les infractions se consommant immédiatement, mais peut également durer plusieurs années. Méthode de comptage : Moyennes réalisées à partir des données relevées par l’AFA dans les décisions de justice analysées.",
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
                "description" : "Notes de lecture :  Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA :     • la durée moyenne de la procédure est de 5 ans;     • la durée moyenne de la période de prévention est de 2 ans.  Explications : Dans cette analyse, la durée de procédure s’entend comme la durée qui s’écoule depuis la fin de la période de prévention jusqu’à la date du jugement de première instance.  La période de prévention est la période durant laquelle les infractions pénales reprochées à un prévenu ont été commises. Elle peut être d’un jour pour les infractions se consommant immédiatement, mais peut également durer plusieurs années. Méthode de comptage : Moyennes réalisées à partir des données relevées par l’AFA dans les décisions de justice analysées.",
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
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, 44,5% des personnes ont été condamnées à une peine d’emprisonnement et une peine d’amende. 37,3% des prévenus ont été condamnés uniquement à une peine d’emprisonnement tandis que 15,9% ont été condamnés uniquement  à une peine d’amende. Méthode de comptage : Calcul de répartition par peine prononcée selon le sens de la décision.",
                "source" : "source",
                "titre" : "Sens de la décision"
            },
            "analysePeines_type" : {
                "volet" : "Données 2022",
                "panneau" : "Analyse de la peine",
                "no_panneau" : 8,
                "onglet" : "Types de peine",
                "no_onglet" : 1,
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, 44,5 % des prévenus ont été condamnés à une peine d’emprisonnement et à une amende. Explications : La dispense de peine est une « mesure par laquelle le juge correctionnel ou de police qui a retenu la culpabilité du prévenu décide cependant de ne prononcer aucune sanction contre lui lorsqu’il lui apparaît que son reclassement est acquis, que le dommage est réparé, et que le trouble social occasionné par l’infraction a cessé. » (Lexique Dalloz) Méthode de comptage : Calcul de répartition par infractions selon le type de peines prononcées.",
                "source" : "source",
                "titre" : "Types de peine"
            },
            "sanctionPenales_physiquesMoyenneAmende" : {
                "volet" : "Données 2022",
                "panneau" : "Sanction pénale",
                "no_panneau" : 9,
                "onglet" : "Personnes physiques",
                "no_onglet" : 1,
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, les personnes physiques prévenues ont été condamnés en moyenne à près de 19 mois d’emprisonnement et à une amende de 21 973€. Explications : En droit français, une personne morale est un groupement doté de la personnalité juridique. Elle peut être composée d’une ou plusieurs personnes physiques ou morales. La personnalité juridique donne à cette personne morale des droits et des devoirs. Une personne morale peut être droit public (État, collectivités territoriales, établissements publics etc.) ou de droit privé (sociétés privées, associations etc.).  Depuis 1994 les personnes morales, à l'exclusion de l'État, sont responsables pénalement des infractions commises, pour leur compte, par leurs organes ou représentants. Les établissements publics, les collectivités territoriales et leurs groupements ne sont responsables que pour les infractions commises dans l'exercice des activités susceptibles de faire l'objet de délégation de service public. Méthode de comptage : Moyennes réalisées à partir des données relatives aux « amendes » et « emprisonnement » des prévenus ayant la qualité de personnes physiques.",
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
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, les personnes physiques prévenues ont été condamnés en moyenne à près de 19 mois d’emprisonnement et à une amende de 21 973€. Explications : En droit français, une personne morale est un groupement doté de la personnalité juridique. Elle peut être composée d’une ou plusieurs personnes physiques ou morales. La personnalité juridique donne à cette personne morale des droits et des devoirs. Une personne morale peut être droit public (État, collectivités territoriales, établissements publics etc.) ou de droit privé (sociétés privées, associations etc.).  Depuis 1994 les personnes morales, à l'exclusion de l'État, sont responsables pénalement des infractions commises, pour leur compte, par leurs organes ou représentants. Les établissements publics, les collectivités territoriales et leurs groupements ne sont responsables que pour les infractions commises dans l'exercice des activités susceptibles de faire l'objet de délégation de service public. Méthode de comptage : Moyennes réalisées à partir des données relatives aux « amendes » et « emprisonnement » des prévenus ayant la qualité de personnes physiques.",
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
                "description" : "Note de lecture : Sur l’échantillon de 94 décisions de justice rendues en 2021 et analysées par l’AFA, les personnes morales prévenues ont été condamnés en moyenne à une amende de 93 833€. Explications : Par principe, les personnes morales ne pouvant faire l’objet d’une peine d’emprisonnement, elles encourent le quintuple de l’amende encourue par les personnes physiques. Méthode de comptage : Moyennes réalisées à partir des données relatives aux « amendes » et aux personnes morales prévenues.",
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
                "description" : "Note de lecture : Sur l’échantillon de 111 décisions de justice rendues entre 2014 et 2020 et analysées par l’AFA, le montant moyen des confiscations pénales par affaire est de près de 135 000 €. Explications : En plus de l’amende, le juge peut décider de prononcer, dans certaines conditions expressément définies par la loi (article 131-21 du Code pénal), la confiscation de biens meubles ou immeubles, outils ou produits (direct ou indirect) de l’infraction. Il peut également saisir des sommes ou biens correspondant, en valeur, au profit que l’infraction a permis de réaliser.  La peine de confiscation prive l’auteur de l’infraction de la propriété ou de la disposition d’un bien, pour en transférer la propriété à l’État. Dans le cadre de cette étude, sont également comptabilisées les confiscations de scellés (biens saisis lors d’une procédure judiciaire par les enquêteurs ou le juge d’instruction). Méthode de comptage : Moyennes réalisées à partir des données par affaires, relatives aux « confiscations pénales ».",
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
        dict = {'Construction': 19, 'Non renseigne': 9, 'Autres': 9, 'Activités immobilières': 8, 'Activités spécialisées, scientifiques et techniques': 8, 'Hébergement et restauration': 7, 'Activités de services administratifs et de soutien': 6, 'Autres activités de services': 5, 'Arts, spectacles et activités récréatives': 4, "Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné": 3, 'Transports et entreposage': 3}
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
        dict = {"Cadres d'entreprise": 44, 'Cadres de la fonction publique, professions intellectuelles et  artistiques': 37, 'Employés de la fonction publique': 31, 'Non renseigne': 20, 'Autres': 9, "Chefs d'entreprise de 10 salariés ou plus": 6, "Professions intermédiaires de l'enseignement, de la santé, de la fonction publique et assimilés": 5, 'Employés de commerce': 4, 'Ouvriers qualifiés': 3, 'Inactifs divers (autres que retraités)': 3, 'Techniciens': 2}
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
        