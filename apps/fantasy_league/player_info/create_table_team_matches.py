import sqlite3
from bs4 import BeautifulSoup
import requests
import urllib.request

path = r'C:\Users\Karol\PycharmProjects\Speedway\db2.sqlite3'
sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()
'''
cursor.execute("""create table team_matches (
                  round varchar(30) ,
                  game_number integer,
                  home varchar(30),
                  away varchar(30),
                  h_score integer,
                  a_score integer ,
                  date_of_match date )
                  
                  
""")
'''
i = 1
for match_number in range(1076, 1200):
    try:
        stats = requests.get('https://speedwayekstraliga.pl/terminarz-i-wyniki/mecz/' + str(match_number) + '/').text
        soup = BeautifulSoup(stats, features="lxml")
        mydivs = soup.findAll("div", {"class": "match__header__score"})
        home_score = int(mydivs[0].text)
        away_score = int(mydivs[1].text)
        mydivs = soup.findAll("div", {"class": "match__header__shortcut"})
        home_shortcut = str(mydivs[0].text)[1:]
        away_shortcut = str(mydivs[1].text)[1:]
        mydivs = soup.findAll("div", {"class": "match__header__info"})
        res = [str.strip() for str in mydivs[0].text.splitlines()]
        runda = res[2]
        data = res[3]
        data=str(data[0:10]).replace('.','-')
        data=(runda, i, home_shortcut, away_shortcut, home_score, away_score, data)
        cursor.execute('insert into team_matches values (?,?,?,?,?,?,?)', data)
        sqliteConnection.commit()
        i = i + 1
    except:
        continue
