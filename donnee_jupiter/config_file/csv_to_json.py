import pandas as pd
import json 
import os


def convert_excel_to_json(path):
    """Exporte un json à partir d'un excel avec comme clef une ligne et comme valeur un dictionnaire: {colonne: value}"""
    df = pd.read_csv(path, sep = ",")
    json_final = {}
    column = list(df.columns)
    json_struc = ["No_mesure", "No_Indicateur"]
    for colonne_en_trop in json_struc:
        column.remove(colonne_en_trop)
    for panneau in df.No_mesure.unique():
        json_onglet = {}
        df_panneau = df[df.No_mesure == panneau]
        for onglet in df_panneau.No_Indicateur.unique():
            json_indicateur = {}
            df_onglet = df_panneau[df_panneau.No_Indicateur == onglet]
            for indicateur in df_onglet.Code_indicateur.unique() : 
                json_valeurs = {}
                df_indicateur = df_onglet[df_onglet.Code_indicateur == indicateur]             
                for i in range(len(df_indicateur)):
                    for col in column:
                        json_valeurs[col] = str(df_onglet.iloc[i][col])
                json_indicateur["Indicateur No {}".format(indicateur)] = json_valeurs
            json_onglet["Onglet No {}".format(onglet)] = json_indicateur
        json_final["Panneau No {}".format(panneau)] = json_onglet
    return json_final


json_final = convert_excel_to_json(path = os.path.join(os.getcwd(), "dashboard_widgets", "donnee_jupiter", "config_file", "Web_edito v_1.csv"))
    
with open(os.path.join(os.getcwd(), "dashboard_widgets", "donnee_jupiter", "config_file", "config_file.json"), 'w', encoding="utf8") as f:
    json.dump(json_final, f, indent=4, ensure_ascii=False, sort_keys=False )
with open(os.path.join(os.getcwd(), "dashboard_widgets", "public", "config_file.json"), 'w', encoding="utf8") as f:
    json.dump(json_final, f, indent=4, ensure_ascii=False, sort_keys=False )
    




