########


import sqlite3
connect = sqlite3.connect('mydatabase.db')

cursor = connect.cursor()

input = input("Ma'lumotni kiriting: ")

cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT,
    age INTEGER
)
               
""")

cursor.execute("""
INSERT INTO shopping VALUES
('Javohir', 'Nematov', 15),
('Mashhurbek', 'Ergashev', 15)
               
""")

cursor.execute("SELECT * FROM shopping")

if input == 'malumot':
    print(cursor.fetchall())
elif input == '':
    print('malumot yoq biror narsa kiriting')
else:
    print("malumot mavjud emas")