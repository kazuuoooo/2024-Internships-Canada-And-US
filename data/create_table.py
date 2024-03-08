import json
from datetime import datetime

def format_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%b %d, %Y')


with open('header.md', 'r', encoding='utf-8') as header_file:
    header_content = header_file.read()

with open('internship_listings.json', 'r', encoding='utf-8') as file:
    listings = json.load(file)


markdown_content = header_content + "\n\n# Internship Listings for Summer 2024\n\n"
markdown_content += "| Company | Role | Location(s) | Apply | Date Posted |\n"
markdown_content += "|--------------|------------------|---------------|-------------|------------------------|\n"

sorted_listings = sorted(listings, key=lambda x: x.get('date_posted', 0), reverse=True)

for listing in listings:
    company_name = listing.get('company_name', 'N/A')
    title = listing.get('title', 'N/A')
    locations = ', '.join(listing.get('locations', []))
    date_posted = format_date(listing.get('date_posted', '0'))
    terms = ', '.join(listing.get('terms', []))
    url = listing.get('url', '')
    link_button = (f'<p align="center">'
               f'  <a href="{url}" target="_blank">'
               f'    <img src="data/images/applybutton.png" alt="Apply Button" style="width:150px;">'
               f'  </a>'
               f'</p>'
               f'<p align="center">'
               f'  <img src="data/images/applybutton.png" alt="Intern Insider" style="width:75px;">'
               f'  <img src="data/images/applybutton.png" alt="Ribbon" style="width:75px;">'
               f'</p>')

    markdown_content += f"| {company_name} | {title} | {locations} | {link_button} | {date_posted} |\n"


with open('../README.md', 'w', encoding='utf-8') as readme_file:
    readme_file.write(markdown_content)

print("README.md has been created successfully.")
