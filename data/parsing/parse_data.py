import json
from datetime import datetime


def filter_and_format_listings(input_filename, output_filename):
    # Read the input JSON file
    with open(input_filename, 'r') as file:
        listings = json.load(file)

    # Process and format each listing
    formatted_listings = []
    for listing in listings:
        formatted_listing = {
            "company_name": listing.get('company_name', 'N/A'),
            "title": listing.get('title', 'N/A'),
            "locations": ', '.join(listing.get('locations', [])),
            "date_posted": (listing.get('date_posted', 0)),
            "terms": ', '.join(listing.get('terms', [])),
            "url": listing.get('url', '')
        }
        formatted_listings.append(formatted_listing)

    # Write the processed listings to the output JSON file
    with open(output_filename, 'w') as file:
        json.dump(formatted_listings, file, indent=4)

    print(f"Processed listings have been saved to {output_filename}")

# Example usage
input_filename = 'listings.json'
output_filename = 'formatted_listings.json'
filter_and_format_listings(input_filename, output_filename)
