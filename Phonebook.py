import pickle

def main() :
    # open stored list of data
    contacts = read_contact_file()
    # variable for use with reading menu options
    # note that it is set to display first
    menuoption = "d"

    # create a loop which will handle menu options.
    # display menu, get the answer from the user
    # done - add (a), edit (e), remove (r), display (d), or quit (q). 

    while menuoption != "Q":
        menuoption = menu()
        if menuoption.upper() == "A":
            add(contacts)
        elif menuoption.upper() == "E":
            edit(contacts)
        elif menuoption.upper() == "R":
            remove(contacts)
        elif menuoption.upper() == "D":
            display(contacts)
        elif menuoption.upper() == "Q":
            menuoption = "Q"


    #save the file before exiting
    write_contact_file(contacts)


def read_contact_file():
    contents = {}
    # load the file into the dictionary object
    with open('phonebook.dat', 'rb') as handle:
        data = handle.read()
    contents = pickle.loads(data)
    return contents

def write_contact_file(contacts) :
    # write the contents of the contacts dictionary object to the opened file
    file = open("phonebook.dat", "wb")
    pickle.dump(contacts, file)
    file.close()

def menu() :
    # Create a menu that displays options to Add, Edit, Display, Remove, or Quit the phone book

    # display the options

    print("Add (A), Edit (E), Display (D), Remove (R), Quit (Q)")

    # Get the user's input (A, E, D, R, Q) which will perform the correction operation. 

    run = True

    while run == True:
        menuoption = input("What would you like to select?: ")
        if (menuoption.upper() == "A" or menuoption.upper() == "E" or menuoption.upper() == "D" or menuoption.upper() == "R" or menuoption.upper() == "Q"):
            run = False



    # return a valid value to the main function
    return menuoption 


def add(contacts) :
    # This function get the current contacts dictionary object to allow the user to add a new record
    
    # ask the user for the person's name
    name = input("Who would you like to add?: ")
    # ask the user for the person's phone number/email
    number = input("What is their phone number or email?: ")
    # stores those values in the contact dictionary
    contacts[name] = (number)

    return 

def remove(contacts) :
    # ask for the contact to be removed
    removecontact = input("Which contact would you like removed?: ")
    #remove the contact
    for name in contacts:
        if removecontact == name:
            del contacts[removecontact]
            return
    print("That user doesn't exist")

    return 

def edit(contacts) :
    # ask for the contact to be edited
    editcontact = input("Which contact would you like to edit?: ")
    # get the value that it needs to be changed to
    # edit the contact
    for name in contacts:
        if editcontact == name:
            newusername = input("What is the users new name?: ")
            newphonenumber = input("What is the new phone number?: ")
            del contacts[editcontact]
            contacts[newusername] = (newphonenumber)
            return
    print("User doesn't exist you should add them")

    return 

def display(contacts) :
    for key in contacts:
        print(key + ":\t" + contacts[key])

if "__main__" :
    # call our main function
    main()