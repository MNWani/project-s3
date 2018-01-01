# Project-S3

## Overview

### What is this app for?
This app is a gaming blog and its main purpose is to provide users with the latest news is computer gaming.

### What does it do?
Users can browse the site to get the latest news in gaming, read the reviews, and also view the best rated games of each month. If a user chooses to sign up they will be given access to subscribe to a monthly newsletter and to purchase gaming guides from store.  

### How does it work
The app utilises the Django framework which is written on Python. This allows us to create very quickly a quality web application that works with both frontend and backend technologies. Paypal is also integrated into this app allowing users to carry out smooth transactions through their Paypal accounts. This app uses db Sqlite3 which is the default Django ORM.

## Features
Users can comment on the news posts through a Disqus account and can also share the latest news stories on their Facebook, Twitter, and Google plus pages. This app can be displayed on Large devices (large desktops, 1200px and up), Small devices (tablets, 768px and up), and Extra small devices (phones, less than 768px).

### Features Left to Implement
"Popular stories" will be updated so stories are displayed based on number of views.  

### Some of the tech used includes:
- [Pip](https://pip.pypa.io/en/stable/)
  - **pip** pip is a package management system used to install and manage software packages written in Python.
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
- [PayPal](https://developer.paypal.com/developer/accounts/)
  - **PayPal Sandbox** The PayPal Sandbox is a self-contained, virtual testing environment that mimics the live PayPal production environment. It provides a shielded space where you can initiate and watch your application process the requests you make to the PayPal APIs without touching any live PayPal accounts.
- [Whitenoise](http://whitenoise.evans.io/en/stable/)
  - **Whitenoise** With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS providers.)

## Testing

**Functionality:**
- Checked all the links worked on all pages.
- Tested forms on all pages.
- Validated HTML/CSS using W3C.
- Checked all queries were executing correctly from database.
- Made sure there was compatibility with different browser platforms. This project was
  tested on; Safari, Chrome, Firefox, Opera, and MS Edge.
- Tested responsiveness and compatibility on mobile devices, IOS and Android.
- Disqus commenting and sharing posts tested. 
- Paypal Sandbox transactions were checked.
- Created users to test user functionality.

## What was kept
Disqus integration was kept.
blogposts.html and postdetail.html along with corresponding models and views was kept and modified as needed.
paypal_cancel.html and paypal_return.html was kept and modified as needed.
SignUpForm, login.html, logout.html, and signup.html was kept and modified as needed.
PostTests was kept and unchanged.

## Deployment

- This project was uploaded and deployed on Heroku
