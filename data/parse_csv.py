import csv
import json
from datetime import datetime

# The path to your CSV file
csv_file_path = 'ribbon_listings.csv'

# The path to the JSON output file
json_file_path = 'output.json'

# Initialize an empty list to hold the converted JSON data
json_list = []

# Function to format date, assuming ISO 8601 format in your CSV
def format_date(date_str):
    try:
        # Assuming the date is in 'YYYY-MM-DD HH:MM:SS+00' format
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f+00").strftime("%Y-%m-%d")
    except ValueError:
        # Return original string if it doesn't match the format
        return date_str

# Open the CSV file for reading
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Reformat the 'posting_date' using the format_date function
        row['posting_date'] = format_date(row['posting_date'])
        
        # Append each row (already a dictionary matching your JSON structure) to the list
        json_list.append(row)

# Open the JSON file for writing
with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
    # Convert the list to JSON format and write to the file
    jsonfile.write(json.dumps(json_list, indent=4))

print(f"CSV data has been converted and saved to '{json_file_path}'")
