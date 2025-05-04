import sqlite3

conn = sqlite3.connect("tickets.db" )
c = conn.cursor()
# c.execute("""CREATE TABLE tickets (
#     ticketNumber INTEGER,
#     movieName TEXT,
#     visitDate TEXT,
#     uname TEXT
# )""")



print(c.fetchall())
conn.commit()
conn.close()