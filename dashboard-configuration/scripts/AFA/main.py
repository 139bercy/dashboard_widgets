# Ce fichier sert de coordinateur : Il choisit les jeu de données à utiliser et les graphiques à générer
import pandas as pd
import utils.fileManager as fm
import caafa2021

def WIP():
    
    # choix du dataset
    page = caafa2021.pagecaafa2021("DJ-2021")

    # obtention de data et conf
    data = page.donut_nbDJParTypeActeurPublic()

    # écriture pour récupération manuelle sur MinIO
    fm.export_ndjson(data[0],"widget-ca-afa-2021.ndjson")
    fm.export_csv(data[1],"conf-ca-afa-2021.csv")

WIP()