from contacts_app.generator import create_contacts

# 3 prywatne wizytówki
private_cards = create_contacts("private", 3)

# 3 służbowe wizytówki
business_cards = create_contacts("business", 3)

print("\n--- Prywatne kontakty ---")
for card in private_cards:
    print(card.first_name, card.last_name, "-", card.label_length)
    card.contact()

print("\n--- Służbowe kontakty ---")
for card in business_cards:
    print(card.first_name, card.last_name, "-", card.label_length)
    card.contact()
