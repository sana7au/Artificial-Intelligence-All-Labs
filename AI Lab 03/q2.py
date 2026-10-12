contact = {"name": "Hamza", "phone": "0300-1234567", "city": "Islamabad"}

print(contact)

contact["email"] = "hamza@example.com"

print("\nAfter adding email:", contact)

contact["city"] = "Rawalpindi"

print("\nAfter modifying city:", contact["city"])

phone_value = contact.pop("phone")

print("\nRemoved phone:", phone_value)

print("\nCompany:", contact.get("company", "Freelancer"))

print("\nFinal contact details:")

for key, value in contact.items():
    print(key, "->", value)