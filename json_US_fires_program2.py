import json

infile = open('US_fires_9_14.json', 'r')

firesdata = json.load(infile)

list_of_fires = firesdata

brights, lats, lons = [],[],[]

for fire in list_of_fires:
    if fire['brightness'] > 450:
        bright = (fire['brightness'])
        lat = (fire['latitude'])
        lon = (fire['longitude'])
        brights.append(bright)
        lats.append(lat)
        lons.append(lon)
    

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline



data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [b//35 for b in brights],
        'color': brights,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }
}]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename='USfires_sept14.html')
