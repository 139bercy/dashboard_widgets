import pandas as pd
import csv
import json
import copy

config = pd.read_csv('afa-2021.csv',sep=",") # Configuration à mettre à jour
data = pd.read_csv('donnees_a_afficher.csv',sep=',') # Nouvelles données i.e. sans la phase test
# Mettre data-test.ndjson à la racine


## STEP 1 ##
# On s'assure que la nouvelle config ait les bons noms d'indicateurs, on génére les nouveaux codes, et on exporte

config['Titre_indicateur'] = data.iloc[:,0]
config['Nom_indicateur'] = data.iloc[:,0]
config['Code_indicateur'] = config['Titre_onglet']+'_'+config['Titre_panneau']+'_'+data.iloc[:,0]
config.to_csv('afa-2021.csv',sep=',',index=False,quoting=csv.QUOTE_NONNUMERIC)



## ETAPE 2 ##
# Maintenant que l'on connait les code indicateurs on peut produire le ndjson

df = pd.DataFrame()
df['code'] = config['Code_indicateur'] 
df['number'] = data['0'] 

def append_to_list(code,number,list_of_dicts,date='2021-01-01'):

    values = {
        'date': date,
        'value': number
    }

    framework = {
        'level': '',
        'code_level': 0,
        'last_value': number,
        'last_date': date,
        'evol': 0,
        'evol_percentage':0,
        'evol_color':'red',
        'values': [values]
    }

    fra = copy.deepcopy(framework)
    fra['level'] = 'nat'
    fra['code_level'] = 'fra'

    reg = copy.deepcopy(framework)
    reg['level'] = 'reg'

    dep = copy.deepcopy(framework)
    dep['level'] = 'reg'

    elt = {
        'code' : code,
        'nom': '.',
        'unite': '.',
        'france': [fra],
        'regions': [reg],
        'departements': [dep],    
    }

    list_of_dicts.append(elt)


def df_to_ndjson(df,name_of_file,mode):
    liste = []

    df['number'] = df['number'].astype(float)
    for i in range(len(df)):
        append_to_list(df['code'].iloc[i],df['number'].iloc[i],liste)

    path_to = ''

    if mode=='a':
        with open(path_to+"data-test"+".ndjson", 'r') as file:
            for line in file:
                liste.append(json.loads(line))

    with open(path_to+name_of_file+".ndjson", 'w', encoding="utf-8") as file:
        for item in liste:
            json_str = json.dumps(item)
            file.write(json_str + "\n")


# Modifie le "w" en "a" pour ajouter à l'existant
df_to_ndjson(df,'data','a')