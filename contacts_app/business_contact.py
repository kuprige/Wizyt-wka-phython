from contacts_app.base_contact import BaseContact

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer służbowy {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")
