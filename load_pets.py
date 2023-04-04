import sqlite3

if __name__ == "__main__":
    '''This script populates the person, pet, and person_pet tables in the "pets" database.
    The person_pet table is a junction table to connect the person and pet tables in many-to-many relationships.'''

    con = sqlite3.connect('pets.db')

    with con:

        cur = con.cursor()
#        cur.execute('CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)')
#        cur.execute('CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)')
#        cur.execute('CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER)')
        cur.execute("INSERT INTO person(first_name, last_name, age) VALUES ('James', 'Smith', 41)")
        cur.execute("INSERT INTO person(first_name, last_name, age) VALUES ('Diana', 'Greene', 23)")
        cur.execute("INSERT INTO person(first_name, last_name, age) VALUES ('Sara', 'White', 27)")
        cur.execute("INSERT INTO person(first_name, last_name, age) VALUES ('William', 'Gibson', 23)")
        cur.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Rusty', 'Dalmation', 4, 1)")
        cur.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Bella', 'Alaskan Malamute', 3, 0)")
        cur.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Max', 'Cocker Spaniel', 1, 0)")
        cur.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Rocky', 'Beagle', 7, 0)")
        cur.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Rufus', 'Cocker Spaniel', 1, 0)")
        cur.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Spot', 'Bloodhound', 2, 1)")
        cur.execute("INSERT INTO person_pet VALUES (1, 1)")
        cur.execute("INSERT INTO person_pet VALUES (1, 2)")
        cur.execute("INSERT INTO person_pet VALUES (2, 3)")
        cur.execute("INSERT INTO person_pet VALUES (2, 4)")
        cur.execute("INSERT INTO person_pet VALUES (3, 5)")
        cur.execute("INSERT INTO person_pet VALUES (4, 6)")



