contacts = {
    "Rahul": "9876543210",
    "Sneha": "9123456789",
    "Amit": "9988776655"
}

contacts["Priya"] = "9012345678"
contacts["Rahul"] = "9999999999"

existing_contact = contacts.get("Sneha", "Contact not found")
missing_contact = contacts.get("Vikram", "Contact not found")

print("Safe Lookups:")
print("Sneha:", existing_contact)
print("Vikram:", missing_contact)

print("\nContact List:")

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
