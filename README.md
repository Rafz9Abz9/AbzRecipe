# ABZRECIPE

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/35ac0a6f-8721-4936-81fc-4592c81e8741)

[LINK TO LIVE SITE](https://abzrecipe-72c82cf99b18.herokuapp.com/)

# Table Contents
1. [Introduction](#introduction)
2. [Project Goals](#project-goals)
3. [User Experience](#user-experience)
4. [Agile Methodologies](#agile-methodologies)
5. [Features](#features)
6. [Technologies Used](#technologies-used)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

# Introduction
ABZRECIPE is a user-friendly recipe platform designed to make your cooking experience enjoyable and hassle-free. With a vast collection of mouthwatering recipes, each offering a visual feast of images, detailed ingredient lists, and step-by-step instructions, you’ll find the perfect recipe for any occasion. The path to the heart is through the stomach, and with this website, the journey would be more delightful and accessible than ever. This recipe website is your passport to a world of culinary creativity, where you can explore, create, and savour delicious dishes from every corner of the globe.

# Project Goals
The primary goal of ABZRECIPE is to empower users by creating a comprehensive online culinary resource. We aim to foster a thriving community of passionate food lovers, and providing a platform where users can easily discover and save a collection of recipes, with the goal of making every visit to the website an inspiring and delightful culinary experience. 

# User Experience 

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
- Ability to access their saved recipes in a separate page for easy access.
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
- Enable users to create accounts, log in, and log out securely.
- Goal: Allow users to access a diverse range of dishes easily.
- Provide users with the ability to edit their profiles.
- Allow users to save their favorite recipes for quick access.
- Enable users to post comments on recipes.
- Implement interactive features to engage users.
- Enhance account security through email verification.

# Agile Methodologies
- Implemented Agile methodology for development, emphasizing iterative progress and continuous enhancement.
- Managed project tasks and user stories using a GitHub Project board.
- Ensured a structured and organized workflow for effective project management.
- User stories contain tasks and acceptance criteria.
- Prioritized project elements into 'must haves,' 'should haves,' 'could haves,' and 'won't haves'.
- NOTE: I updated my user stories and amended the prioritization labels and acceptance criteria. 

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/02a6bf9a-9e62-4854-84f6-975fd37b4805)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/93e19b79-497a-460a-8a89-06b28707d85a)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/6a57bc21-da94-4e90-b50b-840eae5d7b70)

# Features

This is a video converted to GIF of the what the process of the website looks like:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/0f726267-afa9-48e8-8bbc-0f23a6386418)

This is the **Register** and **Login** process:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/44a61eaf-e3f6-44d5-a729-cbf85b9a6fb9)

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

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/d366223f-a1a4-4073-aaec-e212263cb303)

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

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/65a54c27-8abb-4e95-bb86-1b3345585d3d)

- Underneath the 2 images, there is a section named 'The Best Recipes'. This has 6 enticing images of some dishes.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/5417afbf-1870-4231-9006-d8d3e027a7e3)

- There is also a feature titled 'Explore Deliciousness' which also includes a 'Discover More Recipes' button. If user clicks on this button, it will take user to the 'Recipes' page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/6ed1ab53-c0f5-4a85-8ab4-cb9dcd941f5b)

- After this, there is a feature that displays some dishes and the amount of comments submitted for them.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/502b1d26-8610-492e-bd7c-812edee97868)

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

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/0e81fd88-7ba7-43f2-95db-bbbbb795eabf)

## Register Page
- This page includes many fields that is required to be filled in by all users. These fields are: username, email address, password, and confirm password.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/217e9b43-be85-4b4a-a1dd-0ac0c409da49)

- User must fill in all the fields otherwise user won't be able to register.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/f92a7bad-4222-4492-a7f1-511f7ff91301)

- After the user has clicked the 'Register' button, they will be sent an email to activate their account via a link. Once they click on the link, they'll be logged in.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/aa72bcb5-5bf7-4d4d-8b62-9f000ab801c6)

## Login Page
- This page consists of a username and password field.
- It also includes a 'Login' and 'Register' button.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/89996aeb-7b5b-4912-abb6-6b13c25da799)

- User must fill in all the fields otherwise user won't be able to login.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/87cb978f-7e1b-4415-90bb-deeff3e417de)

- Once user has logged in, they are notified with a welcome message at the top of the page:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/1a809e47-72a7-4120-a7c2-01fc8b31412d)

## Profile Page
- This page includes details of the user: first name, last name, username, email, phone number, address, country.
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

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/942df87c-8852-441e-8d45-0f1c3288a0ee)

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

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/47670331-4776-4f92-8d21-82dec7d93d87)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/fd9ca92d-7178-482c-91da-497219dcce53)

## Recipe Page
- This page has the ingredients, steps, and a comment section that allows the user to leave a comment under the dish.
- For example, the 'Yam and Egg Sauce' dish has the title, the image, and the introduction, along with a button that says 'Read More'. If the user clicks on the button, it will take the user to a page that has the ingredients, steps, a comment section that allows the user to leave a comment under the recipe of the dish, and a favorite feature that allows the user to favorite the recipe. Once that is favorited, it will be saved to the 'Favorite Recipe' page.
- There is a feature that says 'Other Recipes' which includes some images of the other dishes.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/55d5aaca-92ce-4d67-8574-73e0423e5d51)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/1515dcdf-93c8-4aad-abdd-2e99f3c20a55)

- The above image shows that no comment has been submited, but once a user submits a comment, it will be displayed for everyone to see. User does not have to be logged in for them to leave a comment. For future implementation, user will have to be logged in to leave a comment.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/554d35c4-edf8-4c3f-8919-e78b4c6a42ba)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8521991b-e8d4-49b4-90d0-3023e8da84e7)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/722993f9-946a-43b8-a450-c53b251cd1c1)

- User can also delete their comments.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9efc05ca-1dc8-407f-806e-057de723c986)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/2ee1eeae-d204-48d7-8dce-ae51605d8a04)

## Favorites Page
- This page includes all the dishes that the user has favorited.This is to make it easier for the user to access in the future without having to scroll through a number of dishes. Contributes to the purpose of making it a user-friendly website.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/a973e126-f2db-4dfc-a876-d5d4828ecbb6)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/6257fe55-9ff8-4732-a6ed-cb55e757b5f2)

- User can favorite a dish. Unfavorited shows a yellow heart. Favorited dish shows a purple heart.

- Unfavorited

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/49881bc4-e599-4e9a-acd1-8c8150ec9b1f)

- Favorited

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9a76ee46-a38b-465b-acef-6326957bbd5c)

- User can unfavorite a dish

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8c2a5023-9af9-4a55-9768-8968edfe29fb)

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
- Cloudinary: simplifies handling images and videos for web apps. 
- Lighthouse Testing: ensures high performance, accessibility, and SEO standards for web application.
- CL PEP8 Validator: maintain consistent and readable Python code by adhering to PEP8 style guidelines.
- W3C CSS and HTML Validator: validate and ensure compliance with web standards for CSS and HTML code.
- Balsamiq: for wireframes: create wireframes for project's user interface.

# Testing

## Code Validation

### W3C HTML Validation

<Details>

<Summary>Home Page</Summary>

1. Errors found:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9f0f61bc-c419-43a7-8ca5-7b89979d307b)

2. After fixing the errors:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/bd704225-404d-49e2-a139-79ca69c37154)  

</Details>

<Details>

<Summary>About Us Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/eea3b7ad-408d-45ef-8193-e0ef6b1c5b9d)
  
</Details>

<Details>

<Summary>Contact Us Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/7409c387-32f2-49fd-adb7-4eacf9cdc19c)

</Details>

<Details>

<Summary>Register Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/96df88d7-c6bf-4c49-a4cf-491c12307183)
  
</Details>

<Details>

<Summary>Login Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/b615d3fb-9709-4e3e-855c-db115a8ba515)
  
</Details>

<Details>

<Summary>Profile Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/a9cb41b1-f8ba-4069-9456-763a808cfa64)
 
</Details>

<Details>

<Summary>Favourites Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/d0750add-5274-4823-ae6a-fc40168ebccf)

</Details>

<Details>

<Summary>Recipes Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/aa6699a3-4136-4b94-ac69-bf7796eae465)
 
</Details>

<Details>

<Summary>Recipe Details Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/df6092fe-2f25-4135-b0d0-abff2d191bae)

</Details>

### W3C CSS Validation

<Details>

<Summary>CSS Validation</Summary>

1. Errors found:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/16fb4045-3d79-428f-86dc-7a1b0d69b3fc)

2. After fixing the errors:

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9405d7e4-59c6-4372-a3a8-b5bdf043d2d5)
  
</Details>

### JavaScript Validation
- JavaScript from Bootstrap file.
- I did test for these files: map-active.js and active.js.
- Map-active.js file showed no warnings.
- Active.js file showed a missing semicolon in one of the lines which was amended.

<Details>

<Summary>Map-active.js File</Summary>

  ![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/e8c3175c-45bf-476b-993a-49ce3c2e3192)

</Details>

<Details>

<Summary>Active.js File</Summary>

  ![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/bebcb757-fb81-4869-b315-6cd225c76c2b)

</Details>

### Python Validation

<Details>

<Summary>Python Results</Summary>

| APP        | FILE    | RESULT |
|------------|---------|--------|
| abzrecipe | settings | PASS   |
| abzrecipe | urls     | PASS   |
| core       | forms   | PASS   |
| core       | models  | PASS   |
| core       | utils   | PASS   |
| core       | views   | PASS   |
| recipe     | forms   | PASS   |
| recipe     | models  | PASS   |
| recipe     | urls    | PASS   |
| recipe     | views   | PASS   |
 
</Details>

### Lighthouse Testing

**Mobile View**

<Details>

<Summary>Home Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/694111b2-a4fc-408d-998d-56212d462d32)

</Details>

<Details>

<Summary>Recipe Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/5fce410e-c544-468c-b96b-649cbcb7425b)

</Details>


**Desktop View**

<Details>

<Summary>Home Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/bea8b593-54d3-4bed-b74b-dddf99f3905f)

</Details>

<Details>

<Summary>Recipe Page</Summary>

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/a9f4c03a-7582-4438-86c0-c9c559a341c8)

</Details>

## General Testing

### Home Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/65b19fc2-dc0f-45ba-923b-af50659cc163)

### About Us Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/903d7a8b-91f8-41ec-b3da-85e72caad3fa)

### Recipes Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8e3c9482-8e7b-47f3-b1c9-624410eec389)

### Contact Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/b45e83cf-a0a9-4d39-9ce8-22babe662787)

### Login Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/04739cf8-8fae-4c50-85d2-3d737b47b643)

### Register Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/c4ed0631-2d5b-406a-a460-027321d534dd)

### Favorite Recipe Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/3e7d4799-ecad-4560-9eb3-ad3cf6edd20d)

### Profile Page

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/5237e8d2-f1f5-4001-ab49-fe893606ace0)

## Manual Testing

<Details>

  <Summary>Account Registration Tests</Summary>

| Test                                | Result |
|-------------------------------------|--------|
| User can create an account         | Pass   |
| Verified User can log into account | Pass   |
| User can log out of account        | Pass   |
| User is notified of logging in     | Pass   |
| User is notified of logging out    | Pass   |
| User receives email verification   | Pass   |

</Details>

<Details>

  <Summary>User Navigation Tests</Summary>

| Test                                            | Result |
|-------------------------------------------------|--------|
| User can navigate to recipes                   | Pass   |
| User can access recipe details                 | Pass   |
| Logged In User can navigate to the profile section | Pass   |
| Logged In User can edit their profile information | Pass   |
| Logged In User can access favourites page      | Pass   |
| Logged In User can save recipes                | Pass   |
| User can leave a comment under recipes         | Pass   |
| User can access the contact page and form      | Pass   |
| All links on footer open to correct pages      | Pass   |
| All links on Heading Navigation open to correct option | Pass   |

</Details>

<Details>

  <Summary>Account Security Tests</Summary>

| Test                                                 | Result |
|------------------------------------------------------|--------|
| Unregistered user cannot access profile page         | Pass   |
| Registered user can access profile page              | Pass   |
| All users can access the contact form page          | Pass   |
| Unregistered user cannot save recipes               | Pass   |
| Registered user can save recipes                    | Pass   |
| All users can post a comment under recipes          | Pass   |
| All users can view comments posted by other users   | Pass   |

</Details>

<Details>

  <Summary>Profile Tests</Summary>

| Test                                                 | Result |
|------------------------------------------------------|--------|
| Unregistered user cannot access profile page         | Pass   |
| Registered user can access profile page              | Pass   |
| Registered user can see their details on the profile page | Pass   |
| Registered user can update their first name         | Pass   |
| Registered user can update their last name          | Pass   |
| Registered user can update their email              | Pass   |
| Registered user can update their username           | Pass   |
| Registered user can update their phone number       | Pass   |
| Registered user can update their address           | Pass   |
| Registered user can update country                 | Pass   |

</Details>

<Details>

  <Summary>Feature Testing</Summary>

  | WHO/WHAT            | FEATURE                                                         | RESULTS |
|---------------------|-----------------------------------------------------------------|---------|
| Registered User     | Can access profile page.                                        | PASS    |
| Registered User     | Can save a recipe.                                              | PASS    |
| Registered User     | Can access favourites page.                                     | PASS    |
| Unregistered User   | Can’t access profile page                                       | PASS    |
| Unregistered User   | Can’t save a recipe.                                            | PASS    |
| Unregistered User   | Can’t access favourites page.                                   | PASS    |
| All Users           | Can leave a comment under recipes.                              | PASS    |
| All Users           | Can access contact page.                                        | PASS    |
| All Users           | Can access the contact form and submit an enquiry.              | PASS    |
| All Users           | Can access the recipes pages.                                   | PASS    |
| All Users           | Receive confirmation on the screen when they update, add, or delete something on the website. For example, if registered user saves a recipe, they’ll receive a confirmation of the action being done on the screen. | PASS    |
| Confirmation Email | When account is created – user will receive an activation link. | PASS    |
| Confirmation Email | When user sends a message through the contact form, user will receive an email confirmation. | PASS    |
| Confirmation Email | When user comments under recipes, user will receive an email confirmation. | PASS    |

</Details>

## User Story Testing

<Details>

  <Summary>Features Implemented</Summary>

As a site user, I want to easily register for an account so that I can access my personal profile and saved recipes.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/61972767-77ca-4e84-8689-cbf98021bea0)

As a registered user I can log in or log out of my account so that I can have the ability to access my account when needed or log out for security purposes.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/c0ea50a9-26bf-4224-9195-e547627ba86a)

As a registered user, I can view and edit my account information such as name, email address, address, country, and phone, so that I can have control over my account.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/f3f6f41b-b14a-4e7e-b92c-eda7e1bfef09)

As a site user I can easily navigate and explore the home page which includes clear navigation links to different sections and visually appealing design elements so that it can enhance my overall experience and guide me to relevant areas of the website efficiently.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/c2f7d9d7-f127-4107-acbf-42bc3668d062)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/0e413798-f54b-4c55-80c4-44fcfec2b319)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/af2205b2-f87a-44f8-a41a-f96dbeab4468)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/7d95b444-a3d6-4e6b-8394-de9f3a6e0c91)

As a registered user, I want to have a favourites page so that I can save and easily access recipes I like.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/09e21d78-f87e-42c9-98e3-a4e475d4b054)

As a registered user, I can add recipes to my favourites so that I can easily access them later without having to search for them again.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/2ee1a1a9-ff79-4522-8eac-3a8cab19503a)

As a registered user, I can remove recipes from the list of saved recipes so that I can efficiently manage my recipe collection.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/dd3be8cb-1fdf-4328-8e58-29f9f12f82ab)

As a site user, I can browse the recipe page so that I can easily explore the diverse range of recipes available on the website.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/13a165e5-5bc3-48d7-b599-61639beb56db)

As a site user, I can view the recipe details page so that I can gather detailed information about a specific recipe.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/b0739461-5039-40c4-a07c-f2776839c370)

As a site user, I can view each recipe’s images, title, and brief description so that I can quickly assess the content and decide if the recipe aligns with my preferences.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8c4f91cb-7872-4f9c-99d9-c1a113eed470)

As a site user, I can view images of various dishes so that I can have a visual of what the dishes look like.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/fbdf6f43-15ee-4575-b48d-6e2e0e92fcf7)

As a site user, I can add a comment under recipes so that I can share my thoughts, experiences, or modifications related to the recipe with the community.	

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/7e27ccc3-a480-4a9c-afd6-58668534f509)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/056b03ed-6e6f-41ef-97a7-ddd7819caa4e)

As a site user, I can delete comments I posted under recipes so that I can maintain control over my contributions and ensure the accuracy and relevancy of the content displayed on the website.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/1753ec83-3ef2-44a4-83a3-177e8be6dbbd)

As a site user, I want to have a contact form so that I can submit my inquiries, questions, or feedback easily.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/9acbb7b4-93d0-4b73-a0fb-6144e13bd7f5)


| USER STORY                                                                                            | RESULTS |
|-------------------------------------------------------------------------------------------------------|---------|
| As an admin, I want to enforce validation for all information entered by users to ensure accuracy and completeness. | PASS    |
| As an admin, I want to configure an auto-response email system to provide users with confirmation of any submissions. | PASS    |
| As an admin, I can manage some productivities for the website so that I can create, read, update, and delete details. | PASS    |

</Details>

<Details>

  <Summary>Features NOT Implemented - Future Features</Summary>

| USER STORY                                                                       | RESULTS |
|----------------------------------------------------------------------------------|---------|
| As a site user I can have a live chat option so that I can get quick assistance while browsing. | N/A     |
| As a site user, I can search for specific recipes or content easily, so that I can quickly find relevant information and recipes matching my preferences. | N/A     |
| As a site user, I can subscribe to a newsletter, so that I can receive regular updates, news, and notifications about new recipes, features, and promotions on the website. | N/A     |

</Details>

# Deployment

## Local Deployment
1. Repository cloning performed by clicking the "Code" button.
2. Copy the URL.
3. Open your preferred IDE and open the terminal section.
4. Type "git clone" followed by the URL copied from earlier, and press enter.
5. Install the required dependencies by typing "pip install -r requirements.txt" in the terminal.
6. You will be required to set up the environment variables in the local environment.
7. Connect to your preferred database and run the migrations by typing in "python manage.py migrate" in the terminal.
8. Create a superuser by typing "python manage.py createsuperuser" in the terminal and following the prompts.
9. Run the app by typing in "python manage.py runserver".

## Heroku Deployment
1. Access the Heroku dashboard and initiate the creation of a new application.
2. Establish a connection between your GitHub repository and the newly created Heroku app.
3. Navigate to the Settings tab on Heroku and verify the inclusion of the Python Buildpack.
4. Set necessary environment variables within the Config Vars section, located in the Settings tab.
5. Proceed to the Deploy tab and activate automatic deployment from your GitHub repository.
6. Trigger the deployment process by selecting the "Deploy Branch" button.
7. After the deployment is complete, access the app by clicking the "Open App" button.

### Environment Variables
- If using a Postgres database:
1. DATABASE_URL - the URL for your Postgres database.
2. NAME - the name of your database.
3. USER - the username for your database.
4. PASSWORD - the password for your database.
5. HOST - the host for your database.
6. PORT - the port for your database.

- Django Settings:
1. SECRET_KEY - the secret key for your Django project.
2. DEBUG - set to True for development, False for production.

# Credits
- ChatGPT: used this for getting the recipes for the dishes.
- Favicon: to create favicon.
- Fontawesome
- Gyazo: used this to record website process so that I can show the various features and functionalities.
- Ezgif: used to convert video to GIF.





