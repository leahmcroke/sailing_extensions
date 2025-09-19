import asyncio
import boat_secrets
import json
import requests
import time
import websockets

BOAT_KEY = boat_secrets.boat_key
LATITUDE = -0.751391
NEW_COURSE = 270

def change_direction(course):

    new_direction_post = {
        'key': BOAT_KEY,
        'cmd': 'course',
        'value': course
    }

    change_dir_response = requests.post('https://8bitbyte.ca/sailnavsim/api/boatcmd.php', new_direction_post)

    print(f'Response: {change_dir_response.json()}')


def get_boat_data():

    boat_key = {'key': BOAT_KEY}

    get_data_response = requests.get('https://8bitbyte.ca/sailnavsim/api/boatinfo.php', boat_key)

    boat_data = get_data_response.json()

    return boat_data

def monitor_latitude():

    while(True):

        boat_data = get_boat_data()

        print(boat_data['lat'])

        if boat_data['lat'] < LATITUDE:
            change_direction(NEW_COURSE)
            print('changing course')
            break

        else:
            time.sleep(60)

        
if __name__ == '__main__':
    monitor_latitude()

