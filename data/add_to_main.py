import json

def append_listings(source_file, target_file):
    try:
        # Load listings from the source file
        with open(source_file, 'r') as file:
            new_listings = json.load(file)
        
        # Try to load existing listings from the target file
        try:
            with open(target_file, 'r') as file:
                existing_listings = json.load(file)
        except FileNotFoundError:
            # If the target file does not exist, start with an empty list
            existing_listings = []
        
        # Append new listings to existing listings
        updated_listings = existing_listings + new_listings
        
        # Write the updated listings back to the target file
        with open(target_file, 'w') as file:
            json.dump(updated_listings, file, indent=4)
        
        print("Listings have been successfully appended to", target_file)
        
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
source_file = './parsing/formatted_listings.json'
target_file = 'internship_listings.json'
append_listings(source_file, target_file)
