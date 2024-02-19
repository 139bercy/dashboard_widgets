# Ce fichier gère le formalisme attendu par le widget (pour écrire)
# et interprète le formalisme du tableaue excel (pour lire).
# /!\ Ce fichier ne gère pas le format au sens de l'extension de fichier (fileManager le fait).

import pandas as pd
import copy as cp

# Formalisme du tableau excel des data brutes
#--------------------------------------------------------------------------------------------------------------------------------------#

# Ne retourne rien, change les noms de colonnes pou quelque chose de plus informatique-friendly
def prepareData(tableau):
    # dict = { 'old column1 name' : 'new column1 name', 'old column2 name' : 'new column2 name', ... }
    # l'entièreté des colonnes est représenté, même quand il n'y a pas de changement
    customIndex = {
        'Fiche ' : "fiche",
        'Juridiction' : "juridiction",
        'code NATINF des atteintes à la probité' : "codeNATINF",
        ' codes NATINF - infraction connexe d\'atteintes à la probité  ' : "codeNATINFconnexe",
        'infraction' : "infraction",
        'personne physique /personne morale' : "personne",
        'sexe' : "sexe",
        'année de naissance' : "anneeNaissance",
        'âge au moment des faits' : "ageMomentFaits",
        'qualité des prévenus ' : "qualitePrevenus",
        'secteur économique public concerné ' : "secteurPublic",
        'secteur économique privé concerné ' : "secteurPrive",
        'Profession et catégorie socioprofessionnelle' : "ProfessionEtCategorie",
        'mode opératoire I (description littérale)' : "descriptionModeOperatoire",
        'montant des enjeux financiers ' : "montantEnjeux",
        'département du lieu de commission des faits' : "departementCommissionFaits",
        'région du lieu de commissions des faits' : "regionCommissionFaits",
        'début de la période de prévention' : "debutPrevention",
        'Année de début de prévention' : "anneeDebutPrevention",
        'fin de la période de prévention' : "finPrevention",
        'durée de la période de prévention\n(en nbr jours)' : "dureePrevention",
        'origine de l’affaire' : "origineAffaire",
        'service judiciaire saisi' : "serviceJudiciaireSaisi",
        'mode de poursuite retenu ' : "modePoursuiteRetenu",
        'parties civiles -personne physique \nNombre' : "nbrPartiesCivilesPhysiques",
        'parties civiles - personne morale\nNombre' : "nbrPartiesCivilesMorales",
        'parties civiles - personne morale 1' : "PartieCivileMorale1",
        'parties civiles - personne morale 2' : "PartieCivileMorale2",
        'parties civiles - personne morale 3' : "PartieCivileMorale3",
        'Date de l\'audience ' : "dateAudience",
        'Date du jugement ' : "dateJugement",
        'nullité soulevée ' : "nulliteSoulevee",
        'sens de la décision par prevenu ' : "sensDecision",
        'peines par prevenu' : "peines",
        'durée de l\'emprisonnement (mois) ' : "dureeEmprisonnement",
        'Mandat de dépôt' : "mandatDepot",
        'sursis' : "sursis",
        'durée du sursis\n(mois)' : "dureeSursis",
        'montant de l\'amende' : "montantAmende",
        'sursis sur amende' : "sursisAmende",
        'jour amende' : "jourAmende",
        'peines complémentaires  ' : "peinesComplementaires",
        'interdiction d\'exercice de toute fonction ou emploi public' : "interdictionEmploiPublic",
        'durée' : "dureeInterdictionEmploiPublic",
        'execution provisoire' : "executionProvisoire",
        'interdiction d\'exercer l\'activité professionnelle ayant permis la commission de l\'infraction ' : "interdictionProfession",
        'durée.1' : "dureeInterdictionProfession",
        'interdiction d\'exercer une profession commerciale ou industrielle, de diriger, d\'administrer, de gérer, de controler une entreprise, une société' : "interdictionEntreprise",
        'durée.2' : "dureeInterdictionEntreprise",
        'privation des droits civiques, civiles, de famille' : "privationDroitsCiviques",
        'durée.3' : "dureePrivationDroitsCiviques",
        'privation du droit de vote et d\'éligibilité' : "privationDroitVote",
        'durée.4' : "dureePrivationDroitVote",
        'suspension du permis de conduire' : "suspensionPermisConduire",
        'durée.5' : "dureeSuspensionPermisConduire",
        'privation du droit d\'exercer une fonction juridictionnelle, d\'expert, de representation ou d\'assistance en justice' : "privationFonctionJuridique",
        'durée.6' : "dureePrivationFonctionJuridique",
        'confiscation biens meubles ' : "confiscationBiensMeubles",
        'confiscation biens immeubles ' : "confiscationBiensImmeubles",
        'montant de la confiscation ' : "montantConfiscation",
        'Indemnisation des parties civiles ' : "indemnisationPartiesCiviles",
        'Appel de la décision ' : "appelDecision",
        'durée de la procédure (entre la fin de la durée de prévention et jusqu\'à la décision de première instance)' : "dureeProcedure"
    }

    tableau.rename(columns=customIndex, inplace=True) # inplace permet de ne rien retourner et de modifier
    
# Formalisme du fichier .ndjson des data formattées pour être utilisé par le widget
#--------------------------------------------------------------------------------------------------------------------------------------#

# renvoie un dictionnaire dans le format attendu pour une ligne du fichier data.ndjson (voir le schéma du format)
# fonctionne pour les graphiques en donut (et non pie comme on pourrait le croire)
def donut_createLineData(code,value):

    date = "2021-01-01"
    
    values = {}
    values["date"] = date
    values["value"] = value

    france = {}
    france["level"] = "nat"
    france["code_level"] = "fra"
    france["last_value"] = float(value)
    france["last_date"] = date
    france["evol"] = 0
    france["evol_percentage"] = 0
    france["evol_color"] = "red"
    france["values"] = [values]

    regions = cp.deepcopy(france)
    regions["level"] = "reg"
    regions["code_level"] = 0

    departements = cp.deepcopy(regions)
    
    line = {}
    line["code"] = code
    line["nom"] = "."
    line["unite"] = "."
    line["france"] = [france]
    line["regions"] = [regions]
    line["departements"] = [departements]

    return line

# assemble les lignes de ndjson en une liste avec les bonnes infos à chaque ligne
# donutData est une pandas.Series où les index sont les titres, les valeurs leur valeur, le nom de la série est le nom du donut
def donut_createListData(datasetName, donutData):
    list = []
    names = donutData.index.to_list()
    for i in range(donutData.size):
        code = datasetName + " | " + donutData.name + " | " + names[i]
        line = donut_createLineData(code, int(donutData.iloc[i]))
        list.append(line)
    return list

# Formalisme du fichier .csv de la configuration pour être utilisé par le widget
#--------------------------------------------------------------------------------------------------------------------------------------#

# renvoie un dictionnaire dans le format d'une ligne du fichier [page].csv (configuration widget)
# toujours pour un graphique en donut
def donut_createLineConf(orgInfos,code,name):
    
    dict = {
        "Volet" : orgInfos["volet"],
        "No_Panneau" : orgInfos["no_panneau"],
        "Titre_panneau" : orgInfos["panneau"],
        "No_Onglet" : orgInfos["no_onglet"],
        "Titre_onglet" : orgInfos["onglet"],
        "Indicateur_principal" : 1,
        "Code_indicateur" : code,
        "Carte" : 0,
        "Carte_titre" : "",
        "Graph" : 0,
        "Graph_titre" : "",
        "Graph_avec_valeurs" : 0,
        "Bar" : 0,
        "Bar_titre" : "",
        "Box" : 0,
        "Box_titre" : "",
        "Points" : 0,
        "Pie" : 1,
        "Pie_titre" : orgInfos["titre"],
        "Pie_legende" : 1,
        "Table" : 0,
        "Table_titre" : "",
        "Info" : 0,
        "Info_titre" : "c",
        "Info_contenu" : "c",
        "Avec_nom_indicateur" : "",
        "Avec_moyenne" : 0,
        "MinGeoLevel" : "departements",
        "Titre_indicateur" : name,
        "Nom_indicateur" : name,
        "Lien_page_mesure" : "https://www.agence-francaise-anticorruption.gouv.fr/fr",
        "Description_mesure" : orgInfos["description"],
        "Unité_GP" : "Infractions en 2020",
        "Unité_Evol" : "%",
        "source" : orgInfos["source"],
        "accordéon" : "En savoir plus sur la donnée",
        "titre_page_mesure" : ""
    }
    
    return pd.Series(dict)

# assemble les lignes de conf en une liste avec les bonnes infos
# pageInfos est un dictionnaie contenant les infos de la page pour un graphique
def donut_createListConf(datasetName, data, orgInfos):
    lines = []
    names = data.index.to_list()
    for i in range(data.size):
        code = datasetName + " | " + data.name + " | " + names[i]
        line = donut_createLineConf(orgInfos,code,names[i]).T
        lines.append(line)
    return pd.concat(lines,axis=1).T

