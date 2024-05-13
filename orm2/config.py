import sqlite3

CONN = sqlite3.connect("books.db")
CONN.execute("PRAGMA foreign_keys = on") #for the entire database connection
CURSOR = CONN.cursor()