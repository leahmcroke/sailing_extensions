import requests
import asyncio
import websockets

def changeDirection():
    userInput = input("Input new Direction: ")

    newDirectionPost = {
        'key': 'e31096543ca32b74facde4a059828b69',
        'cmd': 'course',
        'value': userInput
    }

    changeDirection = requests.post('https://8bitbyte.ca/sailnavsim/api/boatcmd.php', newDirectionPost)

    print(f"Status Code: {changeDirection.status_code}")
    print(f"Response Body: {changeDirection.json()}")

def getData():
    boatkey = {
        'key': 'e31096543ca32b74facde4a059828b69',
    }

    response = requests.get('https://8bitbyte.ca/sailnavsim/api/boatinfo.php', boatkey)
    
    print(response.json())

async def webSocket():
    boatkey = {
        'key': 'e31096543ca32b74facde4a059828b69',
        'cmd': 'bdl'
    }
    
    async with websockets.connect('https://8bitbyte.ca/sailnavsim/snsws/v1/ws') as websocket:
        await websocket.send(boatkey)
        response = await websocket.recv()
        print(f"Received: {response}")
    
    #response = requests.post('https://8bitbyte.ca/sailnavsim/snsws/v1/ws', boatkey)
    

def main():
    asyncio.run(webSocket())
    
main()