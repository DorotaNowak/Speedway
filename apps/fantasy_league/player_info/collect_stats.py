import sqlite3
path=r'C:\Users\Karol\PycharmProjects\speedway_site\Speedway\db2.sqlite3'
conn = sqlite3.connect(path)
from bs4 import BeautifulSoup
import requests
import urllib.request

con = sqlite3.connect(path)
cursor = con.cursor()
cursor.execute("SELECT * FROM fantasy_league_player")

htmlSource = requests.get('https://speedwayekstraliga.pl/statystyki/lista-klasyfikacyjna/').text
soup = BeautifulSoup(htmlSource)
players=soup.find_all('tr')
for p in players:
    names_info=p.find_all("strong")
    if len(names_info)>1:
        name=names_info[0].text
        surname=names_info[1].text
        print(name)
        print(surname)
