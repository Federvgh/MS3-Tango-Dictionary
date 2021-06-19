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
