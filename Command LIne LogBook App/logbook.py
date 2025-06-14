from helper import format_entry

entry = input("Enter your log entry: ")
fotmatted = format_entry(entry) 

try:
    with open("logbook.txt", "a") as file:
        file.write(fotmatted+"\n")
        print("Your entry was saved to logbook.txt.")
except Exception as e:
    print("Error, could not write to file.")
    print("Details:"+ e)

try:
    with open("logbook.txt","r") as file:
        print(file.read())
except FileNotFoundError as e:
    print("And error has been found")
    print("Error: "+ e)