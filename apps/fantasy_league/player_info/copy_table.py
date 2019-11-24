import sqlite3
path=r'C:\Users\Dorota Nowak\Desktop\Speedway\db2.sqlite3'
sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()
sqlite_insert_with_param = """INSERT INTO fantasy_league_player SELECT * FROM fantasy_league_player3;"""
cursor.execute(sqlite_insert_with_param,)
sqliteConnection.commit()
