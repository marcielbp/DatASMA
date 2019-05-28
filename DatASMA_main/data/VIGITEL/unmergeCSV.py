import pandas as pd
d = pd.read_csv('VigitelDictFull.csv', sep=';')
d.fillna(method='ffill', inplace=True)
d.to_csv('VigitelDictFullOut.csv', sep=';', index=False)