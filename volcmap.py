import folium
import pandas as pd

volc_data = pd.read_csv("Volcanoes.txt")
volc_lat = list(volc_data["LAT"])
volc_lon = list(volc_data["LON"])
elev = list(volc_data["ELEV"])
name = list(volc_data["NAME"])
#print(volc_data.columns)
html = """
Volcano Information:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#map = folium.Map(location=[51.5007863, -0.1243937], zoom_start=10, tiles="Stamen Terrain")
map = folium.Map(location=[37.422724,-114.3825967], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(volc_lat, volc_lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")
