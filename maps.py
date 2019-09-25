# coding=utf-8

import googlemaps
import polyline
import poi
from datetime import datetime
from model.route import Route
from recommender import *
import pandas as pd



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

pois = poi.loadJson()


start_location = 'Aeroporto de Salvador'
end_location = 'Shopping Barra'

def score_by_route(route):
    pois_route = poisPorRota(route,pois,300)
    pois_route.final_google_route = get_directions(start_location, end_location,waypoints=pois_route.get_pois_coordinates())[0]
    pois_route_df = pd.DataFrame(pois_route.pois)
    pois_user_df = pd.read_json('data/poi2.json')
    pois_route.scores = recommend(pois_route_df, pois_user_df)
    pois_route.get_final_score()
    return pois_route

#['overview_polyline']['points']
if __name__ == '__main__':
    routes = get_directions(start_location,end_location)

    pois_routes = []
    for route in routes:
        pois_routes.append(score_by_route(route))

    pois_routes.sort(key=lambda x: x.final_score, reverse=True)

    for p in pois_routes:
        print('-----------')
        p.print_final_info()
        print('-----------')

    #final_route = get_directions(start_location,end_location,waypoints=pois_route.get_pois_coordinates())
    print("FIM")
    #print(pois_retorno)
