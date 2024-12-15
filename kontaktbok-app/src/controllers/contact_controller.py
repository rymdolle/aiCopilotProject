class ContactController:
    def __init__(self, connection):
        self.connection = connection

    def add_contact(self, name, phone_numbers, emails):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO contacts (name, phone_numbers, email_addresses)
            VALUES (?, ?, ?)
        ''', (name, phone_numbers, emails))
        self.connection.commit()
        print("Kontakt tillagd.")

    def search_contact(self):
        name = input("Ange namn att söka efter: ")
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM contacts WHERE name LIKE ?
        ''', ('%' + name + '%',))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"ID: {row[0]}, Namn: {row[1]}, Telefonnummer: {row[2]}, E-postadresser: {row[3]}")
        else:
            print("Inga kontakter hittades.")

    def delete_contact(self, contact_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM contacts WHERE id = ?
        ''', (contact_id,))
        self.connection.commit()
        print("Kontakt raderad.")