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
dataSet = pd.read_csv("csv/DOPCE2017.csv",sep=",")#,nrows=4
cid10 = pd.read_csv("csv/CID10-UTF-8.csv",sep=";")#,nrows=4
#dataSet.fillna(0)
#pattern = re.compile("^J.*$")
numOb = dataSet.count()[0]
numOfOccurrences = 0
disease = []
causaBase = pd.DataFrame(dataSet, columns = ['CAUSABAS','IDADE','LINHAA','LINHAB','LINHAC','LINHAD','LINHAII'])
causaBase.fillna(0)
#print(causaBase['LINHAA'].str.contains('J45').count())
#print(causaBase['LINHAB'].str.contains('J45').count())
#print(causaBase['LINHAC'].str.contains('J45').count())
#print(causaBase['LINHAD'].str.contains('J45').count())
#print(causaBase['LINHAII'].str.contains('J45').count())
#print(causaBase)
#CID10_09

obLA = causaBase[causaBase['LINHAA'].str.contains('J45')]
numObRespLA = obLA.count()[0]
'''
obLB = causaBase[causaBase['LINHAB'].str.contains('J')]
numObRespLB = obLB.count()[0]
obLC = causaBase[causaBase['LINHAC'].str.contains('J')]
numObRespLC = obLC.count()[0]
obLD = causaBase[causaBase['LINHAD'].str.contains('J')]
numObRespLD = obLD.count()[0]
obL2 = causaBase[causaBase['LINHAII'].str.contains('J')]
numObRespL2 = obL2.count()[0]
'''
#CID10_10
obResp = causaBase[causaBase['CAUSABAS'].str.contains('J')]
obAsma = causaBase[causaBase['CAUSABAS'].str.contains('J45')]
numObResp = obResp.count()[0]
numObAsma = obAsma.count()[0]
# print(Counter(causaBase['CAUSABAS']).most_common())
print("Obitos totais", numOb)
print("Obitos doencas Resp:", numObResp)
print("Obitos Asma:", numObAsma)
print("Obitos Asma LA:", numObRespLA)
'''
print("Obitos Resp LA:", numObRespLA)
print("Obitos Resp LB:", numObRespLB)
print("Obitos Resp LC:", numObRespLC)
print("Obitos Resp LD:", numObRespLD)
print("Obitos Resp L2:", numObRespL2)
'''

'''
for i in range(0,len(causaBase)):
	if(causaBase[i][0]=="J"):
		disease.append(causaBase[i])
		numOfOccurrences = numOfOccurrences+1
print(numOfOccurrences)
'''
#select only columns CAUSABAS and IDADE
#df = pd.DataFrame(dataSet, columns = ['CAUSABAS', 'IDADE'])
#print(Counter(disease).most_common())
#print("Obitos por Asma alergica:", sum(1*(dataSet['CAUSABAS']=="J450")))
#dataSet['IDADE']
#print("Obitos por Asma nao-alergica:",sum(1*(dataSet['CAUSABAS']=="J451")))
#print("Obitos por Asma mista:",sum(1*(dataSet['CAUSABAS']=="J458")))
#print("Obitos por Asma nao especificada:",sum(1*(dataSet['CAUSABAS']=="J459")))

#{'J189': 4133 (Pneumonia NE), 'J180': 2835 (Broncopneumonia NE), 'J440': 1730, 'J449': 1140,