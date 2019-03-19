import googlemaps
import polyline
import poi
from datetime import datetime



gmaps = googlemaps.Client(key='AIzaSyAXP_Xrmn7tQxnJX1PRij18yuW8uaoe1Fc')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit

def getDirections(startPlace,endPlace):
    return gmaps.directions(startPlace,endPlace,alternatives=True)


#['overview_polyline']['points']
if __name__ == '__main__':
    routes = getDirections('Aeroporto de Salvador','Farol da Barra')
    route = routes[0]
    points = polyline.decode(route['overview_polyline']['points'])
    pois = poi.loadJson()

    pois_retorno = []
    for p in points:
        pois_add = poi.poisInDistance(p,pois,1000)
        for poi_to_add in pois_add:
            if poi_to_add not in pois_retorno:
                pois_retorno.extend(pois_add)
    print(pois_retorno)
