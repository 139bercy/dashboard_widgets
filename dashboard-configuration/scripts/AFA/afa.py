import utils.fileManager as fm
import pandas as pd

data = fm.import_excel("Test.xlsx",[1])
# customIndex

# Graphique : Analyse par secteurs publics
def AnalyseSecteursActivite_Public(normal=False):
    public = data.iloc[:,data.columns.isin(['secteur économique public concerné ','Fiche '])]
    public = public.dropna()
    public = public.rename(columns={"Fiche ": "fiche", "secteur économique public concerné ": "secteurEco"})
    group = public.groupby('fiche').agg(lambda x: x.unique())
    final = group.value_counts()
    print(group)
    return 0#public.value_counts(normalize=normal)

# Graphique : Analyse par secteurs privés
def AnalyseSecteursActivite_Prive(normal=False):
    prive = data.iloc[:,data.columns=='secteur économique privé concerné ']
    return prive.value_counts(normalize=normal)

# Graphique : Répartition public/privé
def AnalyseSecteursActivite_RepartitionPublicPrive():
    return pd.Series([AnalyseSecteursActivite_Public().dropna().size,AnalyseSecteursActivite_Prive().dropna().size],index=["public","privé"])