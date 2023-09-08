# ETL_Pipeline
## 1. import requests & import JSON
This Python script interacts with the Pokémon API to retrieve information about the character "Pikachu" and then formats and prints this data in a readable JSON format. Let's break down the script step by step:

import requests and import json: These lines import the necessary Python modules. The requests module is used to send HTTP requests, while the json module is used for working with JSON data.

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu'): This line sends an HTTP GET request to the URL "https://pokeapi.co/api/v2/pokemon/pikachu," which is an API endpoint for retrieving data about the Pokémon character "Pikachu." The response from the API is stored in the response variable.

data = response.json(): This line extracts the JSON data from the API response and parses it into a Python dictionary, which is stored in the data variable. This dictionary contains various attributes and statistics about Pikachu.

pokedata = {...}: This section of the script creates a new dictionary called pokedata to structure and format the data retrieved from the API. It includes the following information:

'name': Pikachu's name is directly taken from the data dictionary.
'stats': This is a nested dictionary that stores Pikachu's statistics. It uses a dictionary comprehension to iterate through the "stats" section of the data dictionary, extracting each statistic's name (e.g., "hp," "attack") and its base value.
print(json.dumps(pokedata, indent=2)): Finally, this line uses the json.dumps() method to convert the pokedata dictionary into a nicely formatted JSON string. The indent=2 argument specifies that the JSON should be indented by 2 spaces, making it more human-readable. The formatted JSON data is then printed to the console.

So, in summary, this script fetches data about Pikachu from the Pokémon API, extracts relevant information, structures it into a dictionary, and then formats and prints that data in a readable JSON format.

