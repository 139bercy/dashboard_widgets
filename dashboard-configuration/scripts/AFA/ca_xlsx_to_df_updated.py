# pip install openpyxl
import pandas as pd
df = pd.read_excel('BDD_CA_2021.xlsx',sheet_name='BASE',header=1)
df = df.loc[:160] # Pour éviter de prendre en compte les dernières lignes

## NATURE ##
df['nature'] = df['personne physique /personne morale'].map(lambda x: x.split()[1])

nature = prevenus.groupby('nature').size()

## SECTEUR ##
def quel_secteur(row):
    if not pd.isna(row['secteur économique public concerné ']):
        return 'PUBLIC'
    elif not pd.isna(row['secteur économique privé concerné ']):
        return 'PRIVE'
    else: 
        return 'PARTICULIER'

df['secteur'] = df.apply(quel_secteur,axis='columns')

## REPARTITION PAR FAMILLE D'INFRACTION ##
natinf = pd.read_excel('natinf_afa.XLSX',sheet_name=' AFA juin 2022')

def groupe_natinf(code):
    if pd.isna(code):
        return pd.NA

    tmp = natinf[natinf['N° Natinf']==int(code)]['Groupe']

    if len(tmp)==0:
        return pd.NA
    else:
        return tmp.values[0][3:]  

df['groupe'] = df['code NATINF des atteintes à la probité'].map(groupe_natinf).map(lambda x: pd.NA if type(x)==str and x in ['Blanchiment','Recel'] else x).str.upper().map(lambda x: ' '.join(x.split()[:3]) if type(x)==str else x)
part_infractions = df.groupby('groupe').size()

## INFORMATIONS LIEES AUX PREVENUS ##
# Identifie les prévenus de manière unique :
prevenus =  df.drop_duplicates(subset=['Fiche ','personne physique /personne morale'])

age_moyen = pd.Series(data=[prevenus['âge au moment des faits'].mean()],index=['Age moyen des prévenus'])

nb_prevenus_aff = pd.Series(data=[prevenus['Fiche '].value_counts().mean()],index=['Nombre moyen de prévenus par affaire']) 

sexe = prevenus.groupby('sexe').size()
sexe.index = sexe.index.str.upper()

qualite = prevenus.groupby('qualité des prévenus ').size()
#csp_autre = ['EMPLOYÉS DE COMMERCE','PROFESSIONS INTERMÉDIAIRES DE L\'ENSEIGNEMENT, DE LA SANTÉ, DE LA FONCTION PUBLIQUE ET ASSIMILÉS','PROFESSIONS LIBÉRALES ET ASSIMILÉS','EMPLOYÉS ADMINISTRATIFS D\'ENTREPRISE','OUVRIERS NON QUALIFIÉS','PERSONNELS DES SERVICES DIRECTS AUX PARTICULIERS','OUVRIERS QUALIFIÉS','COMMERÇANTS ET ASSIMILÉS']
#prevenus['Profession et catégorie socioprofessionnelle'] = prevenus['Profession et catégorie socioprofessionnelle'].map(lambda x: 'AUTRE' if x in csp_autre else x)

csp = prevenus.groupby('Profession et catégorie socioprofessionnelle').size()

repartition =  df.drop_duplicates(subset=['Fiche ','personne physique /personne morale','groupe']).groupby('groupe').size()

#prive_autre = ['AGRICULTURE SYLVICULTURE ET PÊCHE','ARTS, SPECTACLES ET ACTIVITÉS RÉCRÉATIVES','INFORMATION ET COMMUNICATION']
#prevenus['secteur économique privé concerné '] = prevenus['secteur économique privé concerné '].map(lambda x: 'AUTRE' if x in prive_autre else x) 
public_prive = prevenus.groupby('secteur').size() # Répartition par secteur 
public_prevenus = prevenus.groupby('secteur économique public concerné ').size() # Répartition par secteur public
prive_prevenus = prevenus.groupby('secteur économique privé concerné ').size() # Répartition par secteur privé


## AFFAIRES ##
affaires = df.drop_duplicates(subset=['Fiche ']) 
origine_autre = ['SIGNALEMENT AU PROCUREUR PAR UNE ASSOCIATION  OU UN PARTICULIER ','NOTIFICATION TRACFIN','ENQUETE / AUDIT INTERNE','ENQUETE D\'INITIATIVE ','SIGNALEMENT HATVP','DOSSIER CONNEXE JUSTICE']
affaires['origine de l’affaire'] = affaires['origine de l’affaire'].map(lambda x: 'AUTRE' if x in origine_autre else x) 
origine = affaires.groupby('origine de l’affaire').size()



## ISSUE ##  

# En théorie par infraction en pratique par affaire
moy_procédure = pd.Series(data=[df['durée de la procédure (entre la fin de la durée de prévention et jusqu\'à la décision de la CA)'].mean()],index=['Durée moyenne de la procédure'])
moy_prevention = pd.Series(data=[df['durée de la période de prévention\n(en nbr jours)'].mean()/365],index=['Durée moyenne de la période de prévention '])
moy_audiencement = pd.Series(data=[df['Durée entre les deux'].mean()/365],index=['Durée moyenne de la période d\'audiencement '])

sens_decision = df.groupby('sens de la décision par prevenu ').size()
sens_decision.index = sens_decision.index.str.upper()

type_de_peine = df.groupby('peines par prevenu').size()
type_de_peine.index = type_de_peine.index.str.upper() 

df['Confirmation/ infirmation de la décision relative à la culpabilité'] = df['Confirmation/ infirmation de la décision relative à la culpabilité'].map(lambda x: x.split()[0]+' CULPABILITE' if type(x)==str else x)
ci_culpa = df.groupby('Confirmation/ infirmation de la décision relative à la culpabilité').size()
ci_culpa.index = ci_culpa.index.str.upper()

ci_peines = df.groupby('Confirmation/ infirmaion des peines principales').size()
ci_peines.index = ci_peines.index.str.upper()

def quel_objet(row):
    if row['Culpabilité'] == 'OUI ' and row['Peine'] == 'OUI ':
        return 'CULPABILITE ET PEINE'
    elif row['Culpabilité'] == 'OUI ' and row['Peine'] == 'NON ':
        return 'CULPABILITE'
    elif row['Culpabilité'] == 'NON ' and row['Peine'] == 'OUI ':
        return 'PEINE'
    else:
        return 'AUTRE'

df['objet'] = df.apply(quel_objet,axis='columns')
objet = df.groupby('objet').size()

## PENALITES ##
# Il faut avoir en tête que la on prend en compte aussi ceux qui ne sont pas condamnés pour de la corruption
sanctions = df.drop_duplicates(subset=['Fiche ','personne physique /personne morale','durée de l\'emprisonnement (mois) ' ,'montant de l\'amende','montant de la confiscation ']) 

emprisonnement = pd.Series(data=[sanctions['durée de l\'emprisonnement (mois) '].mean()],index=['Durée moyenne de l’emprisonnement'])

amendes = sanctions.groupby('nature')['montant de l\'amende'].mean()
amendes.index = 'Montant moyen des amendes prononcées (Personnes '+amendes.index.str.capitalize()+'s)'
amendes = pd.concat([pd.Series(amendes.iloc[1], index=[amendes.index[1]]),pd.Series(amendes.iloc[0], index=[amendes.index[0]])])

#confiscations = pd.to_numeric(sanctions['montant de la confiscation '],errors='coerce').mean() Données insuffisantes

## SAUVEGARDE ##
to_save = pd.concat([part_infractions,public_prive,public_prevenus,prive_prevenus,repartition,nb_prevenus_aff,age_moyen,nature,sexe,qualite,csp,origine,objet,moy_procédure,moy_prevention,moy_audiencement,sens_decision,ci_culpa,ci_peines,type_de_peine,emprisonnement,amendes]).map(lambda x: round(x,1))
to_save.index = to_save.index.str.replace(',','').str.replace(';','').str.replace('- ','').str.rstrip()
to_save.to_csv('donnees_a_afficher.csv', header=True)
