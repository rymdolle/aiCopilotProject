def display_contacts(contacts):
    if not contacts:
        print("Inga kontakter att visa.")
        return
    for contact in contacts:
        print(f"Namn: {contact.name}")
        print(f"Telefonnummer: {', '.join(contact.phone_numbers)}")
        print(f"E-post: {', '.join(contact.emails)}")
        print("-" * 20)

def prompt_for_contact_info():
    name = input("Ange namn: ")
    phone_numbers = input("Ange telefonnummer (separera med kommatecken): ").split(',')
    emails = input("Ange e-postadresser (separera med kommatecken): ").split(',')
    return name.strip(), [num.strip() for num in phone_numbers], [email.strip() for email in emails]

def show_search_results(results):
    if not results:
        print("Inga sökresultat hittades.")
        return
    print("Sökresultat:")
    display_contacts(results)

def prompt_for_search():
    search_term = input("Ange namn eller telefonnummer att söka efter: ")
    return search_term.strip()