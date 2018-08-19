import json
import os

os.chdir('/home/thomas/.config/google-chrome/Default/')

jsonFile = open('Preferences', "r")
data = json.load(jsonFile)
data['profile']['exited_cleanly'] = "true"
data['profile']['exit_type'] = "None"
jsonFile = open('Preferences', "w+")
jsonFile.write(json.dumps(data))
jsonFile.close()
