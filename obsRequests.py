#    PythonStreamDeck, a control panel for OBS in html using obs-websocket and simpleobsws
#    Copyright (C) 2022  Daniel Tomov




import asyncio
from simpleobsws import simpleobsws
from yml import items
from time import sleep

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='xViZuAgPWTJbSwVK', loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.


async def make_request(command, data={}):
    await ws.connect() # Make the connection to OBS-Websocket
    #result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    result = await ws.call(command, data) # Make a request with the given data
    #print(result)
    await ws.disconnect()
    return result

async def get_items():
    await ws.connect() # Make the connection to OBS-Websocket
    #result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    result = await ws.call('GetCurrentScene', {}) # Make a request with the given data
    #print(result)
    sceneName = result['name']
    activeSources = []
    for source in result['sources']:
        activeSources.append(source['name'])
    for i in items:
        if sceneName == i[0] and i[2] == 'scene':
            i[3] = True
        elif i[2] == 'scene':
            i[3] = False
        for source in result['sources']:
            sourceName = source['name']
            render = source['render']
            
            if i[0] == sourceName and i[2] == 'source' and (render == True or render == False):
                i[3] = render
            elif i[2] == 'source' and i[0] not in activeSources:
                i[3] = 'disabled'


        #print(items)


    await ws.disconnect()
    return result