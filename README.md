

[![Build Status](https://travis-ci.com/TapiwaDivine/Unicorn-Attractor.svg?branch=master)](https://travis-ci.com/TapiwaDivine/Unicorn-Attractor)

# Unicorn Attractor 
This project is a Full-Stack project that has been build in Django  Framework 1.11.24, with databases being Sqlite3 in development and PostgresqL in production.
Unicorn-Attractor - a startup tech-company that offer Unicorn Attractor (CRM), webapps, websites, free bug fixes and more. 
This webapp allows users to request addition features to their app and report bug which will be fixed free of charge. Features and Issuse can be requested 
and immediately appear om the website for transparency and to help user associate if they want an addtional feaure or they have same bug. Users can also upvote feature or bug
at no cost as way of attracting users through interaction and also to clarity on the most import issue and features. I a user has the same issue raise their upvote/like will automatically yellow flag them for the admin say
i have this too. Th issues and features are closed only by the admin as users might forget to update and will lead other users feeling that the admins are not doing their work well.



## Content Table

1. [UX](#UX)
2. [Features](#Features)
    +   1. [Existing Features](#existing-features)
    +   2. [Features Left to Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
    +   1. [Content](#content)
    +   2. [Media](#media)
    +   3. [Acknowledgements](#acknowledgements)


## UX
1. Landing on the page the user is directed to the CRM download for which will need additional features and which we feel might need to be added a monthly subscriptions fee as a additional project idea.
 - On the Home Page i wanted to persuade the user that they can get our CRM and have a summary of what we do in the SERVICES section. Also I decided to put a view reviews which would the user can be convince the user to establish a relationship with the company
 - Services page also seeks to solidify and connect users to the issue submition and feature request buttons. the page also display maximum of 3 requsted features and seeing all feature would be facilitated by the View All button.
 - Each Feature or Bug a boostrap accordion rendering it with more deatils viewed onclick and a future detail viewed on view more were.
 - The user will be able to comment or like once they have signed up or logged on, all interactions by users are done we they are logged on. This would help admin to track all the interactions. So on signup User Profile is also created
2. Colour: The theme colour of this project is Blue, Black, & yellow.While images for the hero in 3pages and page backgrounds. The footer of this app is for branding boosting purpose and its something different that i want to try out 
3. Pages : This web app has about 18 pages which can be openned through either navbar, links and buttons
4. Mock up: I did a mock up of the front end of this website using figma [figma.com](https://www.figma.com/file/gFrdNHRfuekcYOctZTP3dt0O/Untitled?node-id=0%3A1) and my database planning was done using  [dbdiagram.com](https://dbdiagram.io/d/5d65c60eced98361d6ddf95e)

## Features 

### Existing Features

* Navbar:
    * The website navbar has a Company logo designed specifically for this project. The logo has a blue Unicorn with white and pink word
    * The navbar is responsive and returns a hamburger menu in mobile and tablets screens, while it displays fullscreen with in all screens

* Home Page:
    * Hero Image - I put an image that projects excitement and winning, to capitivate the user to download the company's app
    * Services Section provides a glimpse of a short advert in what the company is all about and will be come more detail as the user get to the services page

* Signup & Login :
    * The signup and login page provides forms for users to register 
    * these login page is key as user will not be able to interate with the website if they are not logged in so when user try to comment, like, make a purchase etc. without login they are redirect to login page

* Community Page
    * Community Page displays maximum of 3 bug on the page
    * Also a business hub for submitting issues, features, requesting website
    
* Contact Us Page
    * Has a form for users to contact the admins or the company via email and emailjs
    * The page offers every contact users might need from address, social media link, phone numbers, email addresses.

* Profile Page
    * The profile page will be aumomatically created when the user registers
    * The user will be able to edit and add more information to their profile and also add their profile pictures
    * The profile page also displays a dashboard for user to view the requested features and progress through a mini dashboard

* Cart Page & Checkout Page
    * Cart Page displays an item a user wishes to purchase, the price in total needed to be paid & the number of items selected
    * The cart page also displays a form for adjusting the items and number of items
    * Checkout Page display the payments form and user payment details
     
* Common feature

    * The View Feature and View Bug Details pages display similar features and to note an edit and delete buttons that display to the author only.
    * The footer is a banner meant for branding the new company as a reminder to the user about the company when they get to the bottom of each page.

### Features Left to Implement

- Features Left to Implement to implement include a user dashboard  that displays liked features or bugs
- Also Website dashboard that has graphs to display the work on features and bugs
- Pagination for rendering more features and bugs
- Search bar to cater for easy and dynamic navigation

## Technologies Used
1. In this project i used:
    * Python Django Framework
    * PostgresqL
    * Sqlite3
    * Jinja2
    * Bootstrap 4
    * Bootswatch
    * Django-forms 
    * AWS Cloud 9
    * AWS S3 
    * StripeJS
    * Heroku
    * Travis CI
    * CSS3
    * HTML5
    * GoogleFonts
    * Fontawesome
    * Javascript
    * EmailJs
    * sweetalertJS
    * figma
    * dbdiagrams


    
2. This project was styled with Bootstrap 4 , Fontawesome, Javascript and CSS3
3. I used [heroku](heroku.com) to serve the data with the heroku's postgresql
4. I also used [awss3](cloudinary.com) serve my static files
5. Figma was my mockup platform of choice it worked fantastic form me.

## Testing
* Automated testing with Django TestCase
    - Testing for views with login required decorator always failed so they have been removed from the test  available im the project
    
* All code were validated through:
    - [W3C Mark-up Validation Service](https://validator.w3.org/)
    - [W3C CSS Validation Service](http://www.css-validator.org/)
* Add Recipe And Edit Recipe forms
    - I tested both form and forms are functioning well and have a required element to make sure that no field will be empty. At first the form was submitting  without any data
* Signup Form
    - When you click Signup page On navbar
    - Submit an empty form ,error message that required fields appears.
    - Submit form with a registered email already and verify that a relevant error message appears.
    - Submit form with a taken username already and verify that a relevant error message appears.
    - Submit form with different passwords and verify that a relevant error message appears.
    - Submit the form with all inputs valid and verify you are redirected to the Profile page where a success message will appear.

* Login Form
    - When you click Login page On navbar
    - Submit an empty form ,error message that required fields appears.
    - Submit the form with an unregisterd username or email, a relevant error message appears.
    - Submit the form again with valid registered user credentials, you will be redirected to the homepage and a success message appears.

* Profile 
    - Click on the profile page in the navbar
    - A half populated form with details from sign up form and a default image will appear
    - Edit form allows user to add further details and add picture
    - Profile form cannot be posted empty because it return  the required fields error
    - profile cannot change to another user's email and it return the relevant error

* Bug Form & Features form
    * When you click a report bug or request issue button a form will appear
    * Submit an empty form the form will render a required fields error

    
* Mobile Responsive
    - This web-app is mostly responsive in most screens i have tested it on Iphone X, Huawei Psmart2019,Windows Chrome browser, edge browser and Opera browser

- Futher testing on this project was done manually using developer tools to test the website
- I also openned each page to check and see if there are any bug or frontend errors.

## Deployment
- This project was created in AWS cloud9 IDE environment to push code to github and heroku respectively
- [github](https://github.com/TapiwaDivine/Unicorn-Attractor)
- [heroku](http://uni-attractor.herokuapp.com/)

## Credits
- [YouTube](youtube.com)
    Channels
    - Pretty Printed
    - Learn with Ali Hossain
    - Traversy Media
    - Corey Schafer
    - Coding Entrepreneurs
    - Abhishek Verma
    - Max Goodridge

- Code Institute tutorials (the manin source of most of the i code i used in this project)    
- [Stack Overflow](https://stackoverflow.com/questions) (I got a lot of code that i implemented in this project from stackoverflow kudos to this platform)
- Miguel Grinberg [Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)(Contributed a lot to my understanding though if a flsk project)
- Tutors at code institute(Haley, Neil, Samatha, Tim, Xavier i must say everyone at Code Institute was Fantastic)
- My Mentor (Maranatha)
- Jinja2 Documentation
- [mdbootstrap](mdbootstrap.com)
- [Getboostrap](getboostrap.com)
- [sweetalertJS](https://sweetalert.js.org/guides/)


### Content
- getboostrap.com were i accessed code for all the bootstrap in this project
- Stack overflow were most of my solutions came from
- Code Institute most of the layout in the project were from the lessons source
- W3schools.com - helped with some of the CSS codei used in this project
- mdbootstrap - i used it to set up the base.html footer
- Corey Schafer - mostly his video on YouTube helped to set up pfrofile page and its functionality
- Abhishek Verma - following what i saw in this Youtuber got me getting votoes/likes in my database
- Pretty Printed, Traversy Media, tutors at code institute and  Maranatha all the mentioned helped me understand concepts that apply not only in python and django bbut other languages also.
- Coding Entrepreneurs I used some code from this YouTuber's Try Django tutorials
- Also the django tutorials but Max Goodridge on YouTube as well whose code i used also in some parts of my project
- There are also an assorted list of YouTube channels that i helped me get this project up

### Media

- Most pictures used were all downloaded from random google search and also Pixabay

### Acknowledgements
- I drew inspiration for this website from a cocktail of websites of web development companies and also from the sega website
- I would also wanted to acknowledge the work done by the forementioned at the credits section to whom the biggest percentage of the codein the project has been influenced from or brought understanding to the needs of this project
- Special mention to Video Tutorials, Code institute Tutors and my mentor, God Bless 
