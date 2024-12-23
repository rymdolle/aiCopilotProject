# File: /kontaktbok-app/kontaktbok-app/src/main.py

import sqlite3
from controllers.contact_controller import ContactController

def initialize_database():
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone_numbers TEXT,
            email_addresses TEXT,
            contact_type TEXT NOT NULL
        )
    ''')
    connection.commit()
    return connection

def main():
    connection = initialize_database()
    contact_controller = ContactController(connection)
    
    while True:
        print("\n--- Kontaktbok ---")
        print("1. Lägg till kontakt")
        print("2. Sök kontakt")
        print("3. Avsluta")
        choice = input("Välj ett alternativ: ")

        if choice == '1':
            name = input("Ange namn: ")
            phone_numbers = input("Ange telefonnummer (separerade med kommatecken): ")
            emails = input("Ange e-postadresser (separerade med kommatecken): ")
            contact_type = input("Ange kontakttyp (privat/jobb): ")
            contact_controller.add_contact(name, phone_numbers, emails, contact_type)
        elif choice == '2':
            contact_controller.search_contact()
        elif choice == '3':
            break
        else:
            print("Ogiltigt val, försök igen.")

    connection.close()

if __name__ == "__main__":
    main()