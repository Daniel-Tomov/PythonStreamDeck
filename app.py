#    PythonStreamDeck, a control panel for OBS in html using obs-websocket and simpleobsws
#    Copyright (C) 2022  Daniel Tomov


from flask import Flask, jsonify, render_template, request
import webbrowser
import time
#from playsound import playsound
from obsRequests import ws, loop, make_request, get_items
from yml import items
app = Flask(__name__)


for i in range(0,3): print('')
print('OBS control like a Strem Deck by Daniel Tomov')
print('https://github.com/daniel-tomov/pythonstreamdeck')
print('PythonStreamDeck  Copyright (C) 2022  Daniel Tomov \nThis program comes with ABSOLUTELY NO WARRANTY; \nThis is free software, and you are welcome to redistribute it \nunder certain conditions. Such conditions include, but are not limited to: \nredistributing the program for a closed source version or asking others to pay for it.')
for i in range(0,3): print('')


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
        command = request.form['button'].split("|")
        if command[1] == "scene":
            loop.run_until_complete(make_request('SetCurrentScene', {'scene-name':command[0]}))
        elif command[1] == "source":
            visibility = not loop.run_until_complete(make_request('GetSceneItemProperties', {'item': command[0]}))['visible']
            loop.run_until_complete(make_request('SetSceneItemProperties', {'item':command[0],'visible':visibility}))
    
    loop.run_until_complete(get_items())
    return render_template('index.html', buttons=items)

    
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)