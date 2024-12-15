class ContactController:
    def __init__(self, connection):
        self.connection = connection

    def add_contact(self, name, phone_numbers, emails, contact_type):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO contacts (name, phone_numbers, email_addresses, contact_type)
            VALUES (?, ?, ?, ?)
        ''', (name, phone_numbers, emails, contact_type))
        self.connection.commit()
        print("Kontakt tillagd.")

    def search_contact(self):
        search_term = input("Ange namn eller telefonnummer att söka efter: ")
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM contacts
            WHERE name LIKE ? OR phone_numbers LIKE ?
        ''', ('%' + search_term + '%', '%' + search_term + '%'))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"ID: {row[0]}, Namn: {row[1]}, Telefonnummer: {row[2]}, E-postadresser: {row[3]}, Typ: {row[4]}")
        else:
            print("Inga kontakter hittades.")

    def delete_contact(self, contact_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM contacts WHERE id = ?
        ''', (contact_id,))
        self.connection.commit()
        print("Kontakt raderad.")