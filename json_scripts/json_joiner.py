import sys
import json

with open(sys.argv[1], "r") as jsonFile:
    with open(sys.argv[2], "r") as scndJsonFile:
        first_data = json.load(jsonFile)
        second_data = json.load(scndJsonFile)
        with open("file.json", "w") as jsonFile:
            json.dump(first_data, jsonFile, indent=0)            
            json.dump(second_data, jsonFile, indent=0)

