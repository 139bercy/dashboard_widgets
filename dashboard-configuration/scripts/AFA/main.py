# Ce fichier sert de coordinateur : Il choisit les jeu de données à utiliser et les graphiques à générer

from datetime import date
import pandas as pd
import utils.fileManager as fm
import caafa2021
import afa
import afa2021

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

    # Assemblage des datas et confs
    finalData = []
    for data in allDatas:
        finalData = finalData + allDatas[data]
    finalConf = pd.concat(list(allConfs.values()))

    # Ecriture pour récupération sur MinIO
    fm.export_ndjson(finalData,"ca-afa-2021-" + str(date.today()) +".ndjson")
    fm.export_csv(finalConf,"ca-afa-2021-" + str(date.today()) +".csv")
    
page_afa2021()

