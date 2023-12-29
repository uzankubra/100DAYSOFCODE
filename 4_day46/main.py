from bs4 import BeautifulSoup
import requests

year_answer=input("Enter the year you would like to?: (Type in this format(YYY-MM-DD))")

response = requests.get("https://www.billboard.com/charts/hot-100/" + year_answer)


soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]