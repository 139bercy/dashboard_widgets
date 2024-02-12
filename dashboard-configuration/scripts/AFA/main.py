import utils.fileManager as fm
import utils.formalismManager as fom
import pandas as pd

import afa

datasetName = afa.getDatasetName()
data = afa.AnalyseSecteursActivite_Prive()
#list = fom.donut_createListData(datasetName, data)
conf = fom.donut_createListConf(datasetName, data, "v", "p", "o")
fm.export_csv(conf,"testconf.csv")
