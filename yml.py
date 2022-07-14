#    PythonStreamDeck, a control panel for OBS in html using obs-websocket and simpleobsws
#    Copyright (C) 2022  Daniel Tomov


import yaml
from yaml.loader import SafeLoader

items = []
data = yaml.load(open('config.yaml'), Loader=SafeLoader)
#print(data)

for item in data:
    #print(data[item]['img'])
    if 'min' in data[item]:
        items.append([item, data[item]['img'], data[item]['type'], '', 'audio', [data[item]['min'], data[item]['max']]])
    else:
        items.append([item, data[item]['img'], data[item]['type'], ''])
#print(items)