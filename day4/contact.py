contacts = {
    "Rahul": "9876543210",
    "Sneha": "9123456789",
    "Amit": "9988776655",
    "Priya": "9012345678",
    "Karan": "8899776655"
}

contacts["Rahul"] = "9999999999"
contacts["Sneha"] = "9111111111"

existing_contact = contacts.get("Amit", "Contact not found")
missing_contact = contacts.get("Vikram", "Contact not found")

print("Safe Lookups:")
print("Amit:", existing_contact)
print("Vikram:", missing_contact)

print("\nContact List:")

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
