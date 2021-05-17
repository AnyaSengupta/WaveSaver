import folium
import pandas
df=pandas.read_csv("CA_Beaches_Dataset.txt")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors')

points_name = [df['NAME']]

def color(tide): 
    if tide == 1:
        col='darkgreen'
    elif tide == 2:
        col='green'
    else:
        col='orange'
    return col
fg=folium.FeatureGroup(name="Volcano Locations")
for lat,lon,name,tide in zip(df['LAT'],df['LON'],df['NAME'],df['TIDE']):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(name)),icon=folium.Icon(color=color(tide),icon_color='black')))
map.add_child(fg)
map.add_child(folium.LayerControl())
plugins.Search(points_name, search_zoom=20, ).add_to(map)
map.save(outfile='map.html')