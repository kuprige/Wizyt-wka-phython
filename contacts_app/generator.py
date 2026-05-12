from faker import Faker
from contacts_app.base_contact import BaseContact
from contacts_app.business_contact import BusinessContact


fake = Faker("pl_PL")

def create_contacts(contact_type, quantity):
    if contact_type not in ("private", "business"):
        raise ValueError("contact_type must be 'private' or 'business'")

    contacts = []


    for _ in range(quantity):
        first = fake.first_name()
        last = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()

        if contact_type == "business":
            position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()
            contact = BusinessContact(
                first, last, phone, email, position, company, business_phone
            )
        else:
            contact = BaseContact(first, last, phone, email)

        contacts.append(contact)

    return contacts
