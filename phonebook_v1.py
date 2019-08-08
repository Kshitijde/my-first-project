#make a phonebook.name and a number every man comes and gives u.dictionary format.program :add a contact,like previous do u wanna add anohter contact input as name and number
from json import loads,dumps
response=0
f=open("phonebook.txt","r")
content=f.read()
phonebook=loads(content)
while True:
    response=int(input(print("press 1 to enter a new entry and press 2 to stop and see your phonebook")))
    if response==2:
        break
    key=input(print("enter your name"))
    value=input(print("enter your number"))
    if key in phonebook.keys():
        if value in phonebook[key]:
            print("contact already exists")
        else:
            phonebook[key].append(value)
    else:
        phonebook[key]=[]
        phonebook[key].append(value)
f.close()
f=open("phonebook.txt","r+")
f.write(dumps(phonebook))
search=int(input("if u want to search a contact,press 3"))
if search==3:
    name=input("enter the name of your entry")
    if name in phonebook.keys():
        print(phonebook[name])
    else:
        print("contact does not exist.")

