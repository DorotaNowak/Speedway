import sqlite3
con = sqlite3.connect(r'C:\Users\Karol\PycharmProjects\Speedway\db2.sqlite3')
cursor = con.cursor()
cursor.execute("select * from fantasy_league_player3")
print(cursor.fetchall())