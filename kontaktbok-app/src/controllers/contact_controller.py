class ContactController:
    def __init__(self, contact_model):
        self.contact_model = contact_model

    def add_contact(self, name, phone_numbers, emails):
        contact = self.contact_model(name=name, phone_numbers=phone_numbers, emails=emails)
        contact.save()

    def search_contact(self, query):
        return self.contact_model.search(query)

    def delete_contact(self, contact_id):
        contact = self.contact_model.get_by_id(contact_id)
        if contact:
            contact.delete()