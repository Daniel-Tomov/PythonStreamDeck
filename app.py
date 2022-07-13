from flask import Flask, jsonify, render_template, request
import webbrowser
import time
import asyncio
import simpleobsws
from playsound import playsound
import os
from netifaces import interfaces, ifaddresses, AF_INET

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='', loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.

app = Flask(__name__)

async def make_request(request, name, command):
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    #print(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(0)
    data = {request:name}
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
 
@app.route('/_stuff', methods = ['GET'])
def stuff():
    result = int(loop.run_until_complete(get_request('source', 'VAIO', 'GetVolume'))) + 1
    if result < 0.1:
        return jsonify(VAIOM='False')
    else:
        return jsonify(VAIOM='True')
    return jsonify(VAIOM='True')
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if (request.form['button'] == 'button1'):
            loop.run_until_complete(make_request('scene-name', 'Game Recording', 'SetCurrentScene'))
        if (request.form['button'] == 'button2'):
            loop.run_until_complete(make_request('scene-name', 'Camera', 'SetCurrentScene'))
        if (request.form['button'] == 'button3'):
            loop.run_until_complete(make_request('scene-name', 'Zoom Profile Pic', 'SetCurrentScene'))
        if (request.form['button'] == 'button4'):
            loop.run_until_complete(make_request('scene-name', 'Desktop recording', 'SetCurrentScene'))
        if (request.form['button'] == 'button5U'):
            loop.run_until_complete(unmute_audio_request('VAIO', 'SetVolume'))
        if (request.form['button'] == 'button5M'):
            loop.run_until_complete(mute_audio_request( 'VAIO', 'SetVolume'))
    result = float(loop.run_until_complete(get_request('source', 'VAIO', 'GetVolume')))
    if result < 0.1:
        return render_template('index.html', VAIOM='False')
    else:
        return render_template('index.html', VAIOM='True')
    #return render_template('index.html')

    
if __name__ == "__main__":
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        address = ' '.join(addresses)
        print(address)
        if (address == '192.168.0.105'):
            app.run(debug=False, host=address, port=5555)
            break
        if (address == '192.168.3.140'):
            app.run(debug=False, host=address, port=5555)
            break
        else:
            app.run(debug=False, host='0.0.0.0', port=5555)
            break
