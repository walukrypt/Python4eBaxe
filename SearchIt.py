import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://gamersbaxe.wordpress.com")    
print(json.dumps(response.json(), ident=2))
    