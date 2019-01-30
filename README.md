# Introduction To Go Humongous With MongoDB

## What is it?

A highly scalable database server.

## What does it do?

Stores data in a non-relational format.

## How do you use it?

Using mLab - a cloud database provider and MongoDB Python libraries.

LESSON:

In this unit, we're going to look at MongoDB.
MongoDB is a versatile database server that you can use in your projects.
So what is MongoDB, and what makes it different from MySQL, which we've already looked at?
Well MongoDB is a document-based database.
It's also called a NoSQL, or non-relational, database.
Now, we looked at MySQL earlier, which requires data to be stored in a very structured form.
Each field in the table has a specific data type, string, integer, floating point, number, and so on.
And this format allows for data in various tables to be connected to form a relationship, hence the term relational database.
MongoDB is different.
It's useful for storing large amounts of unstructured data.
In fact, its name, MongoDB, comes from the fact that it's designed to store humongous amounts of data.
Using Mongo, data can easily be stored across multiple servers in the cloud.
It also uses a JSON-like format called BSON, which we're already familiar with.
MongoDB is great at storing data when no relationship is needed.
In a traditional SQL database, we'd have, for example, a products table.
And the product ID might be linked to an artist table and the invoicing table and so on.
In Mongo, we don't make those kind of relationships.
Data in Mongo is stored in a collection of documents with no rigid structure, which means that we can store large amounts of data without having to define what types they are in advance.
Now, it's important to be familiar with different types of database technology in order to be flexible and to choose the correct database system for our projects.
It's good to know Mongo, as well, because it's part of what's called the MEAN stack, which consists of MongoDB, ExpressJS, Angular, and NodeJS.
In this unit, we're going to look at using a cloud-based MongoDB provider and how to integrate this with Python.
So our learning outcomes for this unit include creating a MongoDB database in the cloud, using MongoDB command-line tools to manipulate data, connecting to MongoDB using Python, and then we're going to create a menu-driven database system.
End of transcript. Skip to the start.
   

# Create A MongoDB Database With MLab

## What is it?

A MongoDB database.

## What does it do?

A database that stores unstructured data.

## How do you use it?

You use mLab, which is a Database-as-a-Service, to create and host your Database in the cloud.

LESSON:

The first thing that we need to do, then, is to create our MongoDB database in the cloud.
Now remember that we said that we were going to be storing our Mongo database in the cloud.
And for this we're going to use mLab.
They're a hosted services provider, and we can get a free hosted MongoDB database with them which allows us up to 500 megabytes of data, plenty for our requirements.
So click on get started and let's sign up.
So we need an account name, an email address, and, finally, choose a username and then a password.
Accept and create our account.
Now when we do that, it will ask us to verify our email before we can go ahead.
So let's go ahead and do that.
I'm just going to open up my email here.
And, as you can see, when I go into my email, I have the verification.
And just click the link, then, in the verification email to complete.
So now that we've got that completed, we can create our first MongoDB database.
Now, unfortunately, this site is not very responsive, so we're going to have to just scroll across the screen here.
And when we do that, we can see we have a create new.
So click on that.
And we're going to choose Amazon Web Services because that's the free sandbox.
We don't want to be paying for our database for this.
So then click the continue button.
Then choose our region.
Choose the one closest to you.
For us, that's Ireland, we cannot get much closer than that.
And then provide a database name.
So call it mytestdb.
Confirm that all the details are correct.
Click Submit.
And this places an order with mLab for the database.
It'll take a few seconds for the database to be created.
And when it is, it'll appear on the front screen here.
As we can see, it's creating our database.
It takes just a few seconds, and now it's done.
We're using the sandbox plan, which is free.
So go ahead and click on the database.
And this brings us to our database screen.
We need to add a user first so that we can connect to our database.
So again, we'll scroll across and add database user.
And we're going to create a database user called root.
Give root a password and remember this because we're going to need it later.
And then click the Create button.
So as we can see now, we have our root user created under database users.
As we said in our introductory video, data in Mongo is stored in collections.
And we can think of a collection as being like a table in a SQL database but without the same rigid data structure.
So let's create a new collection.
We'll call it myFirstMDB.
We'll click on create.
And just notice, as well, at the top here, we have our MongoDB URL.
And so we'll come back to that when we start connecting to our database.
For now, as we can see, we have a couple of collections: the system one and the one we created.
So let's click on that.
At the moment, we've got no documents in there.
So let's go ahead and add a new document.
The documents in Mongo are stored in a format that's json-like.
So to create a document, we use the two curly brackets and provide key value pairs.
So let's create a database of people.
We will create a field called first.
The first name will be Kate.
And then we put a comma after it.
Then "last": "bush",
Let's get her date of birth,
And put that in as the 30th of July 1958.
Again, comma after each new field and record that we're adding.
Her gender is female.
Her hair color is brown.
So again, we supply all of this data, and we put it in key value pairs.
We surround both the field names and the values in quotes separated by a colon and then a comma at the end.
Let's just put her nationality in there as English.
And we don't need a comma because this is the last piece of data we're providing.
Now we have to put the field names in quotes here, but when we're actually importing data into Mongo later or working directly with the shell, we won't have to.
It's just for this particular interface here.
So click on create and go back.
And when we go back, we can see that we have all of our information here.
We've created one document.
Now Mongo adds the ID for us automatically, which is very handy.
And we've created our first document.
Now normally, we will be importing data or adding it programmatically, rather than doing it through this frontend.
And in our next video, we'll see how to interact with our new MongoDB database using the command-line.

# Create And Read Back Data

## What is it?

Running commands (insert, find and sort) from the command line to update your MongoDB Database.

## What does it do?

The insert command allows you to create new database entries. The find and sort commands allow you to query and read back existing database entries.

## How do you use it?

By including your database credentials and your Mongo method (insert, find, sort) in your command.

LESSON:

In our last video, we set up a MongoDB database on mLab.
Now that we've done that, we can use the command-line tools in order to manipulate the data.
So to begin with, create a blank Cloud9 workspace.
Now Cloud9 comes with Mongo support built-in, but, unfortunately for us, it's an old version, so we need to upgrade it to the newest version.
To do this, we need to remove the old version and install the new.
So let's go ahead and open a terminal window and type the following command.
And what this does is it downloads and runs a script, which will remove the old version of Mongo and install the very latest version, which, at the time of this video, was 3.4.10.
Now that takes quite a long time to complete, so thanks to the magic of video editing, we've cut out all of the text scrolling up the screen.
But when it's completed, you'll be returned to the command prompt like this.
Mongo comes with a shell called ,mongo.
So how do we use it to access our database?
Well, if we go to our mLab page and click on our database, we can see there that it says to connect using the mongo shell, use this command.
So copy that command and paste it into the terminal window.
So what we just need to do now is change dbuser and dbpassword to the username and password that we supplied when we created this database.
So we gave the username of root, and, for me, the password was r00tUser.
And when we press ENTER on that, we can see that we get a connection to our database.
To prove that we are connected, type show collections, and that will show all of the collections that the database has.
As you can see, we have myFirstMDB and a system one, which just contains the indexes.
So we want to use myFirstMDB as our primary collection.
Now to shorten our commands, we are going to assign this collection to a variable like this, coll = db.myFirstMDB:
And that returns the name showing that that's now been assigned to a variable.
Remember, as well, that we use semicolons on the end of MongoDB commands.
So let's look at inserting data.
To do this, we can type coll.insert.
Then provide the key value pairs, just as we did when we added it on the web frontend.
So we're going to add John Lennon to our persons database.
Notice this time as well, as we're typing, that we don't have to put quotes around the field names.
Now that was just for the web frontend.
But when we're adding data like this programmatically, then you don't have to provide quotes around the field names.
So we'll just add in all of the data.
Hair color brown.
Occupation, well, you could say singer, but he was a Beatle.
And nationality was English.
So again, we'll just close the curly bracket and close the other bracket.
And we can see there that we get a write result back that one record has been inserted.
Now we will also supply some data for you to paste in, rather than retyping it all.
So I'm going to do that.
This adds another few people to our database.
And as you can see, after each one, we get inserted : 1.
Let's just check to see that all of those have actually been inserted.
So to do that, we can use the find() method, coll.find().
And when we provide that without any arguments in the brackets, it returns all of the data.
We can see everything that we've added, including the first record that we added on the web frontend.
I'm going to start typing cls between each command.
Cls is just a command that is short for clear screen.
And it will just make it easier to read what's going on here, rather than have everything scroll up the screen.
You don't have to do this. I'm just doing it to make things easier to read.
So we can supply an argument to our find() method if we want to find specific data in the table.
So, for instance, here, we can use {gender: "f"}.
So it will return all of the records where gender is set to f, or female, in our database.
And as we can see, this returns four records.
Now try changing that to m and see what happens.
You can try that on your own installation there.
We can return data based on multiple criteria as well.
For example, if we wanted to return all of the records where we have the female gender set and the nationality of English, then, again, we just separate our search terms with a comma inside the same set of curly braces.
You have {gender: "f", nationality: 'english'});
And that just returns Kate Bush from our database.
We can also use the special or operator to select records where either criteria is met.
So for example, if we wanted to find all database entries with the female gender who are either Irish or American, then we would use this command.
So coll.find {gender: "f" $or
We place our or clause inside the square braces.
So again, we close the curly bracket here now, then we open a new one.
We've got nationality: 'american' or nationality: 'irish'.
The fiddly bit now is closing all of the braces in the correct order.
So square brace, then curly brace, then a regular bracket.
So as we can see, this returns Eve Ryan who is nationality Irish, we've got Martha who's nationality is Irish, and Rocky who's nationality is American.
And all of them have the female gender.
We can sort the returned data, too, using the sort() function.
We provide the argument of 1 to sort ascending or -1 to sort descending.
Now this is a complicated command.
I just press the up arrow here to get the command that we just typed back.
Take the semicolon off the end.
And what we're going to do now is find all females who are Irish or American and sort by their nationality ascending.
So as you can see there, we could put .sort nationality 1.
And now the nationality American comes first in our list.
Try changing the sort order to descending and see what happens.
In our next video, we're going to look at how to update and delete data now that we've added it and read it back.

# Update And Delete Data

## What is it?

Running commands (update and remove) from the command line to update your MongoDB Database.

## What does it do?

The update command allows you to update existing database entries. The remove command allows you to delete existing database entries.

## How do you use it?

By including your database credentials and your method (e.g. update, remove) in your command.

LESSON:

In our last video, we learned how to create and read information using the Mongo shell.
Now we're going to have a look at how to update and delete data.
So while you're still connected to the database and with our coll variable set as we did before, type coll.update.
And we're going to search for the nationality of Irish.
And we're going to use the set keyword, which is $set.
And we want to set the hair color to blue.
So let's do that and put the semicolon on the end.
We instantly see, then, that we get back that it matched one record, and it modified one record.
Let's just confirm that. Let's do a search for all of the people in our database who have the nationality of Irish.
So again, using coll.find, as we did before.
That's strange.
We have two records of Irish, but only one record has updated a hair color.
Why is this?
Well, this is because Mongo just updates the very first record that it finds.
If we wanted to update all of the records, then we have to use the multi option.
So let's try that again.
I'm just going to use the up arrow.
And to show that it works, and that it's not just finding the second record this time, I'm going to change the hair color from blue to purple.
So type purple in there, in our $set.
And then, after the two closing curly braces, we put a comma.
And then we provide the multi option, which we set to true.
We do that inside the curly braces again.
And as we can see, this time it's matched two, and it's modified two.
Let's just check that using coll.find({nationality: 'irish'}).
And as we can see, this time both of the records have been updated.
So that's updating a record.
How do we delete?
Well, we delete by using the remove() method.
So to delete from our database, let's just clear the screen here.
We use coll.remove.
And then we provide arguments similar to the find function.
So in this case, we're going to find first name Kate, last name Bush, and remove that from our database.
So press return.
And as we can see, again we get a result back that one record has been removed.
If you wanted to remove all of the records from the database, effectively emptying it, then you can provide the coll.remove command without any arguments.
But don't do that just yet.
We don't want that to happen because we're going to use this data elsewhere in our project.
So that covers how to create, read, update, and delete data from the Mongo console.
Now we're going to have a look at how to do that with Python programmatically.
