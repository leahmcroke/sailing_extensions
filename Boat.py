
import requests
import time

class Boat:

    def __init__(self, boat_key):
        self.boat_key = boat_key
        self._boat_data_cache = None
        self._last_refresh_time = 0
        self._cache_duration_sec = 60


    def _update_boat_data(self):
        response = requests.get('https://8bitbyte.ca/sailnavsim/api/boatinfo.php', {'key': self.boat_key})
        self._boat_data_cache = response.json()
        self._last_refresh_time = time.time()
        print('Updated boat data cache')
    

    def _is_cache_stale(self):
        if self._boat_data_cache is None:
            return True
        return (time.time() - self._last_refresh_time) > self._cache_duration_sec

    
    @property
    def time(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('time')
    

    @property
    def lat(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('lat')
    
    @property
    def lon(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('lon')
    
    
    @property
    def course_water(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('courseWater')
    

    @property
    def speed_water(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('speedWater')
    

    @property
    def track_ground(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('trackGround')
    

    @property
    def speed_ground(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('speedGround')
    

    @property
    def wind_dir(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('windDir')
    

    @property
    def wind_speed(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('windSpeed')
    

    @property
    def wind_gust(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('windGust')
    

    @property
    def ocean_current_dir(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('oceanCurrentDir')
    

    @property
    def ocean_current_speed(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('oceanCurrentSpeed')
    

    @property
    def ocean_ice(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('oceanIce')
    

    @property
    def distance_travelled(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('distanceTravelled')


    @property
    def damage(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('damage')
    

    @property
    def wave_height(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('waveHeight')
    

    @property
    def leeway_speed(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('leewaySpeed')
    

    @property
    def heeling_angle(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('heelingAngle')
    

    @property
    def race(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('race')
    

    @property
    def waypoints_reached(self):
        if self._is_cache_stale():
            self._update_boat_data()
        return self._boat_data_cache.get('waypointsReached')

