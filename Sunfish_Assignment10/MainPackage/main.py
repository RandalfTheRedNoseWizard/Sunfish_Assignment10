# Name: Jared Rababy
# email:  Rababyjd@mail.uc.edu
# Assignment Number: Assignment_10
# Due Date:   11/1/2024
# Course #/Section: IS4010
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Retrieve, parse, and save API data to CSV file.

# Brief Description of what this module does: Fetches and exports Pokémon API data.
# Citations: https://www.w3schools.com/, https://www.stackoverflow.com
# Anything else that's relevant: 

# main.py

from apiPackage.api_client import PokemonAPI

def main():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    client = PokemonAPI(url)
    
    data = client.fetch_data()
    parsed_data = client.parse_data(data)
    client.write_to_csv(parsed_data)

if __name__ == "__main__":
    main()
