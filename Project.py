# playlist.py
# ------------------------
# This program reads a CSV file of songs
# and stores them in a SQLite database.
# It also keeps track of artist and album relationships.

import csv
import sqlite3

# Step 1: Connect to the database (creates music.db file)
conn = sqlite3.connect('music.db')
cursor = conn.cursor()

# Step 2: Create tables for Artist, Album, and Song
cursor.execute('''
CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY(artist_id) REFERENCES Artist(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    album_id INTEGER,
    duration TEXT,
    FOREIGN KEY(album_id) REFERENCES Album(id)
)
''')

cursor.execute("DELETE FROM Artist")
cursor.execute("DELETE FROM Album")
cursor.execute("DELETE FROM Song")
conn.commit()

# Step 3: Open and read the songs.csv file
with open("songs.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row['title']
        artist = row['artist']
        album = row['album']
        duration = row['duration']

        # Step 4: Insert artist if not already in database
        cursor.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))
        cursor.execute("SELECT id FROM Artist WHERE name = ?", (artist,))
        artist_id = cursor.fetchone()[0]

        # Step 5: Insert album if not already in database
        cursor.execute("INSERT OR IGNORE INTO Album (name, artist_id) VALUES (?, ?)", (album, artist_id))
        cursor.execute("SELECT id FROM Album WHERE name = ? AND artist_id = ?", (album, artist_id))
        album_id = cursor.fetchone()[0]

        # Step 6: Insert the song
        cursor.execute("INSERT INTO Song (title, album_id, duration) VALUES (?, ?, ?)", (title, album_id, duration))



print("All songs added successfully to music.db!\n")

# Print table header with fixed column widths
print(f"{'Song Title':<25} {'Album Name':<20} {'Artist Name':<20} {'Duration':<8}")
print("-" * 75)

# Fetch and print rows neatly
for row in cursor.execute('''
SELECT Song.title, Album.name, Artist.name, duration
FROM Song
JOIN Album ON Song.album_id = Album.id
JOIN Artist ON Album.artist_id = Artist.id
'''):
    title, album, artist, duration = row
    print(f"{title:<25} {album:<20} {artist:<20} {duration:<8}")


# Step 7: Save all changes
conn.commit()
conn.close()