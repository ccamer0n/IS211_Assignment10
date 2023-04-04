import sqlite3

if __name__ == "__main__":
    '''This script takes an ID number as input and outputs information about pet owners and their pets.'''

    id_num = input("Please enter an ID number (enter '-1' to exit): ")
    con = None
    while id_num != '-1':
        try:
            con = sqlite3.connect('pets.db')

            cur = con.cursor()
            cur.execute('''SELECT person.first_name, person.last_name, person.age, pet.name, pet.breed, pet.age, pet.dead
                        FROM person
                        INNER JOIN person_pet ON person.id = person_pet.person_id
                        INNER JOIN pet ON person_pet.pet_id = pet.id
                        WHERE person.id=:id''', {"id": id_num})
            row = cur.fetchone()
            alive = row[6]
            print(f"This ID belongs to {row[0]} {row[1]}, age {row[2]}.")
            if alive == True:
                  print(f"{row[0]} {row[1]} owns {row[3]}, a {row[4]} that is {row[5]} years old.")
            else:
                  print(f"{row[0]} {row[1]} owned {row[3]}, a {row[4]} that was {row[5]} years old.")
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                alive = row[6]
                if alive == True:
                    print(f"{row[0]} {row[1]} owns {row[3]}, a {row[4]} that is {row[5]} years old.")
                else:
                    print(f"{row[0]} {row[1]} owned {row[3]}, a {row[4]} that was {row[5]} years old.")

            id_num = input("Please enter an ID number (enter '-1' to exit): ")

        except Exception as err:
            print(err)
            id_num = input("Please enter an ID number (enter '-1' to exit): ")

        finally:
            if con:
                con.close()