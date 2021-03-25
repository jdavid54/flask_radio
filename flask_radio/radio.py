#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from predefines import host, port, txtFile, templateFile

from predefines import isInteger, mpcCommand
import subprocess

import webbrowser

app = Flask(__name__)

def update_list(stations, position):
    x = 1
    stationOutput = ''
    for station in stations:
        stationOutput += '<option value="' + str(x) + '" '
        if x == int(position):
            stationOutput += 'selected="selected"'
        stationOutput += '>' + str(x) + ' - ' + station + '</option>'
        x += 1
    return stationOutput

@app.route('/', methods=['GET', 'POST'])
def hello_world(name='Flask Home FM ',css='styles.css'):
    stations = []
    stationURLs = []
    stationOutput = ''

    #read stations data from file
    for x in open('stations2.txt','r'):
        a = x.split("|")
        stations.append(a[0])
        stationURLs.append(a[1].strip())

    #add URL to list
    for stationURL in stationURLs:
        mpcCommand(['mpc', 'add', stationURL])

    #get current position
    position = mpcCommand(['mpc', '-f', '%position%'])
    idx = position.split(b'[')
    position = idx[0].strip()
    if isInteger(position) == False:
        position = 0

    #process post messages from html form
    if request.method == 'POST':
        if request.form['submit'] == 'turn radio on':
            mpcCommand(['mpc', 'play'])
        elif request.form['submit'] == 'turn radio off':
            mpcCommand(['mpc', 'stop'])
        elif request.form['submit'] == 'change':
            mpcCommand(['mpc', 'play', str(request.form['station'])])
        elif request.form['submit'] == 'next station':
            mpcCommand(['mpc', 'next'])
            position  = int(position)+1
            mpcCommand(['mpc', 'play', stations[position]])
        elif request.form['submit'] == 'previous station':
            mpcCommand(['mpc', 'prev'])
            position = int(position) - 1
            mpcCommand(['mpc', 'play', stations[position]])
        elif request.form['submit'] == '+5':
            mpcCommand(['mpc', 'volume', '+5'])
        elif request.form['submit'] == '-5':
            mpcCommand(['mpc', 'volume', '-5'])
        elif request.form['submit'] == 'update playlist':
            mpcCommand(['mpc', 'clear'])

    # update position
    position = mpcCommand(['mpc', '-f', '%position%'])
    idx = position.split(b'[')
    position = idx[0].strip()
    if isInteger(position) == False:
        position = 0

    #update form list to show the selected station
    stationOutput = update_list(stations, position)
    volume = mpcCommand(['mpc', 'volume'])
    return render_template(templateFile, name=name, stations=stationOutput.strip(), volume=volume)



if __name__ == '__main__': 
    app.run(host=host, port=port, debug=True)
    # launch flask web page 
    webbrowser.open("http://localhost:1234", new=1)
        
