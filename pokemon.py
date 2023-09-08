import requests
import json

response = requests.get(
    'https://pokeapi.co/api/v2/pokemon/pikachu'
)

data = response.json()

pokedata = {
    'name': data[ 'name'],
    'stats': {
        s['stat']['name']:s['base_stat']
        for s
        in data['stats'] 
    }
}

print(json.dumps(
    pokedata,
    indent=2
))

