
import Boat
import Race
import boat_secrets

my_boat = Boat.Boat(boat_secrets.boat_key)

print(my_boat.wind_speed)

my_race = Race.Race(boat_secrets.race_id)

print(my_race.finish_point)