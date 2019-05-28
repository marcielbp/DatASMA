import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
'''
J450,
J45.1 Asma nao-alergica                            J451,
J45.8 Asma mista                                   J458,
J45.9 Asma NE                                      J459, J459 - Asma não especificada
'''
dataSet = pd.read_csv("csv/DOPSP2017.csv",sep=",")#,nrows=4
#dataSet.info()
#pattern = re.compile("^J.*$")
numOfOccurrences = 0
disease = []
for i in range(0,100000):
	if(dataSet['CAUSABAS'][i][0]=="J"):
		disease.append(dataSet['CAUSABAS'][i])
		numOfOccurrences = numOfOccurrences+1
print(numOfOccurrences)
#print(Counter(disease).most_common())
print("Obitos por Asma alergica:", sum(1*(dataSet['CAUSABAS']=="J450")))
print("Obitos por Asma nao-alergica:",sum(1*(dataSet['CAUSABAS']=="J451")))
print("Obitos por Asma mista:",sum(1*(dataSet['CAUSABAS']=="J458")))
print("Obitos por Asma nao especificada:",sum(1*(dataSet['CAUSABAS']=="J459")))

#{'J189': 4133 (Pneumonia NE), 'J180': 2835 (Broncopneumonia NE), 'J440': 1730, 'J449': 1140,