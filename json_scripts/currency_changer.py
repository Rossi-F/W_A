import sys
import json

exchange_rate = float(sys.argv[1])
temp = 0

remove_rate = sys.argv[2]
with open(sys.argv[3], "r") as jsonFile:
    data = json.load(jsonFile)
    while temp != len(data):
        if (data[temp] != {}):
            data[temp]["P"] = data[temp]["P"].strip(remove_rate)
            print(data[temp]["P"])
            data[temp]["P"] = exchange_rate * float(data[temp]["P"])
        temp += 1

with open(sys.argv[3], "w") as jsonFile:
    json.dump(data, jsonFile, indent=0)