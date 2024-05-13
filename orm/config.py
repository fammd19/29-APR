import sqlite3

CONN = sqlite3.connect("students.db")
CURSOR = CONN.cursor()