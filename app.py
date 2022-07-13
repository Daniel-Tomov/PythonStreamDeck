from flask import Flask, jsonify, render_template, request
import webbrowser
import time
from playsound import playsound
from obsRequests import ws, loop, make_request, mute_audio_request, unmute_audio_request, get_request 
from yml import data
app = Flask(__name__)

for i in range(0,3): print('')
print('OBS control like a Strem Deck by Daniel Tomov')
print('https://github.com/daniel-tomov/pythonstreamdeck')
print(data)
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
        if (request.form['button'] == 'button1'):
            loop.run_until_complete(make_request('scene-name', 'Game Recording', 'SetCurrentScene'))
        if (request.form['button'] == 'button2'):
            loop.run_until_complete(make_request('scene-name', 'Camera', 'SetCurrentScene'))
        if (request.form['button'] == 'button3'):
            loop.run_until_complete(make_request('scene-name', 'AFK', 'SetCurrentScene'))
        if (request.form['button'] == 'button4'):
            loop.run_until_complete(make_request('scene-name', 'Desktop Recording', 'SetCurrentScene'))
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
    app.run(debug=True, host="0.0.0.0", port=80)