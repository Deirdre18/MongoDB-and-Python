import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "mydbtest1"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        #conn = pymongo.MongoClient(url)
        
        conn = pymongo.MongoClient("mongodb://root:trickORTREAT2019@ds163162.mlab.com:63162/mydbtest1")
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
#creating show_menu function. Printing each of our options (CRUD) - create, read, update and delete.
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option
    
#But before then, we want to create a little helper function, which is going to assist us with our find, edit, and delete functions later on. The reason for this is that this code is reusable. We don't want to keep writing it out each time. So above our add_record() function, let's define another one called get_record().   

#So at the moment, our little helper function doesn't do anything. We don't call it anywhere. We're going to do that in the next video when we add find, update and delete functionality to our project.
    
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
#try/except block.
    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database")
    #empty variable returned if document not found. 
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc    
    
#So this will prompt us to enter this information and store it in each of these variables.
def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

#building string and storing in dictionary. So as we can see, we're doing it exactly the same as we did before, but this time we're putting the variable names in. And we're also calling the lower() method on our first and our last name.
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob,
               'gender': gender, 'hair_colour': hair_colour, 'occupation':
               occupation, 'nationality': nationality}
    #putting in a try block.
    try:
        #inserting our dictionary.
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")
    
    
#In our final video, we're going to add find, update, and delete functionality to our app. So that will give us the full range of CRUD operations, Create, Read, Update, and Delete in our menu-driven app. So go ahead and add a new function after our add function. This one's going to be called find_record.

def find_record():
    doc = get_record()
    if doc:
        print("")
       # So we're calling the items method here to step through each individual value in our dictionary.
        for k, v in doc.items():
            #The first thing we want to check is if the key is not equal to ID. ID, if you remember, is that default key that is created by Mongo. We don't want that to be displayed. So if the key is not equal to ID, then let's print the key. We will put the capitalized method on it, so that we get the first letter capitalized. Plus a colon. And then plus the value again with the first letter capitalized. Remember that we stored our data in lowercase, so we want to capitalize it again, just to make it look nice.
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

def edit_record():
    ##Again, we are going to store the results of our get_record() function in doc. And we're going to check to see if there is something in the dictionary.              
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        #And this time, we're going to create an empty dictionary called update_doc, and we're going to add to that dictionary. We're going to build that as we go on to iterate through our keys and our values.
        #That dictionary will form the basis of what we're going to use and insert into the database. So we'll print another blank line. Again, it's the same thing. We're going to iterate through using k,v in doc.items. And yet again, we also want to filter out the ID field. We don't want to be editing that.
        for k, v in doc.items():
            if k != "_id":
               # And the reason that we're doing this is that we want the value to appear in these square brackets so that we can see what the current value of them is. So k is the key, and v is the value. We should get a prompt that contains both the key and what the value is currently set to.
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    
                    update_doc[k] = v
        #I'm going to have a try except block again. And we're going to call the coll.update_one() method. It's the current document that we want to update. We put the set keyword in there with the $ in front. And then the dictionary that we're going to pass in is our update_doc dictionary that we just created. Print a blank line. And then say that our document was updated.
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")
            
def delete_record():

    doc = get_record()

    if doc:
        print("")
        #Then, much as we did with our find() function, we're going to iterate through and print each of the values. And the reason we're going to do this is we want to be sure that we're deleting the right document. We don't just want to go ahead and delete it without asking and confirming.
        for k, v in doc.items():
            #So again, we'll filter out the ID. We'll capitalize our key. We'll have a colon separating the key and the value. We'll capitalize the first letter of our value as well. So now we've done that, we'll print a blank line.
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        #And this time, we're going to create another variable called confirmation. And that's going to store the results of an input statement. And our input is going to prompt us to say 'Is this the document you want to delete?'.
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")
        #So we're asking the user for confirmation that this is the document they actually want to delete. So we'll just move the screen up a bit. If confirmation.lower() == 'y', then we're going to try coll.remove. And we're going to remove the doc.
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Document not deleted")

                
        
#main loop funciton created.        
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
            #print("You have selected option 1")
        elif option == "2":
            #print("You have selected option 2")
            find_record()
        elif option == "3":
            #print("You have selected option 3")
            edit_record()
        elif option == "4":
            #print("You have selected option 4")
            delete_record()
        elif option == "5":
            conn.close()
            #breaks from the programme
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()

#We've learned how to create a MongoDB database in the cloud and how to add data to it using the mLab web frontend. We've also seen how to install Mongo's command-line tools and use them for the basic CRUD operations of creating, reading, updating, and deleting data. Finally, we saw how to talk to a MongoDB database using the pymongo library in Python and brought all of that together in our walkthrough project at the end of this module. In future lessons, we're going to look at how to get this displaying on your own website by integrating Python, pymongo, and the Flask mini framework.