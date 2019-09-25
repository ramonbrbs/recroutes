
class Route:

    def __init__(self,googleRoute,pois):
        self.google_route = googleRoute
        self.pois = pois
        self.route_with_waypoints = False
        self.scores = []
        self.final_score = 0.0
        self.final_google_route = None
        self.final_distance = 0.0

    def get_pois_coordinates(self):
        pois_return = []
        for poi in self.pois:
            pois_return.append((poi['latitude'],poi['longitude']))
        return pois_return

    def get_final_score(self):
        self.final_distance = 0.0
        for l in self.final_google_route['legs']:
            self.final_distance += l['distance']['value']
        len_pois = len(self.pois)
        sum_score = sum([x[1] for x in self.scores])
        self.final_score = ((len_pois * sum_score)* 1000) / self.final_distance

    def print_final_info(self, legs = False):
        print("Rota por " + self.final_google_route['summary'])
        print("Distancia (metros): " + str(self.final_distance))
        print("Score final : " + str(self.final_score))
        print("POIs:")
        for p in self.pois:
            print(p['name'])
        if(legs):
            for l in self.final_google_route[u'legs']:
                for s in l[u'steps']:
                    print(s[u'html_instructions'])




    