from bs4 import BeautifulSoup
import requests
import sqlite3

path = r'C:\Users\Karol\PycharmProjects\Speedway\db2.sqlite3'

sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()

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
        data = str(data[0:10]).replace('.', '-')
        date = data[6] + data[7] + data[8] + data[9] + '-' + data[3] + data[4] + '-' + data[0] + data[1]
        data = (runda, i, home_shortcut, away_shortcut, home_score, away_score, data)

        soup = BeautifulSoup(stats, features="lxml")
        tr = soup.findAll('table')[0].findAll('tr')
        for t in tr:
            res = t.findAll("td", {"class": "match__header__points__sum"})
            res2 = t.findAll('span')
            if str(res[0].text)[1:] == '':
                points = 0
            else:
                points = int(str(res[0].text)[1:])
            tt = ((res2[0].text), (res2[1].text), points, runda, i, date, home_shortcut, away_shortcut, home_shortcut)
            cursor.execute('insert into indv_matches values (?,?,?,?,?,?,?,?,?)', tt)
            sqliteConnection.commit()

        tr = soup.findAll('table')[1].findAll('tr')
        for t in tr:
            res = t.findAll("td", {"class": "match__header__points__sum"})
            res2 = t.findAll('span')
            if str(res[0].text)[1:] == '':
                points = 0
            else:
                points = int(str(res[0].text)[1:])
            tt = ((res2[0].text), (res2[1].text), points, runda, i, date, home_shortcut, away_shortcut, away_shortcut)

            cursor.execute('insert into indv_matches values (?,?,?,?,?,?,?,?,?)', tt)
            sqliteConnection.commit()
        i = i + 1
    except:
        continue
