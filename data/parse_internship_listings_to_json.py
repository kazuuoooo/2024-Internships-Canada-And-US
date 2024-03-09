import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    rows = []

    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            rows.append(row)

    # Write the data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4)

    print(f"CSV data has been successfully converted to JSON and saved to {json_file_path}.")

# Define the CSV and JSON file paths
csv_file_path = 'internship_listings.csv'  # Update to your CSV file path
json_file_path = 'internship_listings.json'  # Update to your desired JSON output file path

# Convert the CSV to JSON
csv_to_json(csv_file_path, json_file_path)
