import utils.fileManager as fm
import utils.formatManager as fom
import pandas as pd

import afa

test = fom.generateJsonDictDonut()
fm.export_ndjson(test,"line.ndjson")

