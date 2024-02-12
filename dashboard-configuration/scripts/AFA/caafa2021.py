import utils.fileManager as fm
import utils.dataManager as dm
import pandas as pd

datasetName = "DJ-2021"
data = fm.import_excel(datasetName + ".xlsx",[1])
dm.prepareData(data)

def getDatasetName():
    return datasetName
    
# Graphique : Analyse par secteurs publics
def donut_public_typeSecteur(normal=False):
    FichesLieesPublic = data.loc[data.secteurPublic.notna()].groupby('fiche')
    ActeursParFiche = FichesLieesPublic.secteurPublic.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
    
    values = data.secteurPublic.dropna().unique()
    proportion = {key: 0 for key in values}
    for fiche in ActeursParFiche:
        for acteurPublic in fiche:
            proportion[acteurPublic] += 1
            
    return pd.Series(proportion,name="Nombre de DJ pour chaque type d'acteur public").sort_values(ascending=False)