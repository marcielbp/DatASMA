import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns
import time
import os

#input files
fp = "SHAPES/municipios.json"
fp2 = "SHAPES/estados.shp"
cidadesBR = pd.read_csv("csv/muniBR-UTF-8.csv",delimiter=',')
dataSet = pd.read_csv("csv/DOPCE2017.csv",sep=",")
#cid10 = pd.read_csv("csv/CID10-UTF-8.csv",sep=";")
output_path = 'mapas/'

#select dataframe
dataFrameBase = pd.DataFrame(dataSet, columns = ['CODMUNRES','IDADE','CAUSABAS'])
onlyAsma = dataFrameBase[dataFrameBase['CAUSABAS'].str.contains('J45')]

logicIndex = cidadesBR['uf'].str.contains('CE')
citiesUF = cidadesBR[logicIndex]

data = gpd.read_file(fp)
data['OB_ASMA']=0
data['POPULACAO']=0
values = onlyAsma['CODMUNRES'].value_counts().keys().tolist()
counts = onlyAsma['CODMUNRES'].value_counts().tolist()
numCounts = len(counts)

# set numOBAsma in each city
for i in range(0,numCounts):
	data.OB_ASMA[data.GEOCODIGO.str.contains(str(values[i]))]=counts[i]

fig = data.plot(column='OB_ASMA',cmap='OrRd')
fig.axis('off')
filepath = os.path.join(output_path, '_municipios_AsmaDeaths.png')
chart = fig.get_figure()
chart.savefig(filepath, dpi=600)
