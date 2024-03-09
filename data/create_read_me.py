import json
from datetime import datetime

with open('header.md', 'r', encoding='utf-8') as header_file:
    header_content = header_file.read()

with open('internship_listings.json', 'r', encoding='utf-8') as file:
    listings = json.load(file)


markdown_content = header_content + "\n\n# Internship Listings for Summer 2024\n\n"
markdown_content += "| Company | Role | Location(s) | Apply/Link | Date Posted |\n"
markdown_content += "|---------|------|-------------|------------|-------------|\n"

sorted_listings = sorted(listings, key=lambda x: x.get('date_posted', 0), reverse=True)

for listing in listings:
    company_name = listing.get('Company', 'N/A')
    role = listing.get('Role', 'N/A')
    locations = listing.get('Location(s)', 'N/A')
    date_posted = listing.get('Date Posted', 'N/A') 
    apply_url = listing.get('Apply', '')
    link_button = (f'<a href="{apply_url}" target="_blank"><img src="data/images/applybutton.png" alt="Apply Button" style="width:80px;"></a>'
                    f'<a href="https://www.interninsider.me/subscribe?utm_source=githubposting" target="_blank"><img src="data/images/interninsidersmall.png" alt="Intern Insider" style="width:40px;"></a>'
                    f'<a href="https://www.ribbon.ai/install" target="_blank"><img src="data/images/ribbonsmall.png" alt="Ribbon" style="width:40px;"></a>')

    markdown_content += f"| {company_name} | {role} | {locations} | {link_button} | {date_posted} |\n"


with open('../README.md', 'w', encoding='utf-8') as readme_file:
    readme_file.write(markdown_content)

print("README.md has been created successfully.")
