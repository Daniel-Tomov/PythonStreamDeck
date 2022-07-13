import asyncio
import simpleobsws

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='', loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.


async def make_request(request, name, command):
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    data = {request:name}
    result = await ws.call(command, data) # Make a request with the given data
    #print(result)
    await ws.disconnect()

async def mute_audio_request(name, command):
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    data = {'source':name, 'volume':0.0}
    result = await ws.call(command, data) # Make a request with the given data
    #print(result)
    await ws.disconnect()


async def unmute_audio_request(name, command):
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    data = {'source':name, 'volume':0.5}
    result = await ws.call(command, data) # Make a request with the given data
    #print(result)
    await ws.disconnect()

async def mute_audio_request(name, command):
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    data = {'source':name, 'volume':0.0}
    result = await ws.call(command, data) # Make a request with the given data
    #print(result)
    await ws.disconnect()
    
async def get_request(request, name, command):
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    data = {request:name}
    result = await ws.call(command, data) # Make a request with the given data
    #print(result)
    await ws.disconnect()
    Array = []
    for value in result.values():
        Array.append(value)
    return Array[3]