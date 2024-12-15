class Contact:
    def __init__(self, name, phone_numbers=None, email_addresses=None):
        self.name = name
        self.phone_numbers = phone_numbers if phone_numbers is not None else []
        self.email_addresses = email_addresses if email_addresses is not None else []

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)

    def add_email_address(self, email_address):
        self.email_addresses.append(email_address)

    def get_contact_info(self):
        return {
            "name": self.name,
            "phone_numbers": self.phone_numbers,
            "email_addresses": self.email_addresses
        }