import requests
import boat_secrets

class Race:

    def __init__(self, race_id):
        self.race_id = race_id

        response = requests.get('https://8bitbyte.ca/sailnavsim/api/raceinfo.php', {'id': self.race_id})
        race_data = response.json()

        self.finish_min_lat = race_data['finishMinLat']
        self.finish_min_lon = race_data['finishMinLon']
        self.finish_max_lat = race_data['finishMaxLat']
        self.finish_max_lon = race_data['finishMaxLon']
        
        self.finish_point = self.finish_point()

    def finish_point(self):
        finish_point_lat = ((self.finish_max_lat-self.finish_min_lat)/2)+self.finish_min_lat
        finish_point_lon = ((self.finish_max_lon-self.finish_min_lon)/2)+self.finish_min_lon
        return (finish_point_lat, finish_point_lon)


