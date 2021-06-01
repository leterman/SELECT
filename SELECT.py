import sqlalchemy
import psycopg2
from sqlalchemy.engine import Inspector

db = ('postgresql://userok:12345@localhost:5432/bass')
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


sel = connection.execute("""SELECT album_name, year FROM albums
WHERE year =2018;
""").fetchmany(10)
print(sel)

cel = connection.execute("""SELECT track_name, track_length FROM tracks
ORDER BY track_length DESC;
""").fetchmany(1)

print(cel)

cel1 = connection.execute("""SELECT track_name, track_length FROM tracks
WHERE track_length >=210;
""").fetchmany(100)

print(cel1)

cel2 = connection.execute("""SELECT name, year FROM playlist
WHERE year >=2018 AND year <=2020;
""").fetchmany(100)

print(cel2)

cel3 = connection.execute("""SELECT name FROM artists
WHERE name NOT LIKE '%% %%';
""").fetchmany(10)
print(cel3)

cel4 = connection.execute("""SELECT track_name FROM tracks
WHERE track_name LIKE '%%My%%';
""").fetchmany(10)
print(cel4)