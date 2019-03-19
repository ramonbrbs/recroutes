
class Route:

    def __init__(self,googleRoute,pois):
        self.google_route = googleRoute
        self.pois = pois
        self.route_with_waypoints = False

    def get_pois_coordinates(self):
        pois_return = []
        for poi in self.pois:
            pois_return.append((poi['latitude'],poi['longitude']))
        return pois_return


    