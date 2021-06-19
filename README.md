# ms3-Tango-dictionary
For my Milestone 3 project I'm creating a dictionary of Tango slang that explains the terminology of this music
and gives some examples with songs to better understand it.

# Table of Contents

- [MS3-Tango-dictionary](#MS3-Tango-dictionary)
- [UX](#ux)
  * [General](#general)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)
  * [Features](#features)
  * [Dictionary](#dictionary)
  * [Navigation](#navigation)
  * [Footer](#footer)
  * [About](#about)
  * [Register](#register)
  * [Log In](#log-in)
  * [Search](#search)

- [CRUD Functionality](#crud---create--read--update-and-delete)

## General
The landing page of the website is the dictionary itself, this was done with the idea that people can search for words
even if they are not registered on the website. I have created and index by letter to be easier to search a specific words.
Once the user is registered and logged in they can add their own words, edit them or delete them if they choose to.
The "About" page explaines the purpose of the website. 

## User Stories

<details>
<summary><strong>User stories: visitor</strong></summary>
<br>
<ol>
<li>As a visitor the first thing i would like to see is the dictionary</li>
<p>Thats why the landing page is fully accessible to all visitors, no need to be registered.</p>
<li>As a visitor I want to search for specific words</li>
<p>A search bar is available on the main dictionary page to search all words.</p>
<li>As a visitor I want to easily navigate through the website</li>
<p>The main dictionary page has all teh words and you can scroll down to see all the words loaded.</p>
</ol>
</details>
<br>
<details>
<summary><strong>User stories: user</strong></summary>
<br>
<h3>Registerd users have the same access as the visitors</h3>
<ol>
<li>As a user I want to log in</li>
<p>The log in page is accessible in the navigation bar in the top right.</p>
<li>As a user I want to add a new word to the dictionary</li>
<p>After a user adds a word to the dictionary they will receive a message with the task succesfully completed,
then they can add another word o go back to the main screen to view their recently added word.</p>
<li>As a user I want to edit words</li>
<p>From the user dashboard, users are able to edit words which are pending approval.</p>
<li>As a user I want to log out</li>
<p>The user can log out of their account by going to the navigation bar in the top right.</p>
</ol>
</details>
<br>


# Features

## Dictionary
The landing page is the dictionary, you can see all the words that have been added since it was created, on the top you can see the search bar
and there is an index of letters to filter the search, below that you can find each word in a card separated by lines, with different categories, 
"type of word", "meaning" "used in this song".


## Navigation

The navbar at the top of the page has the page title and logo aligned to the left side and the links aligned to the right side. 
The links displayed on the navbar change depending wheter the user is logged in or not. If a visitor is not logged in, they will see a 
link for the about page, the dictionary page, the log page and the register page. 

If the user is logged in, they will not see the register and log in page links anymore, instead they will see 
"About" "Dictionary" "Profile" "Addd word" and "Logout" they will be able to add a new word and logout. 


## Footer
The footer is standard across all pages and shows the purpose for the website.


## Register

The register option gives the visitors the posiblity to register and contribuite adding words to the dictionary. 
The visitor needs to select a username and password. Form validation makes sure the username is not shorter than 5 characters or
empty fields. If the username is not available, it will receive a prompt message saying "Username already exists".

## About
The about page provides information about the dictionary and the reason why it was created.

## Log In
Users who have an account can login using their username and password. 
If a visitor does not have an account, they will below a message "New Here? Register Account" with a link to take them to the registration page
If the user enters their username and password they will be taken to their profile page.

## Search
On the dictionary page, users ot visitors can search for specific words located either in the word field or the meaning. 


# Features left to implement

- Pagination to avoid scrolling down 
- contact form
- an alert for the administrator when a word is submitted
- Option to delete a user by an admin and for users to delete their accounts. 
- Ability for a user to reset their password if they forget it. 
- automatically open new browser when click in on the link for the song

# CRUD

As part of the milestone project this application can perform CRUD operations.

## Create

### Add new words
All registered users are able to add new words to the dictionary. Each submission creates a new record in the database.

### Register new user
Anyone who does not have an account is able to register for an account. The register function creates a new record in the database for that user. 

## Read

### Display words from Mongo DB
All users are able to read from the database.
The application pulls the words collection from the database and displays them in the dictionary.

### Search
All users are able to search for words within the dictionary. It will look for the parameteres on the DB and display the results.

## Update & Delete

### Edit words
All users have the ability to delete or edit the words they submitted to the database, but only the ones they have submitted. The option to edit or
delete will be shown on each word the user has submitted previously, otherewise there wont be an option.


# Mongo DB Databse Structure
The database used for this project is MongoDB. The Databse contains three collections. 
- Categories 
- Users
- Words

### Categories
This collection contains the types of words. Each word can be either a Noun, Verb or a Phrase.

```
_id: ObjectID
category_name: String
```

### Users
The users collection stores all the data about registered users. The strucutre of the users collection is: 

```
_id: ObjectID
user_name: String
user_password: String 
``` 

The user_password string is hashed using the Werkzeug password hash function

### words
The words collection stores all the types words, their meaning, the category they are in, who created the entry and the link. The structure is as follows:

```
_id: ObjectID
category_name: String
Word: String
Meaning: String
Link: String
Created_by: String
```


### Frameworks, Libraries & Programs Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML) 
* [CSS](https://en.wikipedia.org/wiki/CSS) 
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 
* [Python](https://www.python.org/)

## Libraries

* [Materialize](https://materializecss.com/) 
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Jinja](https://www.palletsprojects.com/p/jinja/)
* [Pymongo](https://pypi.org/project/pymongo/)

## Hosting

* [Heroku](https://www.heroku.com/home)


1. Google Fonts

- Google Font was used to import the Poppins font through the entire website

2. Github

- Github was used to store the code pushed through Gitpod

3. Gitpod

- Gitpod was the Integrated Development Environment used to develop the Website.

4. Balsamiq

- Balsamiq was used to create the wireframes during the design process.

5.  Chrome DevOps Tools

- Chrome DevOps Tools was used to check elements and help debug issues with the site layout and try different CSS styles.

6. https://pixlr.com/x/

- For editing Images








