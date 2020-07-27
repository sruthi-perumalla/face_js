from flask import Flask,request, render_template,Response
import os
import json, requests, subprocess, shlex
from flask import url_for
import json
from camera import VideoCamera

global app

app = Flask(__name__)

@app.route('/opencv')
def opencv():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
