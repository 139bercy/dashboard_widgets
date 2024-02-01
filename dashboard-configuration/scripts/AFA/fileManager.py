# Fichier définissant des méthodes pour read/write des données stockées sur mon espace MinIO ("Mes fichiers") du datalab
# Les fichiers sont immédiatement traduits en DataFrame
# Pour ouvrir les vieux excels de l'AFA, il faut installer la dépendance openpyxl : "pip install openpyxl"
# Issue de la doc du SSPCloud : https://docs.sspcloud.fr/onyxia-guide/stockage-de-donnees

import os
import s3fs
import pandas as pd

# Create filesystem object ?????? je ne comprend pas mais ça marche
S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})

BUCKET = "esimon" # = racine

# file_path = string
def import_excel(file_path):
    PATH = BUCKET + "/" + file_path
    with fs.open(PATH,mode="rb") as file: # https://www.geeksforgeeks.org/with-statement-in-python/
        df = pd.read_excel(file)
    return df

def export_csv(df,file_path):
    PATH = BUCKET + "/" + file_path
    with fs.open(PATH,mode="w") as file:
        df.to_csv(file)