import pandas as pd
import json
import os


def convert_excel_to_json(path):
    """Exporte un json à partir d'un excel avec comme clef une ligne
    et comme valeur un dictionnaire: {colonne: value}"""
    df = pd.read_csv(path, sep=",")
    liste_panneaux = []
    panneau_properties = [
        "Lien_page_mesure",
        "Titre_panneau",
        "Volet",
        "source",
        "accordéon",
        "titre_page_mesure"
    ]
    onglet_properties = [
        "Carte",
        "Carte_titre",
        "Graph",
        "Graph_titre",
        "Graph_avec_valeurs",
        "Bar",
        "Bar_titre",
        "Box",
        "Box_titre",
        "Points",
        "MinGeoLevel",
        "Description_mesure",
        "Titre_onglet"
    ]
    indicateur_properties = [
        "Code_indicateur",
        "Nom_indicateur",
        "Indicateur_principal",
        "Titre_indicateur",
        "Unité_GP",
        "Unité_Evol",
    ]
    unique_bool_properties = [
        'Graph_avec_valeurs',
        'Pie_legende',
        'Avec_nom_indicateur'
    ]
    unique_text_properties = [
        'Pie_titre',
        'Graph_titre'
    ]
    isAfa = "afa.csv" in path
    if isAfa:
        onglet_properties.extend([
            'Pie',
            'Pie_titre',
            'Pie_legende',
            'Table',
            'Table_titre',
            'Info',
            'Info_titre',
            'Info_contenu'])

    df = df.dropna(subset=['No_Panneau']).sort_values(by=["No_Panneau"], ascending=True)
    panneaux = list(df["No_Panneau"].unique())
    for panneau in panneaux:
        dict_panneau = {}
        liste_onglets = []
        df_panneau = df[df["No_Panneau"] == panneau]
        df_panneau = df_panneau.sort_values(by=["No_Onglet"], ascending=True)
        onglets = list(df_panneau["No_Onglet"].unique())
        for onglet in onglets:
            dict_onglet = {}
            liste_indicateurs = []
            df_onglet = df_panneau[df_panneau["No_Onglet"] == onglet]
            df = df.sort_values(by=["Indicateur_principal"], ascending=False)
            indicateur = list(df_onglet["No_Onglet"].unique())
            for indicateur in range(len(df_onglet)):
                df_indicateur = df_onglet.iloc[indicateur]
                dict_indicateur = {}
                for col in indicateur_properties:
                    if col in df_indicateur.keys() and not pd.isna(df_indicateur[col]):
                        dict_indicateur[col] = str(df_indicateur[col])
                liste_indicateurs += [dict_indicateur]
            for col in onglet_properties:
                # ne pas intégrer les valeurs null ou autre
                if col in df_onglet and not pd.isna(df_onglet[col].iloc[0]):
                    if col in ["Carte", "Graph", "Points", "Bar", "Box", 'Pie', 'Table', 'Info']:
                        value = int(df_onglet[col].iloc[0])
                        if isAfa:
                            if value == 0:
                                dict_onglet[col] = False
                            else:
                                dict_onglet[col] = value
                        else:
                            if value == 1:
                                dict_onglet[col] = True
                            else:
                                dict_onglet[col] = False
                    elif not col in unique_text_properties and col not in unique_bool_properties:
                        dict_onglet[col] = str(df_onglet[col].iloc[0])

            for property in unique_text_properties:
                if property in df_onglet.keys():
                    property_values = df_onglet[df_onglet[property].notnull()][property].sort_index()
                    if not property_values.empty:
                        dict_onglet[property] = str(property_values.iloc[0])

            for property in unique_bool_properties:
                if property in df_onglet.keys():
                    dict_onglet[property] = bool(df_onglet[property].any())
            dict_onglet["indicateurs"] = liste_indicateurs
            liste_onglets += [dict_onglet]
        for col in panneau_properties:
            if not pd.isna(df_panneau[col].iloc[0]):
                dict_panneau[col] = str(df_panneau[col].iloc[0])
        dict_panneau["onglets"] = liste_onglets
        liste_panneaux += [dict_panneau]
    return liste_panneaux



def build_configuration(source: str, sink: str):
    json_final = convert_excel_to_json(path=os.path.join(
        os.getcwd(), "dashboard-configuration", source))

    with open(
        os.path.join(
            os.getcwd(),
            "public",
            sink
        ),
        'w',
        encoding="utf8"
    ) as f:
        json.dump(json_final, f, indent=4, ensure_ascii=False, sort_keys=False)


build_configuration("france-relance.csv", "france-relance.json")
build_configuration("afa.csv", "afa.json")
build_configuration("afa-2021.csv", "afa-2021.json")
build_configuration("impact.csv", "impact.json")
