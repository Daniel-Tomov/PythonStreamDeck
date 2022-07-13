from flask import Flask, jsonify, render_template, request
import webbrowser
import time
from playsound import playsound
from obsRequests import ws, loop, make_request, mute_audio_request, unmute_audio_request
from yml import items
app = Flask(__name__)


for i in range(0,3): print('')
print('OBS control like a Strem Deck by Daniel Tomov')
print('https://github.com/daniel-tomov/pythonstreamdeck')
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
            loop.run_until_complete(make_request({'scene-name':command[0]}, 'SetCurrentScene'))
        elif command[1] == "source":
            visibility = not loop.run_until_complete(make_request({'item': command[0]}, 'GetSceneItemProperties'))['visible']
            loop.run_until_complete(make_request({'item':command[0],'visible':visibility}, 'SetSceneItemProperties'))
        if (request.form['button'] == 'button5U'):
            loop.run_until_complete(unmute_audio_request('VAIO', 'SetVolume'))
        if (request.form['button'] == 'button5M'):
            loop.run_until_complete(mute_audio_request( 'VAIO', 'SetVolume'))#
        return render_template('index.html', buttons=items)
    #result = float(loop.run_until_complete(get_request('source', 'VAIO', 'GetVolume')))
    else:
        return render_template('index.html', buttons=items)

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)