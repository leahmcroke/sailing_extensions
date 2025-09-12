
import requests

class Boat:

    def __init__(self, boat_key):
        self.boat_key = boat_key


    @property
    def wind_speed(self):
        wind_speed = self.update_boat()['windSpeed']
        return wind_speed
    

    def update_boat(self):
        response = requests.get('https://8bitbyte.ca/sailnavsim/api/boatinfo.php', {'key': self.boat_key})
        updated_boat_data = response.json()
        return updated_boat_data
    
