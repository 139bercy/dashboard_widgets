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

    finalData = data_nbDJParSecteur + data_nbDJParTypeActeurPublic + data_nbDJParTypeActeurPrive
    finalConf = pd.concat([conf_nbDJParSecteur,conf_nbDJParTypeActeurPublic,conf_nbDJParTypeActeurPrive])
    
    # écriture pour récupération manuelle sur MinIO
    fm.export_ndjson(finalData,"widget-ca-afa-2021.ndjson")
    fm.export_csv(finalConf,"conf-ca-afa-2021.csv")

page1()