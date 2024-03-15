import sys
import json
import requests
import collections

with open("PyShockConfig.json", "r") as jsonfile:
	jsonData = json.load(jsonfile)

url = 'https://do.pishock.com/api/apioperate/'

data = {
	'Username': jsonData["Username"],
	'Name': 'Py_API_Script',
	'Code': jsonData["Code"],
	'Intensity': jsonData["Intensity"],
	'Duration': jsonData["Duration"],
	'Apikey': jsonData["Apikey"],
	'Op': '1',
}

arg_names = ["command", "operation",  "intensity", "duration"]
args = dict(zip(arg_names, sys.argv))

Arg_list = collections.namedtuple("Arg_list", arg_names)
args = Arg_list(*(args.get(arg, None) for arg in arg_names))

if args[1]:
	Args1 = sys.argv[1].lower()
	if args[3]:
		data["Intensity"] = args[2]
		data["Duration"] = args[3]
	else:
		if args[2]:
			data["Duration"] = args[2]
else:
	print("Command line argument not provided, falling back to DefaultMode.")
	Args1 = jsonData["Mode"].lower()

if jsonData["TestMode"]:
	data["Op"] = "2"
	del data["Intensity"]
	print("TestMode On")
else:
	if "shock" in Args1: # Shock Mode
		data["Op"] = "0"
	elif "vibrate" in Args1: # Vibrate Mode
		data["Op"] = "1"
	elif "beep" in Args1 or "test" in Args1: # Beep Mode
		data["Op"] = "2"
		del data["Intensity"]
	else:
		print("Config error: DefaultMode INVALID.\nUsing Beep Mode.")
		data["Op"] = "2"
		del data["Intensity"]

response = requests.post(url, json=data)
print(response.text)
