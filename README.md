# ABZRECIPE

# Table Contents

# Introduction
ABZRECIPE is a user-friendly recipe platform designed to make your cooking experience enjoyable and hassle-free. With a vast collection of mouthwatering recipes, each offering a visual feast of images, detailed ingredient lists, and step-by-step instructions, you’ll find the perfect recipe for any occasion. The path to the heart is through the stomach, and with this website, the journey would be more delightful and accessible than ever. This recipe website is your passport to a world of culinary creativity, where you can explore, create, and savour delicious dishes from every corner of the globe.

# Project Goals
The primary goal of ABZRECIPE is to empower users by creating a comprehensive online culinary resource. We aim to foster a thriving community of passionate food lovers, and providing a platform where users can easily discover and save a collection of recipes, with the goal of making every visit to the website an inspiring and delightful culinary experience. 

# User Experience - UX

## User Goals
- Ability to register an account.
- Ability to log into the account.
- Ability to receive a notification of a successful account being registered.
- Ability to receive an email with a link to activate an account after registration.
- Ability to receive a notification of a successful login.
- Ability to access their account profile.
- Ability to update their profile.
- Ability to view recipes of dishes.
- Ability to save their favorite recipes.
- Ability to access their saved recipes for easy access.
- Ability to leave a comment under recipes.

## Website Owner Goals
- Provide ingredients and steps to various dishes.
- Allow users to access recipes that they saved.
- Allow users to leave a comment under recipes.
- Make the website user-friendly so that users are able to easily access it.
- Create a contact form that allows users to send any queries that they may have.
- Create a comment section under each recipe so that users can leave a comment which makes the website more engaging.
- Admin login: to manage CRUD functionality.

## Developer Goals
- The site should restrict users that don't have an account created from saving recipes, accessing profile page, and accessing the favourite page.
- Users should receive an email when their account is registered with a link in order to activate their account.
- Users should receie

# Agile Methodologies

# Features

## CRUD Functionality
- Create: users can create a comment under different recipes when logged in and can save their favorite recipes.
- Read: users can view their saved recipes in the favorite's page when logged in.
- Update: users can update their profile details when logged in.
- Delete: users can delete the comments that they made under recipes when logged in. 
- Admin CRUD functionality implementation done from the Django Admin dashboard.

## Authentication and Authorization
- Users can create an account on the register page.
- Users can receive a notification notifying them that their registration was successful.
- Users can receive an email with a link to activate their account.
- Users can log in from the login page.
- Users can receive a notification notifying them that their login was successful.
- Authorisation is required in order to update the profile page, save favorite recipes, view the saved recipes, and write a comment under the recipes.

1. Register Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8e8e9c6f-5b47-49d1-b873-4b30bfbac701)

2. Login Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/3799a49b-61bc-4553-9426-9c06fde6aeb1)
  
## Navigation
- The primary navigation is located in the header section and is present on all pages.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9346aa23-507b-4011-9f5a-dda1d980d13f)

## Search
- There is a search feature, but it has not been implemented yet. This will be a future implementation. With this feature, the user will be able to search for any dish without having to scroll through the recipe page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/d14e1501-e1c2-4923-b407-df632a6471d9)

## Home Page
- This page includes images and introductory messages that summarize the purpose of the website.
- In the first image, there's an image slideshow that includes a button that says 'Go To Recipes', and if user clicks on this button, it automatically takes them to the recipe page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8eb65926-82d0-42d7-9b3e-966f121a78be)

- Home page also includes 2 images of dishes alog with their names, and a button that says 'Read More'. If user clicks on this button, it will take them to the recipe page of that particular dish.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/61694321-0165-413f-b505-c8f20b68eaa6)

- Underneath the 2 images, there is a section named 'The Best Recipes'. This has 6 enticing images of some dishes.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/5299aeaa-7aa8-4a3d-9ff2-793262d616ca)
 
- There is also a feature titled 'Explore Deliciousness' which also includes a 'Discover More Recipes' button. If user clicks on this button, it will take user to the 'Recipes' page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/6ed1ab53-c0f5-4a85-8ab4-cb9dcd941f5b)

- After this, there is a feature that displays some dishes and the amount of comments submitted for them.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/fb90a7f4-59c4-45e9-a277-8568a0a041be)

- Just to make this website more appealing to the user, there is a quote displayed in a box and a cookbook offer. This was added to make the page look better.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/75843929-5f3d-4029-a474-e86465da5852)
  
- This page also displays a compilation of images of dishes, and if the user hovers over them, there will be an Instagram icon. If user clicks on the image, they will be taken to the Instagram page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/bf411619-5970-41a0-bf8b-b8ec50fec23d)

- This is what the website looks like if the user isn't registered or logged into the account:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/54c6fbaf-5422-44d1-be5f-ba30d6bf578d)

- This is what the website looks like when the user has logged into the account:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/2b44411b-aee1-44a5-9eeb-62ce914a7c40)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/52d1b45f-3dd2-45cd-8ace-208da2461fe7)

- This is when the user has logged out:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/51aa19a8-c1ad-4287-9072-045e0db39870)

## Register Page
- This page includes many fields that is required to be filled in by all users. These fields are: username, email address, password, and confirm password.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/217e9b43-be85-4b4a-a1dd-0ac0c409da49)

- User must fill in all the fields otherwise user won't be able to register.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/f92a7bad-4222-4492-a7f1-511f7ff91301)

- After the user has clicked the 'Register' button, they will be sent an email to activate their account via a link. Once they click on the link, they'll be logged in.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/aa72bcb5-5bf7-4d4d-8b62-9f000ab801c6)

## Login Page
- This page requires a username and password field.
- It also includes a 'Remember Me' feature with a box that a user can tick if they want their details to be remembered for easy access.
- It also includes a 'Login' and 'Register' button.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/368a8f33-5b57-4d50-b4dc-43b87aed4b52)

- User must fill in all the fields otherwise user won't be able to login.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/500d2f25-4299-4c66-a484-2dfd29efaa17)

- Once user has logged in, they are notified with a welcome message at the top of the page:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/1a809e47-72a7-4120-a7c2-01fc8b31412d)

## Profile Page
- This page includes details of the user: first name, last name, username, emaial, phone number, address, country.
- The username and email fields will be automatically filled in because to access the profile page, the user must be logged in.
- User can edit their details.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/0efab5a2-f923-4791-90a0-cecde91e80e6)

- The above image shows that the user's username is 'rafz', but the user can edit this username and will be notified if they do so.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8b484668-f1f4-48c2-85d0-8effb5360e70)

- The user can choose to add extra information if they like.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/28639070-c8a4-4be4-aa59-443f64316018)

- Since the user changed their username from 'rafz' to 'babz', when they want to login later, their previous username will not work, they will receive a notification of "Invalid credentials".

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/4f78e7ab-b166-46da-9191-921cf0ec4408)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/30e8737f-47c9-48f1-b1c7-1a2c11968e57)

- If they now use their new username 'babz', they will be logged in successfully.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/f2b29e91-5abb-4b7a-99dc-9ed9c05c343d)

## About Us Page
- This page is a reflection of the purpose and personality of the website.
- Includes a feature that shows the number of dishes on the website and the number of dishes in each category (breakfast, lunch, dinner, beverages, salads, soups, snacks, and desserts).
- Underneath these features is a 'Contact Us' button.
- If user clicks on this button, it will take them to the contact page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/febef813-d557-43f2-8ad4-e76410347c94)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/de566d73-015c-4823-82fb-3dff4d4cbca6)

## Contact Page
- This page includes the details necessary for the user to contact in case of any questions or assistance they may require.
- It includes a contact form where the user can input their name, email address, the subject of the email, and the actual message.
- There's a 'Send' button and if user clicks on it, it will allow them to submit the form.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/438f5800-e3f8-4f56-9927-c23a3eff5c56)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/7eb9242a-bfac-4341-813b-5a3bb5249364)

- Once the message has been sent, the user will be notified that their message has been sent.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/34f24aa1-72b3-4726-9de6-880a3dd18afd)

- They will also receive an email notification.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/41da74d5-cb41-4baf-8cda-481db549b631)

## Recipes Page
- This page includes a list of all the dishes on the website.
- It displays images, the titles, introductory messages, and a 'Read More' button for each dish.
- If the user clicks on the 'Read More' button, it will take the user to a separate page which is the 'Recipe' page for the particular dish. 
- The page also has the 'Categories' feature displayed on the right side of the page. The categories include these sections: 'All, Breakfast, Lunch, Dinner, Soups, Salads, Beverages, Snacks, and Desserts'.
- Just to make this website more appealing to the user, there is a quote displayed in a box and a newsletter that will be part of a future implementation. This was added to make the page look better.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/17ad862f-ed1a-4761-8336-3547e05ed112)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/d25f81e5-1cc6-47ad-8bf1-56c681514277)

## Recipe Page
- This page has the ingredients, steps, and a comment section that allows the user to leave a comment under the dish.
- For example, the 'Yam and Egg Sauce' dish has the title, the image, and the introduction, along with a button that says 'Read More'. If the user clicks on the button, it will take the user to a page that has the ingredients, steps, a comment section that allows the user to leave a comment under the recipe of the dish, and a favorite feature that allows the user to favorite the recipe. Once that is favorited, it will be saved to the 'Favorite Recipe' page.
- There is a feature that says 'Other Recipes' which includes some images of the other dishes.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/fa789733-2856-4353-848c-90d56ebe83d0)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/71b51fd8-9ded-4852-9ce5-516364984268)

- The above image shows that no comment has been submited, but once a user submits a comment, it will be displayed for everyone to see. User does not have to be logged in for them to leave a comment. For future implementation, user will have to be logged in to leave a comment.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/554d35c4-edf8-4c3f-8919-e78b4c6a42ba)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8521991b-e8d4-49b4-90d0-3023e8da84e7)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/722993f9-946a-43b8-a450-c53b251cd1c1)

- User can also delete their comments.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9efc05ca-1dc8-407f-806e-057de723c986)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/2ee1eeae-d204-48d7-8dce-ae51605d8a04)

## Favorites Page
- This page includes all the dishes that the user has favorited.This is to make it easier for the user to access in the future without having to scroll through a number of dishes. Contributes to the purpose of making it a user-friendly website.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/073f97df-f677-4817-a2b5-368ff9255c71)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/2161f6c2-a16e-4feb-a140-61b88d516529)

- User can favorite a dish. Unfavorited shows a yellow heart. Favorited dish shows a purple heart.

- Unfavorited

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/f27ce44c-ed9c-452f-b18d-23917c6652af)

- Favorited

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/2f098c74-3bfc-443a-b1db-705650219f1f)

- User can unfavorite a dish

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/0c7b87d7-282f-4bb1-8b79-8f326118929f)

# Technologies Used
  
## Core Development Technologies
- Django: for full-stack framework in order to develop the app.
- JavaScript: for enhancement of overall functionality and user experience. For client-side interaction and validation.
- HTML: for building pages.
- CSS: for building pages.

## Libraries, Frameworks, and Packages
- Bootstrap: library of pre-designed HTML, CSS, and JavaScript components and tools for building responsive and visually appealing user interfaces.

## Python/Django Packages
- Gunicorn: provides HTTP server.
- psycopg2: PostgreSQL adapter for Python, allowing Django to interact with PostgreSQL databases.
- Pillow: for handling image-related tasks.
- Whitenoise: to serve static files.
- Django-heroku: simplifies process of deploying Django applications to Heroku.
- Django: simplifies web development.
- asgiref: ASGI implementation that Django uses for handling asynchronous operations.
- dj-database-url: allows for utilization of the DATABASE_URL environment variable to configure the Django application's database.
- python-dotenv: loads environment variables from a .env file, making it easy to manage configuration in development.
- setuptools: simplifies process of distributing and installing Python packages.
- six: for writing code that works across both Python 2 and 3.
- sqlparse: SQL parsing library used by Django for formatting SQL queries.
- validate-email: for validating email addresses in Python.

## Infrastructural Technologies
- Heroku: for deploying and hosting the application.
- Code Institute: for notes on project.
- GitHub and Git: collaborate seamlessly, track changes, and manage project's version control.
- Visual Studio Code: for writing code.
- PostgreSQL: for efficient data storage.
- Lighthouse Testing: ensures high performance, accessibility, and SEO standards for web application.
- CL PEP8 Validator: maintain consistent and readable Python code by adhering to PEP8 style guidelines.
- W3C CSS and HTML Validator: validate and ensure compliance with web standards for CSS and HTML code.
- Balsamiq: for wireframes: create wireframes for project's user interface.

# Testing

## Automatic Testing

## Manual Testing

## General Testing

# Credits
- ChatGPT: used this for getting the recipes for the dishes.





