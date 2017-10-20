# Project-S3

## Overview

### What is this app for?
This app is a gaming blog and its main purpose is to provide users with the latest news is computer gaming. 
 
### What does it do?
Users can browse the site to get the latest news in gaming, read the reviews, and also view the best rated games of each month. If a user chooses to sign up they will be given access to subscribe to a monthly newsletter and to purchase gaming guides from store.  

### How does it work
The app utilises the Django framework which is written on Python. This allows us to create very quickly a quality web application that works with both frontend and backend technologies. Paypal is also intergrated into this app allowing users to carry out smooth transactions through their Paypal accounts. This app uses db Sqlite3 which is the default Django ORM. 

## Features
Users can comment on the news posts through a Disqus account and can also share the latest news stories on their facebook, twitter, and Google plus pages. 
 
### Features Left to Implement
I will create a model and a view for Popular stories so they can be updated through admin, I will also look at ways of including a forum and a RSS feed. 

### Some of the tech used includes:
- [Bower](https://bower.io/)
  - **Bower** can manage components that contain HTML, CSS, JavaScript, fonts or even image files. Bower doesn’t 
    concatenate or minify code or do anything else - it just installs the right versions of the packages you need and
    their dependencies.
- [Python](https://www.python.org/)
  - **Python** is a hugely popular general-purpose, high-level programming language, used in web and 
    game development and scientific projects.
- [Django](https://www.djangoproject.com/)
    - We use **Django** to handle page routing, create additional apps, we also use it to make calls to the REST API and build custom directives.
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give our project a simple, responsive layout.
- [Jquery](https://jquery.com)
  - **Jquery** is a fast, small, and feature-rich JavaScript library. It makes things like 
    HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an
    easy-to-use API that works across a multitude of browsers.
- [Font-Awesome](http://fontawesome.io/)
  - **Font Awesome** is a full suite of pictographic icons that can be easily customised for websites.
- [Heroku](https://www.heroku.com/)
  - **Heroku** is a platform as a service (PaaS) that enables developers to build, run, and operate applications 
    entirely in the cloud.

## Testing
 
**Functionality:**
- Checked all the links worked on all pages.
- Tested forms on all pages.
- Validated HTML/CSS using W3C.
- Checked all queries were executing correctly from database.
- Made sure there was compatibility with different browser platforms. This project was
  tested on; Safari, Chrome, Firefox, Opera, and MS Edge.
- Tested responsiveness and compatibility on mobile devices, IOS and Android.

## What was kept
 
- Flask py file - This was kept and modified as needed.
- CSV file - Upload this file to my database unchanged. This file can 
  be downloaded from [donorschoose.org](http://www.donorschoose.org).
- graph.js - This file was modified in order to link to my flask py file.
- These files were kept and unchanged: Crossfilter.js, d3.js, dc.js, intro.js, jquery.min.js,
  keen.min.js, queue.js, dc.css, and introjs.cs.
  
## Deployment

- This project was uploaded and deployed on Heroku.