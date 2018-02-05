print("""Electronic Phone Book
======================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")
phonebook = {'Tolu': "4238001778", 'Tony': "4236778890", 'James': "4236778879"}
x = True
def set_entry():
            name = input("Enter a new name: ").capitalize()
            print ('what you entered', name)
            number = (input("Enter a new number: "))
            phonebook[name] = number
            print (name)
            return name

def delete_entry():
    name = input("Enter name to delete: ").capitalize()
    del phonebook[name]

while x:
    user_input = int(input("What do you want to do (1-5)? "))
    if user_input == 1 :
        print(phonebook)
        search_name = (input("Enter a name to find: ")).capitalize()
        print ('search name you entered', search_name)
        print(phonebook.get(search_name))
    elif user_input == 2 : 
        ret_name = set_entry()
        print("Entry stored for {}".format(ret_name))
    elif user_input == 3 :
        delete_entry()
        print(phonebook)
    elif user_input == 4 :
        for names, numbers in phonebook.items():
            print(names + ": " + numbers)
    elif user_input == 5: 
        print("Goodbye")
        exit
        x = False