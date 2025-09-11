import asyncio
import json
import requests
import boat_secrets
import websockets

BOAT_KEY = boat_secrets.boat_key
RACE_ID = boat_secrets.race_id

def changeDirection():
    userInput = input("Input new Direction: ")

    newDirectionPost = {
        'key': BOAT_KEY,
        'cmd': 'course',
        'value': userInput
    }

    changeDirection = requests.post('https://8bitbyte.ca/sailnavsim/api/boatcmd.php', newDirectionPost)

    print(f"Status Code: {changeDirection.status_code}")
    print(f"Response Body: {changeDirection.json()}")

def getData():
    boatkey = {
        'key': BOAT_KEY
    }

    response = requests.get('https://8bitbyte.ca/sailnavsim/api/boatinfo.php', boatkey)
    
    print(response.json())

async def webSocket():
    boatkey = {
        'key': BOAT_KEY,
        'cmd': 'bdl'
    }
    
    boatkey = json.dumps(boatkey)

    async with websockets.connect('wss://8bitbyte.ca/sailnavsim/snsws/v1/ws') as websocket:
        await websocket.send(boatkey)
        while True:
            response = await websocket.recv()
            print(f"Received: {response}")
    
    #response = requests.post('https://8bitbyte.ca/sailnavsim/snsws/v1/ws', boatkey)
    

def main():
    asyncio.run(webSocket())
    # getData()
    
main()