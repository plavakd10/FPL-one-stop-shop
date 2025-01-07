import urllib.request
import json

def managerid(id):
    
    fpl = "https://fantasy.premierleague.com/api/entry/{}".format(id)
    res = urllib.request.urlopen(fpl).read()
    jsonResponse = json.loads(res.decode('utf-8'))

    first_name = jsonResponse['player_first_name']
    last_name = jsonResponse['player_last_name']
    return [first_name,last_name]
