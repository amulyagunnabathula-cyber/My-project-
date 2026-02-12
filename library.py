
library = {
    "amul": "123",
    "appu": "456",
    "sanju": "789"
}

while True:
    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    
    if name in library:
        print(f"User exists: {name}, Roll: {library[name]}")
    else:
        library[name] = roll
        print(f"Added: {name}, Roll: {roll}")