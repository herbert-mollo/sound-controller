from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/mute')
def mute():
    subprocess.run(["python", "sound_control.py", "mute"])
    return "Sound muted"

@app.route('/unmute')
def unmute():
    subprocess.run(["python", "sound_control.py", "unmute"])
    return "Sound unmuted"

@app.route('/')
def index():
    return open("index.html").read()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
