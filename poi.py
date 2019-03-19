from distance import *
import json


def loadJson():
    with open('data/poi.json') as f:
        return json.load(f)

'''
Dado um ponto, pesquisar na base de pontos de interesse, os que estao ate determinada distancia
'''
def poisInDistance(startPoint,pois,distance):
    r =  [p for p in pois if distanceBetween(startPoint,(p['latitude'],p['longitude'])) <= distance ]

    return r


if __name__=='__main__':
    print('a')
    pois = loadJson()
    start = (-13.0018049, -38.4819481)
    poisInDistance(start, pois, 1000)
    print('ok')