# ETL_Pipeline
## 1. import requests & import JSON
This script is a Python program that uses the requests and json libraries to retrieve data from the Pokémon API and extract information about Pikachu.

The first two lines of the script import the requests and json libraries, which are used to make HTTP requests and work with JSON data, respectively.

The next block of code makes a GET request to the Pokémon API’s endpoint for Pikachu using the requests.get() method. The response from the API is stored in the response variable.

The response.json() method is then called to parse the JSON data returned by the API and store it in the data variable.

Next, a dictionary called pokedata is created to store information about Pikachu. The dictionary has two keys: 'name' and 'stats'. The value of the 'name' key is set to the value of the 'name' key in the data dictionary, which contains Pikachu’s name.

The value of the 'stats' key is set using a dictionary comprehension. The comprehension iterates over the list of stats in the data['stats'] key, and for each stat, it creates a key-value pair where the key is the name of the stat (found in s['stat']['name']) and the value is the base stat (found in s['base_stat']). This creates a dictionary of Pikachu’s stats where each key is the name of a stat and its value is Pikachu’s base stat for that stat.

Finally, the script uses the json.dumps() method to convert the pokedata dictionary into a JSON-formatted string with an indentation of 2 spaces. This string is then printed to the console.

Overall, this script retrieves data from the Pokémon API about Pikachu, extracts its name and stats, and prints this information in a nicely formatted JSON string. Is there anything else you would like to know?This script is a Python program that uses the requests and json libraries to retrieve data from the Pokémon API and extract information about Pikachu.

The first two lines of the script import the requests and json libraries, which are used to make HTTP requests and work with JSON data, respectively.

The next block of code makes a GET request to the Pokémon API’s endpoint for Pikachu using the requests.get() method. The response from the API is stored in the response variable.

The response.json() method is then called to parse the JSON data returned by the API and store it in the data variable.

Next, a dictionary called pokedata is created to store information about Pikachu. The dictionary has two keys: 'name' and 'stats'. The value of the 'name' key is set to the value of the 'name' key in the data dictionary, which contains Pikachu’s name.

The value of the 'stats' key is set using a dictionary comprehension. The comprehension iterates over the list of stats in the data['stats'] key, and for each stat, it creates a key-value pair where the key is the name of the stat (found in s['stat']['name']) and the value is the base stat (found in s['base_stat']). This creates a dictionary of Pikachu’s stats where each key is the name of a stat and its value is Pikachu’s base stat for that stat.

Finally, the script uses the json.dumps() method to convert the pokedata dictionary into a JSON-formatted string with an indentation of 2 spaces. This string is then printed to the console.

Overall, this script retrieves data from the Pokémon API about Pikachu, extracts its name and stats, and prints this information in a nicely formatted JSON string. Is there anything else you would like to know?

