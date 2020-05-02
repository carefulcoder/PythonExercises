customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified" : True
}
print(customer["name"])
print(customer.get("birthdate", "Jan 1 1987"))

# exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)