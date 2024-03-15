# Ce fichier contient toutes les informations pertinentes pour générer un graphique :
# - la méthode d'obtention des données
# - l'emplacement du graphique dans la configuration (volet, panneau, description, etc. -> mix contenant des informations de mise en forme)

import utils.fileManager as fm
import utils.formalismManager as form
import pandas as pd

class pageafa2021:

    def __init__(self, datasetName):
        self.datasetName = datasetName
        self.data = fm.import_excel(datasetName + ".xlsx",[1])
        form.prepareData(self.data)
        self.organisationPage = {} # a remplir

    # Graphiques
    #------------------------------------------------------------------------------------------------------------------------------------------------------#

    # PAS A JOUR -> ne fonctionnera pas #
    def AnalyseSecteursActivite_Public(self,normal=False): 
        FichesLieesPublic = self.data.loc[self.data.secteurPublic.notna()].groupby('fiche')
        ActeursParFiche = FichesLieesPublic.secteurPublic.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
        
        values = data.secteurPublic.dropna().unique()
        proportion = {key: 0 for key in values}
        for fiche in ActeursParFiche:
            for acteurPublic in fiche:
                proportion[acteurPublic] += 1
                
        return pd.Series(proportion,name="Nombre de DJ pour chaque type d'acteur public").sort_values(ascending=False)

    # PAS A JOUR -> ne fonctionnera pas #
    def AnalyseSecteursActivite_Prive(self,normal=False):
        FichesLieesPrive = self.data.loc[self.data.secteurPrive.notna()].groupby('fiche')
        ActeursParFiche = FichesLieesPrive.secteurPrive.unique() # Attention : On parle ici d'une colonne dont les valeurs sont des listes (c relou)
        
        values = data.secteurPrive.dropna().unique()
        proportion = {key: 0 for key in values}
        for fiche in ActeursParFiche:
            for acteurPrive in fiche:
                proportion[acteurPrive] += 1
                
        return pd.Series(proportion,name="Nombre de décisions pour chaque type d'acteur privé").sort_values(ascending=False)

    # PAS A JOUR -> ne fonctionnera pas #
    def AnalyseSecteursActivite_RepartitionPublicPrive(self,normal=False):
        return pd.Series([AnalyseSecteursActivite_Public().dropna().size,AnalyseSecteursActivite_Prive().dropna().size],index=["public","privé"])

    def CSP_in_PII(self,normal=False):
        
        natinfPII = [3530,3555,4430,10709,10710,12282,12283,12284,12285,12286,12287,22725,22726,22727,22728,22729,22730,29258,30151,30152,30153,30154,34342,34343]
        fichesPII = self.data.loc[self.data.codeNATINF.isin(natinfPII)]
        repartitionCSP = fichesPII.qualitePrevenus.value_counts()
        repartitionCSP_normalized = fichesPII.qualitePrevenus.value_counts(normalize=True)
        
        print(repartitionCSP)
        print(repartitionCSP_normalized)
    