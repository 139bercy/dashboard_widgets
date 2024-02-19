# Ce fichier sert de coordinateur : Il choisit les jeu de données à utiliser et les graphiques à générer
import pandas as pd
import utils.fileManager as fm
import caafa2021

def page1():
    
    # choix du dataset
    page = caafa2021.pagecaafa2021("DJ-2021")

    # obtention des datas et confs
    data_nbDJParSecteur,conf_nbDJParSecteur = page.donut_nbDJParSecteur()
    data_nbDJParTypeActeurPublic,conf_nbDJParTypeActeurPublic = page.donut_nbDJParTypeActeurPublic()
    data_nbDJParTypeActeurPrive,conf_nbDJParTypeActeurPrive = page.donut_nbDJParTypeActeurPrive()
    data_ageMoyenPrevenus,conf_ageMoyenPrevenus = page.box_ageMoyenPrevenus()
    data_nbMoyenPrevenusParAffaire,conf_nbMoyenPrevenusParAffaire = page.box_nbMoyenPrevenusParAffaire()
    
    finalData = data_nbDJParSecteur + data_nbDJParTypeActeurPublic + data_nbDJParTypeActeurPrive + data_ageMoyenPrevenus + data_nbMoyenPrevenusParAffaire
    finalConf = pd.concat([conf_nbDJParSecteur,conf_nbDJParTypeActeurPublic,conf_nbDJParTypeActeurPrive,conf_ageMoyenPrevenus,conf_nbMoyenPrevenusParAffaire])

    # écriture pour récupération manuelle sur MinIO
    fm.export_ndjson(finalData,"NEW-ca-afa-2021.ndjson")
    fm.export_csv(finalConf,"NEW-ca-afa-2021.csv")

page1()