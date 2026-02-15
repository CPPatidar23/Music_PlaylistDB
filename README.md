# Music_PlaylistDB
# 🎵 Music Playlist Database Management System

This project is a Python application that reads song data from a CSV file and stores it in a structured SQLite database. It organizes music information into relational tables for Artists, Albums, and Songs, ensuring proper data normalization and relationships.

The system automatically inserts records, avoids duplication, and displays the playlist in a formatted tabular structure.

---

## 🚀 Features

- Imports song data from CSV file
- Creates relational database automatically
- Maintains Artist → Album → Song relationships
- Prevents duplicate artist and album entries
- Stores song duration details
- Displays playlist in structured table format
- Uses SQL JOIN queries for data retrieval

---

## 🗄️ Database Structure

The database **music.db** contains three tables:

### Artist
- id (Primary Key)
- name (Unique)

### Album
- id (Primary Key)
- name
- artist_id (Foreign Key)

### Song
- id (Primary Key)
- title
- album_id (Foreign Key)
- duration

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Database:** SQLite  
- **Libraries:** sqlite3, csv  
- **Concepts:** File Handling, SQL Joins, Database Normalization

---

## ▶️ How It Works

1. Connects to SQLite database (`music.db`)
2. Creates required tables if not present
3. Reads song records from `songs.csv`
4. Inserts Artists and Albums (avoiding duplicates)
5. Stores Songs linked via foreign keys
6. Displays formatted playlist output

---

## 📊 Sample Output

```
Song Title               Album Name          Artist Name         Duration
---------------------------------------------------------------------------
Shape of You             Divide              Ed Sheeran          3:53
Blinding Lights          After Hours         The Weeknd          3:20
```

---

## 📁 Project Files

- `playlist.py` → Main Python script  
- `songs.csv` → Input dataset  
- `music.db` → Generated database file

---

## 🎯 Learning Outcomes

- Practical implementation of SQLite with Python  
- Understanding relational database design  
- Working with CSV datasets  
- Executing SQL JOIN operations  
- Data normalization concepts
