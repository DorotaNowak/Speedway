import sqlite3
path=r'C:\Users\Karol\PycharmProjects\speedway_site\Speedway\db2.sqlite3'
sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()

from bs4 import BeautifulSoup
import requests
import urllib.request


htmlSource = requests.get('https://speedwayekstraliga.pl/statystyki/lista-klasyfikacyjna/?k=2&y=2019').text
soup = BeautifulSoup(htmlSource)
players=soup.find_all('tr')
for p in players:
    names_info=p.find_all("strong")
    if len(names_info)>1:
        name=names_info[0].text
        surname=names_info[1].text
        stats=p.find_all('td')
        team=stats[2].text
        avg=stats[9].text
        sqlite_insert_with_param = """INSERT INTO 'fantasy_league_player3'
                              ( 'first_name', 'last_name', 'team', 'nationality','price') 
                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = ( name, surname,team,'PL',avg)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
