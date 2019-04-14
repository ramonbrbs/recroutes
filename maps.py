import googlemaps
import polyline
import poi
from datetime import datetime
from model.route import Route



gmaps = googlemaps.Client(key='AIzaSyAXP_Xrmn7tQxnJX1PRij18yuW8uaoe1Fc')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit

def get_directions(startPlace,endPlace,waypoints = None):
    return gmaps.directions(startPlace,endPlace,alternatives=True,waypoints=waypoints)


def poisPorRota(rota,pois,distance):
    pontos_de_rota = polyline.decode(rota['overview_polyline']['points'])

    pois_retorno = []
    for p in pontos_de_rota:
        pois_add = poi.poisInDistance(p,pois,distance)
        for poi_to_add in pois_add:
            if poi_to_add not in pois_retorno:
                pois_retorno.append(poi_to_add)
    return Route(rota,pois_retorno)

#['overview_polyline']['points']
if __name__ == '__main__':
    start_location = 'Aeroporto de Salvador'
    end_location = 'Farol da Barra'
    routes = get_directions(start_location,end_location)
    route = routes[0]
    
    pois = poi.loadJson()

    pois_route = poisPorRota(route,pois,1000)

    final_route = get_directions(start_location,end_location,waypoints=pois_route.get_pois_coordinates())
    print("FIM")
    #print(pois_retorno)
