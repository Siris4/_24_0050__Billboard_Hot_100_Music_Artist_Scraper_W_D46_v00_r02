import requests
from bs4 import BeautifulSoup

# CONSTANTS:
LIMIT_OF_MAXIMUM_SONGS_TO_DATA_SCRAPE = 5

user_date_input = input("Which year do you want to Time Travel to? Please type the date in this format: YYYY-MM-DD: ")
print(user_date_input)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date_input}/")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# Initialize list to hold artist names
artist_names_list_for_user_picked_date = []

# Use find_all to get all artist names on the page
# Adjusted class to match your artist block class names
artist_names = soup.find_all("span", class_="c-label", limit=LIMIT_OF_MAXIMUM_SONGS_TO_DATA_SCRAPE)

def contains_number(value):
    # Check if the given string contains any digit
    return any(char.isdigit() for char in value)

for artist_name in artist_names:
    artist_name_text = artist_name.getText(strip=True)
    if not contains_number(artist_name_text):
        artist_names_list_for_user_picked_date.append(artist_name_text)

# Print the list of artist names
print("Artist Names:")
for artist_name in artist_names_list_for_user_picked_date:
    print(artist_name)
