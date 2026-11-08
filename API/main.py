""" 

API (Application Programming Interface):

    An API (Application Programming Interface) acts as a software messenger. It allows your Python script to talk to another 
    server or service to fetch real-time data, send messages, or trigger actions.


JSON: 

    JSON (JavaScript Object Notation) is a lightweight, 
    text-based format used for storing and transporting data.

    * This format follows the rules of a python directory. It consists of Keys and Values. 
    






"""

import sys 
import requests

if len(sys.argv) != 2: 
    sys.exit


response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=", sys.argv[1])

print(response.json())


r = response.json()

for result in r["Result"]: 
    print(result["trackName"])

    