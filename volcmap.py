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
def volc_colour(elevation):
    if elevation <= 1500:
        colour: str = "green"
    elif elevation <= 2500:
        colour: str = "orange"
    elif elevation > 2500:
        colour: str = "red"
    return colour

#map = folium.Map(location=[51.5007863, -0.1243937], zoom_start=10, tiles="Stamen Terrain")
the_map = folium.Map(location=[37.422724,-114.3825967], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(volc_lat, volc_lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(volc_colour(el))))

fgp = folium.FeatureGroup(name="Population Size")

fgp.add_child(folium.GeoJson(data=open("worldpopulation.txt", "r", encoding='utf-8-sig').read(),
             style_function=lambda x: {'fillColor': 'green' if x["properties"]["POP2005"] < 1000000
                                       else 'orange' if x["properties"]["POP2005"] <= 20000000 else 'red'}))

the_map.add_child(fgv)
the_map.add_child(fgp)
the_map.add_child(folium.LayerControl())
the_map.save("Map1.html")
