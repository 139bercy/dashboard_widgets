import pandas as pd

# Douloureux à écrire, génère le modèle qui marche pour les pie_charts
def generateJsonDictDonut():

    values = {}
    values["date"] = "."
    values["value"] = "."

    france = {}
    france["level"] = "."
    france["code_level"] = "."
    france["last_value"] = "."
    france["last_date"] = "."
    france["evol_color"] = "."
    france["evol_percentage"] = "."
    france["evol"] = "."  
    france["values"] = values
    
    line = {}
    line["code"] = "."
    line["nom"] = "."
    line["unite"] = "."
    line["france"] = [france]
    line["regions"] = [france.copy()]
    line["departements"] = [france.copy()]

    return line
    
# donut est une Serie où les index sont les titres et la valeur ler valeur associée
def generateDonutData(dataset, donut):
    return
    

def generateDonutConf(df):
    return