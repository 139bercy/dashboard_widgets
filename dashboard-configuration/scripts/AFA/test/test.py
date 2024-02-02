# Ces lignes permettent d'appeler les modules/scripts du dossier parent (="AFA")
# Attention il faut que le terminal soit dans le dossier du script pendant l'execution comme le chemin est relatif
import sys
sys.path.append("..")

import fileManager as fm

data = fm.import_excel("DJ-2021.xlsx",[0,1])
print(data.iloc[0])