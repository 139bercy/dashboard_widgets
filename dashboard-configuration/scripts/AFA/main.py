# Ce fichier sert de coordinateur : Il choisit les jeu de données à utiliser et les graphiques à générer

from datetime import date
import pandas as pd
import utils.fileManager as fm
import caafa2021
import afa
import afa2021
import afa2022

def page_caafa2021():
    
    # Choix du dataset et de la page
    page = caafa2021.pagecaafa2021("DJ-2021")

    # Choix des graphiques à générer : Génération des datas et confs
    allDatas = {}
    allConfs = {}
    allDatas["nbDJParSecteur"],allConfs["nbDJParSecteur"] = page.donut_nbDJParSecteur()
    allDatas["nbDJParTypeActeurPublic"],allConfs["nbDJParTypeActeurPublic"] = page.donut_nbDJParTypeActeurPublic()
    allDatas["nbDJParTypeActeurPrive"],allConfs["nbDJParTypeActeurPrive"] = page.donut_nbDJParTypeActeurPrive()
    allDatas["ageMoyenPrevenus"],allConfs["ageMoyenPrevenus"] = page.box_ageMoyenPrevenus()
    allDatas["nbMoyenPrevenusParAffaire"],allConfs["nbMoyenPrevenusParAffaire"] = page.box_nbMoyenPrevenusParAffaire()

    # Assemblage des datas et confs
    finalData = []
    for data in allDatas:
        finalData = finalData + allDatas[data]
    finalConf = pd.concat(list(allConfs.values()))

    # Ecriture pour récupération sur MinIO
    fm.export_ndjson(finalData,"ca-afa-2021-" + str(date.today()) +".ndjson")
    fm.export_csv(finalConf,"ca-afa-2021-" + str(date.today()) +".csv")

def page_afa():

    # Choix du dataset et de la page
    page = afa.pageafa("Carto Phase test - 113 DJ - copie")

    # Gen data pour demande Henry
    page.CSP_in_PII()

def page_afa2021():

    # Choix du dataset et de la page
    page = afa2021.pageafa2021("20240321 - Carto TJ - Année 2021")

    # Choix des graphiques à générer : Génération des datas et confs
    allDatas = {}
    allConfs = {}
    allDatas["analyseTypeFaits_FamilleInfractions"],allConfs["analyseTypeFaits_FamilleInfractions"] = page.analyseTypeFaits_FamilleInfractions()
    allDatas["analyseSecteursActivite_PublicPrive"],allConfs["analyseSecteursActivite_PublicPrive"] = page.analyseSecteursActivite_PublicPrive()
    allDatas["analyseSecteursActivite_Public"],allConfs["analyseSecteursActivite_Public"] = page.analyseSecteursActivite_Public()
    allDatas["analyseSecteursActivite_Prive"],allConfs["analyseSecteursActivite_Prive"] = page.analyseSecteursActivite_Prive()
    allDatas["repartitionPrevenus_repartition"],allConfs["repartitionPrevenus_repartition"] = page.repartitionPrevenus_repartition()
    allDatas["repartitionPrevenus_ageMoyen"],allConfs["repartitionPrevenus_ageMoyen"] = page.repartitionPrevenus_ageMoyen()
    allDatas["repartitionPrevenus_nbMoyen"],allConfs["repartitionPrevenus_nbMoyen"] = page.repartitionPrevenus_nbMoyen()
    allDatas["NatureSexePrevenus_Nature"],allConfs["NatureSexePrevenus_Nature"] = page.NatureSexePrevenus_Nature()
    allDatas["NatureSexePrevenus_Sexe"],allConfs["NatureSexePrevenus_Sexe"] = page.NatureSexePrevenus_Sexe()
    allDatas["qualiteCSPPrevenus_qualite"],allConfs["qualiteCSPPrevenus_qualite"] = page.qualiteCSPPrevenus_qualite()
    allDatas["qualiteCSPPrevenus_CSP"],allConfs["qualiteCSPPrevenus_CSP"] = page.qualiteCSPPrevenus_CSP()
    allDatas["caracsProcedure_origine"],allConfs["caracsProcedure_origine"] = page.caracsProcedure_origine()
    allDatas["caracsProcedure_dureeProcedure"],allConfs["caracsProcedure_dureeProcedure"] = page.caracsProcedure_dureeProcedure()
    allDatas["caracsProcedure_dureePrevention"],allConfs["caracsProcedure_dureePrevention"] = page.caracsProcedure_dureePrevention()
    allDatas["analyseDJ_sens"],allConfs["analyseDJ_sens"] = page.analyseDJ_sens()
    allDatas["analysePeines_type"],allConfs["analysePeines_type"] = page.analysePeines_type()
    allDatas["sanctionPenales_physiquesMoyenneAmende"],allConfs["sanctionPenales_physiquesMoyenneAmende"] = page.sanctionPenales_physiquesMoyenneAmende()
    allDatas["sanctionPenales_physiquesMoyenneEmprisonnement"],allConfs["sanctionPenales_physiquesMoyenneEmprisonnement"] = page.sanctionPenales_physiquesMoyenneEmprisonnement()
    allDatas["sanctionPenales_moralesMoyenneAmende"],allConfs["sanctionPenales_moralesMoyenneAmende"] = page.sanctionPenales_moralesMoyenneAmende()
    allDatas["sanctionPenales_confiscations"],allConfs["sanctionPenales_confiscations"] = page.sanctionPenales_confiscations()

    # Assemblage des datas et confs
    finalData = []
    for data in allDatas:
        finalData = finalData + allDatas[data]
    finalConf = pd.concat(list(allConfs.values()))

    # Ecriture pour récupération sur MinIO
    fm.export_ndjson(finalData,"afa-2021-" + str(date.today()) +".ndjson")
    fm.export_csv(finalConf,"afa-2021-" + str(date.today()) +".csv")

def page_afa2022():

    # Choix du dataset et de la page
    page = afa2022.pageafa2022("20240321 - Carto TJ - Année 2021")

    # Choix des graphiques à générer : Génération des datas et confs
    allDatas = {}
    allConfs = {}
    allDatas["analyseTypeFaits_FamilleInfractions"],allConfs["analyseTypeFaits_FamilleInfractions"] = page.analyseTypeFaits_FamilleInfractions()
    allDatas["analyseSecteursActivite_PublicPrive"],allConfs["analyseSecteursActivite_PublicPrive"] = page.analyseSecteursActivite_PublicPrive()
    allDatas["analyseSecteursActivite_Public"],allConfs["analyseSecteursActivite_Public"] = page.analyseSecteursActivite_Public()
    allDatas["analyseSecteursActivite_Prive"],allConfs["analyseSecteursActivite_Prive"] = page.analyseSecteursActivite_Prive()
    allDatas["repartitionPrevenus_repartition"],allConfs["repartitionPrevenus_repartition"] = page.repartitionPrevenus_repartition()
    allDatas["repartitionPrevenus_ageMoyen"],allConfs["repartitionPrevenus_ageMoyen"] = page.repartitionPrevenus_ageMoyen()
    allDatas["repartitionPrevenus_nbMoyen"],allConfs["repartitionPrevenus_nbMoyen"] = page.repartitionPrevenus_nbMoyen()
    allDatas["NatureSexePrevenus_Nature"],allConfs["NatureSexePrevenus_Nature"] = page.NatureSexePrevenus_Nature()
    allDatas["NatureSexePrevenus_Sexe"],allConfs["NatureSexePrevenus_Sexe"] = page.NatureSexePrevenus_Sexe()
    allDatas["qualiteCSPPrevenus_qualite"],allConfs["qualiteCSPPrevenus_qualite"] = page.qualiteCSPPrevenus_qualite()
    allDatas["qualiteCSPPrevenus_CSP"],allConfs["qualiteCSPPrevenus_CSP"] = page.qualiteCSPPrevenus_CSP()
    allDatas["caracsProcedure_origine"],allConfs["caracsProcedure_origine"] = page.caracsProcedure_origine()
    allDatas["caracsProcedure_dureeProcedure"],allConfs["caracsProcedure_dureeProcedure"] = page.caracsProcedure_dureeProcedure()
    allDatas["caracsProcedure_dureePrevention"],allConfs["caracsProcedure_dureePrevention"] = page.caracsProcedure_dureePrevention()
    allDatas["analyseDJ_sens"],allConfs["analyseDJ_sens"] = page.analyseDJ_sens()
    allDatas["analysePeines_type"],allConfs["analysePeines_type"] = page.analysePeines_type()
    allDatas["sanctionPenales_physiquesMoyenneAmende"],allConfs["sanctionPenales_physiquesMoyenneAmende"] = page.sanctionPenales_physiquesMoyenneAmende()
    allDatas["sanctionPenales_physiquesMoyenneEmprisonnement"],allConfs["sanctionPenales_physiquesMoyenneEmprisonnement"] = page.sanctionPenales_physiquesMoyenneEmprisonnement()
    allDatas["sanctionPenales_moralesMoyenneAmende"],allConfs["sanctionPenales_moralesMoyenneAmende"] = page.sanctionPenales_moralesMoyenneAmende()
    allDatas["sanctionPenales_confiscations"],allConfs["sanctionPenales_confiscations"] = page.sanctionPenales_confiscations()

    # Assemblage des datas et confs
    finalData = []
    for data in allDatas:
        finalData = finalData + allDatas[data]
    finalConf = pd.concat(list(allConfs.values()))

    # Ecriture pour récupération sur MinIO
    fm.export_ndjson(finalData,"afa-2022-" + str(date.today()) +".ndjson")
    fm.export_csv(finalConf,"afa-2022-" + str(date.today()) +".csv")
    
page_afa2022()

