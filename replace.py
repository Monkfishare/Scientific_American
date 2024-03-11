import datetime

recipe_file = "scientific_american.recipe"
edition_info_file = "published_date.txt"

auto_fetch_current_date = False  # Set to False if you want to manually set the edition year and month
                                # Set to True if you want to automatically fetch the edition year and month
manual_edition_year = "2023"
manual_edition_month = "06"  # Replace with the desired month (e.g., "01" for January, "12" for December)

with open(recipe_file, 'r', encoding='utf-8') as file:
    recipe_content = file.read()

if auto_fetch_current_date:
    current_date = datetime.date.today()
    Edition_Year = str(current_date.year)
    Edition_Month = str(current_date.month).zfill(2)
else:
    Edition_Year = manual_edition_year
    Edition_Month = manual_edition_month.zfill(2)

with open(edition_info_file, 'w', encoding='utf-8') as edition_file:
    edition_file.write(f"{Edition_Year}-{Edition_Month}")

modifications = {
    "w=800": "w=",
    'issue_url = \'https://www.scientificamerican.com\' + curr_issue_link.a["href"]': f'issue_url = \'https://www.scientificamerican.com/issue/sa/{Edition_Year}/{Edition_Month}-01/\''
}

modified_content = recipe_content
for original, replacement in modifications.items():
    modified_content = modified_content.replace(original, replacement)

with open('scientific_american.recipe', 'w', encoding='utf-8') as file:
    file.write(modified_content)
