import json
from datetime import datetime

try:
    with open("notes.json","r") as file:
        notes=json.load(file)
except:
   notes=[]

while True:
    print("Welcome to the note app! pick an option")
    print("1: Add a new note")
    print("2: Search note by day")
    print("3: view all notes")
    print("4: exit")

    try:
        choice=int(input("Enter a number: "))
    except ValueError:
        print("Invalid choice")
        continue


    if choice==1:
            user_note=input("Write a note: ")
            now=datetime.now().strftime("%d/%m/%Y")

            notes.append({
            "Note": user_note,
            "Date": now
            })
            with open("notes.json","w") as file:
                json.dump(notes, file)
            print("Note saved!")


    elif choice==2:
        search_date=input("Enter a date (dd/mm/yyyy): ")
        found = False
        for note in notes:
            if note['Date'] == search_date:
                print("Note found!")
                print(note["Note"])
                found=True
            if not found:
                print("Note not found")

    elif choice==3:
        for note in notes:
            print(note["Note"], "-", note["Date"])
    elif choice==4:
        break

    else:
        print("Not an option")
        continue
