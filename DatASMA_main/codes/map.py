import folium
import pandas as pd
estadosData = pd.read_csv("obito1000_2014.csv")
print(estadosData)
mapa = folium.Map(location=[-15.788497,-47.879873],tiles='Mapbox Bright', zoom_start=7)
folium.Choropleth(geo_data='estados.json',data=estadosData,key_on='feature.properties.SIGLA',columns=['UF', 'taxa'],fill_color='YlOrRd',fill_opacity=0.5,line_color='white',line_weight=1).add_to(mapa)
#folium.Marker([-19.9166813,-43.9344931]).add_to(mapa)
mapa.save("mapa.html") 

