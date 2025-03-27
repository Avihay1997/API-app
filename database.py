import sqlite3

def create_db():
    conn = sqlite3.connect('parts.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS parts (
                        id INTEGER PRIMARY KEY, 
                        name TEXT,
                        category TEXT,
                        price REAL)''')
    conn.commit()
    conn.close()

def insert_part(part):
    conn = sqlite3.connect('parts.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO parts (name, category, price) 
                      VALUES (?, ?, ?)''', (part['name'], part['category'], part['price']))
    conn.commit()
    conn.close()

def search_parts(query):
    conn = sqlite3.connect('parts.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM parts WHERE name LIKE ?''', ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

