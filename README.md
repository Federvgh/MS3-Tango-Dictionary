# ms3-Tango-dictionary
For my Milestone 3 project I'm creating a dictionary of Tango slang that explains the terminology of this music
and gives some examples with songs to better understand it.

# Table of Contents

- [MS3-Tango-dictionary](#MS3-Tango-dictionary)
- [UX](#ux)
  * [General](#general)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)


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
<details>
<summary><strong>User stories: editor</strong></summary>
<br>
<h3>Editors have all the same access as the visitors and registered users</h3>
<ol>
<li>As an editor I want to edit the words i submitted</li>
<p>When any logged in user submits a word, it must fist be approved by an editor before it is published to the main dictionary. The editor can approve words in the editor dashboard.</p>
<li>As an editor I want to reject a submitted word.</li>
<p>On the editor dashboard, editors can reject a submitted word by clicking on the "Reject" button if the word is not relevant to the dictionary.</p>
<li>As an editor I want to edit words</li>
<p>Editors can edit words before they are approved in the editor dashboard. Editors can also edit any word in the main dictionary by clicking "Edit" next to the word in the main dictionary or serach page</p>
<li>As an editor I want to delete words</li>
<p>If an editor thinks a word is no longer relevant, they can delete that word from the dictionary by either navigating to it in the main dictionary or by searching for the word and deleting it in the search page.</p>
</ol>
</details>
<br>
<details>
<summary><strong>User stories: Admin</strong></summary>
<br>
<h3>Administrators have all the rights and permissions of editors</h3>
<ol>
<li>As an administrator I want to control user types for all registerd users</li>
<p>Administrators have the right to change any registerd user between "user", "editor", "admin".</p>
<li>As an admin I don't want to edit my user type by mistake</li>
<p>An administrator cannot change their own user type.</p>
</ol>
</details>
<br>