# python prototype to create virtual room
#---------------------------------------
# 
# get server certificate into a file before running:
# openssl s_client -connect demo.6connexlocal.com:443 -servername demo.6connexlocal.com -showcerts > cert.pem

import json
import hjson
from pprint import pprint
import requests


def mapNode(node):    
    d = {}
    d['selections'] = []
    d['bgImage'] = ''
    d['x'] = node['x']
    d['y'] = node['y']
    d['label'] = None
    d['name'] = None
    d['id'] = -1
    d['type'] = 'banner'
    d['url'] = ''
    d['width'] = node['width']
    d['height'] = node['height']
    return d

def mapNodes(nodes):
    return [ mapNode(n) for n in nodes ]

def mapTemplate(template):
    d = {}
    d['templateType'] = template['templateType']
    d['templateId'] = template['templateId']
    d['bgImage'] = template['bgImage']
    d['bgImageHeight'] = template['bgImageHeight']
    d['bgImageWidth'] = template['bgImageWidth']
    d['fgImage'] = template['fgImage']
    d['fgImageHeight'] = template['fgImageHeight']
    d['fgImageWidth'] = template['fgImageWidth']
    d['flvHeight'] = template['flvHeight']
    d['flvWidth'] = template['flvWidth']
    d['walkingPeopleFlvPath'] = template['walkingPeopleFlvPath']
    d['thumbnail'] = template['thumbnail']
    d['nodes'] = mapNodes(template['nodes'])
    return d

# Get a virtual room 
url = "https://demo.6connexlocal.com/controlpanel/canvas-trendy/virtual-builder/room/22"
session = requests.Session()
session.auth = ('test@6connex.com', 'qwertyui1!')
session.verify ='cert.pem'
response = session.get(url)

virtualroom = hjson.loads(response.text)

# Mapping of virtual room json output to input needed by creation endpoint
creationInput = {}
creationInput['settings'] = virtualroom['settings']
# change key settings to avoid collision:
creationInput['settings']['description'] = 'NewBooth'
creationInput['settings']['name'] = 'NewBooth'
creationInput['settings']['locationKey'] = 'NewBooth'

creationInput['template'] = mapTemplate(virtualroom['template'])

print(json.dumps(creationInput, indent=2, sort_keys=False))

# Create a virtual room using the creation endpoint
curl = "https://demo.6connexlocal.com/controlpanel/canvas-trendy/virtual-builder/"
response = session.post(curl, json=json.dumps(creationInput))
pprint(response)
