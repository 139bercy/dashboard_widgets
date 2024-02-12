# /!\ Ce fichier ne gère pas le format au sens de l'extension de fichier (fileManager le fait)
# mais dans le sens du formalisme encombrant attendu par le widget

import pandas as pd
import copy as cp

def donut_createLineData(code,value):

    values = {}
    values["date"] = "."
    values["value"] = value

    france = {}
    france["level"] = "."
    france["code_level"] = "."
    france["last_value"] = value
    france["last_date"] = "."
    france["evol_color"] = "."
    france["evol_percentage"] = "."
    france["evol"] = "."  
    france["values"] = values
    
    line = {}
    line["code"] = code
    line["nom"] = "."
    line["unite"] = "."
    line["france"] = [france]
    line["regions"] = [cp.deepcopy(france)]
    line["departements"] = [cp.deepcopy(france)]

    return line

def donut_createLineConf(volet,panneau,onglet,titre,description,source,code,name):

    dict = {
        "Volet" : volet,
        "No_Panneau" : 0,
        "Titre_panneau" : panneau,
        "No_Onglet" : 0,
        "Titre_onglet" : onglet,
        "Indicateur_principal" : 0,
        "Code_indicateur" : code,
        "Carte" : 0,
        "Carte_titre" : 0,
        "Graph" : 0,
        "Graph_titre" : 0,
        "Graph_avec_valeurs" : 0,
        "Bar" : 0,
        "Bar_titre" : 0,
        "Box" : 0,
        "Box_titre" : 0,
        "Points" : 0,
        "Pie" : 1,
        "Pie_titre" : titre,
        "Pie_legende" : 1,
        "Table" : 0,
        "Table_titre" : 0,
        "Info" : 0,
        "Info_titre" : 0,
        "Info_contenu" : 0,
        "Avec_nom_indicateur" : 0,
        "Avec_moyenne" : 0,
        "MinGeoLevel" : 0,
        "Titre_indicateur" : name,
        "Nom_indicateur" : name,
        "Lien_page_mesure" : 0,
        "Description_mesure" : description,
        "Unité_GP" : "Unité_GP",
        "Unité_Evol" : "%",
        "source" : source,
        "accordéon" : "Cliquez pour en savoir plus sur " + titre,
        "titre_page_mesure" : 0
    }
    
    return pd.Series(dict)
    
# data est une Series où les index sont les titres et la valeur leur valeur associée, le nom de la série est aussi utilisé
def donut_createListData(datasetName, data):
    list = []
    names = data.index.to_list()
    for i in range(data.size):
        code = datasetName + " | " + data.name + " | " + names[i]
        line = donut_createLineData(code, int(data.iloc[i]))
        list.append(line)
    return list
    
def donut_createListConf(datasetName, data, volet, panneau, onglet):
    lines = []
    description = "Voici une description"
    source = "Voici une source"
    names = data.index.to_list()
    for i in range(data.size):
        code = datasetName + " | " + data.name + " | " + names[i]
        line = donut_createLineConf(volet,panneau,onglet,data.name,description,source,code,names[i]).T
        lines.append(line)
    return pd.concat(lines,axis=1).T




