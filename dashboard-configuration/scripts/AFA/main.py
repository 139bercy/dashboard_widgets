import utils.fileManager as fm
import utils.formalismManager as fom
import pandas as pd

import caafa2021 as page


datasetName = page.getDatasetName()
data = page.donut_public_typeSecteur()

list = fom.donut_createListData(datasetName, data)

volet = "Analyse par secteurs d’activité"
panneau = "Secteur public"
onglet = "Données 2021"
conf = fom.donut_createListConf(datasetName, data, volet, panneau, onglet)

fm.export_ndjson(list,"widget-ca-afa-2021.ndjson")
fm.export_csv(conf,"conf-ca-afa-2021.csv")
