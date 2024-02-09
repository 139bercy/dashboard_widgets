import utils.fileManager as fm
import utils.dataManager as dm
import pandas as pd

data = fm.import_excel("DJ-2014-2020.xlsx",[1])
dm.prepareData(data)
    
# Graphique : Analyse par secteurs publics
def AnalyseSecteursActivite_Public(normal=False): 
    FichesLieesPublic = data.loc[data.secteurPublic.notna()].groupby('fiche')
    ActeursParFiche = FichesLieesPublic.secteurPublic.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
    
    values = data.secteurPublic.dropna().unique()
    proportion = {key: 0 for key in values}
    for fiche in ActeursParFiche:
        for acteurPublic in fiche:
            proportion[acteurPublic] += 1
            
    return pd.Series(proportion,name="Nombre de DJ pour chaque type d'acteur public").sort_values(ascending=False)

# Graphique : Analyse par secteurs privés
def AnalyseSecteursActivite_Prive(normal=False):
    FichesLieesPrive = data.loc[data.secteurPrive.notna()].groupby('fiche')
    ActeursParFiche = FichesLieesPrive.secteurPrive.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
    
    values = data.secteurPrive.dropna().unique()
    proportion = {key: 0 for key in values}
    for fiche in ActeursParFiche:
        for acteurPrive in fiche:
            proportion[acteurPrive] += 1
            
    return pd.Series(proportion,name="Nombre de DJ pour chaque type d'acteur privé").sort_values(ascending=False)

# Graphique : Répartition public/privé
def AnalyseSecteursActivite_RepartitionPublicPrive():
    return pd.Series([AnalyseSecteursActivite_Public().dropna().size,AnalyseSecteursActivite_Prive().dropna().size],index=["public","privé"])