import json
from datetime import datetime

# Function to convert timestamp to readable date
def format_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

# Read the JSON data from the file
with open('listings.json', 'r', encoding='utf-8') as file:
    listings = json.load(file)

# Start creating the markdown content for the README
markdown_content = "# Internship Listings for Summer 2024\n\n"
markdown_content += "| Company Name | Title | Location(s) | Date Posted | Terms | Listing URL |\n"
markdown_content += "|--------------|-------|-------------|-------------|-------|-------------|\n"

# Loop through each listing and add it to the markdown content
for listing in listings:
    company_name = listing.get('company_name', 'N/A')
    title = listing.get('title', 'N/A')
    locations = ', '.join(listing.get('locations', []))
    date_posted = format_date(listing.get('date_posted', 0))
    terms = ', '.join(listing.get('terms', []))
    url = listing.get('url', '')

    markdown_content += f"| {company_name} | {title} | {locations} | {date_posted} | {terms} | [Link]({url}) |\n"

# Write the markdown content to README.md
with open('README.md', 'w', encoding='utf-8') as readme_file:
    readme_file.write(markdown_content)

print("README.md has been created successfully.")
