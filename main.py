import sqlite3
from datetime import datetime

conn = sqlite3.connect('post.sqlite3')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT,
                contact_name TEXT,
                address TEXT,
                city TEXT,
                postal_code INTEGER,
                country TEXT
               )
''')

conn.commit()

def load_posts(customer_name,contact_name,address,city,postal_code,country):
    cursor.execute('''
                INSERT INTO posts(customer_name,contact_name,address,city,postal_code,country)
                VALUES (?,?,?,?,?,?)
                   ''',(customer_name,contact_name,address,city,postal_code,country))
    conn.commit()

def fetch_post_by_name(country):
    cursor.execute('''
                SELECT * FROM posts WHERE country=?
                ''',(country,))
    posts = cursor.fetchone()
    return posts

while True:
    sample_name = input('Enter the customer_name: ')
    sample_contact = input('Enter the contact_name: ')
    sample_address = input('Enter the your address: ')
    sample_city = input('Enter the your city name: ')
    sample_code = int(input('Enter the your country postal_code: '))
    sample_country = input('Enter the country: ')
    choice = input('Again Do you have new info yes/no ').lower()
    load_posts(sample_name,sample_contact,sample_address,sample_city,sample_code,sample_country)
    fetch_post = fetch_post_by_name(sample_country)
    if choice == 'no':
        print('Okay. Your data has been saved successfully')
        break
    elif choice == 'yes':
        if fetch_post:
            print('Saved info')
            print('customer_name',fetch_post[1])
            print('contact_name',fetch_post[2])
            print('address',fetch_post[3])
            print('city',fetch_post[4])
            print('postal_code',fetch_post[5])
            print('country',fetch_post[6])
        else:
            print('Post Error')
conn.close()    