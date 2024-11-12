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

# api_client.py

# Import libraries
import requests  # For making HTTP requests to the API
import csv       # For writing data to a CSV file

class PokemonAPI:
    def __init__(self, url):
        # Build a URL with a data request
        self.url = url

    def fetch_data(self):
        """
        Step: Submitting to the API server,
        and receiving the results from the server.
        """
        response = requests.get(self.url)  # Make API request
        if response.status_code == 200:  # Check if request was successful
            return response.json()  # Receive and return results as JSON dictionary
        else:
            print("Failed to fetch data from the API.")
            return None

    def parse_data(self, data):
        """
        Step: Parsing the results into a Python dictionary.
        eExtracting some interesting data from the dictionary
        and printing it to the console in a friendly and informative format.
        """
        if data:
            # Extract specific details from the data
            name = data.get('name', 'N/A').capitalize()  # Get and format the name
            base_experience = data.get('base_experience', 'N/A')  # Get base experience
            abilities = [ability['ability']['name'] for ability in data.get('abilities', [])]  # List abilities
            types = [poke_type['type']['name'] for poke_type in data.get('types', [])]  # List types

            # Print the information in a friendly format and informative format
            print(f"Pokemon: {name}")
            print(f"Base Experience: {base_experience}")
            print("Abilities:", ", ".join(abilities))
            print("Types:", ", ".join(types))

            # Return the extracted information as a dictionary
            return {
                "Name": name,
                "Base Experience": base_experience,
                "Abilities": ", ".join(abilities),
                "Types": ", ".join(types)
            }
        else:
            print("No data to parse.")
            return {}

    def write_to_csv(self, parsed_data):
        """
        Step: Write results to a .CSV file.
        Converting JSON to CSV.
        """
        if parsed_data:
            with open('pokemon_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Attribute", "Value"])  # Write headers
                # Write each key-value pair from the parsed data dictionary
                for key, value in parsed_data.items():
                    writer.writerow([key, value])
            print("Data saved to pokemon_data.csv")
        else:
            print("No data to write to CSV.")
