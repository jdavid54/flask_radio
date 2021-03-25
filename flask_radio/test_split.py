#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from predefines import host, port, txtFile, templateFile
#from flask_apscheduler import APScheduler
from predefines import isInteger, mpcCommand
import subprocess

stations = []
stationURLs = []
stationOutput = ''

for x in open('stations2.txt','r'):
    a = x.split("|") 
    stations.append(a[0]) 
    stationURLs.append(a[1].strip())
#print(stations)
#print(stationURLs)

position = 'gjgjqdjqjd[kljllfs'
position = mpcCommand(['mpc', '-f', '%position%'])
print('position',position)

idx = position.split(b'[')
print(idx)

for stationURL in stationURLs:
    mpcCommand(['mpc', 'add', stationURL])
    #mpcCommand(['mpc', 'play'])


position = idx[0].strip()
print(stations[int(position)-1])

if isInteger(position) == False:
    position = 0
x = 1
for station in stations:
    stationOutput += '<option value="' + str(x) + '" '
    
    if x == int(position):
        stationOutput += 'selected="selected"'
    stationOutput += '>' + station + '</option>'
    x += 1

#print(stationOutput)