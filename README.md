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
  
## Navigation
- The primary navigation is located in the header section and is present on all pages.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/b684d567-a0e1-4aa8-ab58-f038441adcd3)

## Home Page
- This page includes images and introductory messages that summarize the purpose of the website.
- In the first image, there's an image slideshow that includes a button that says 'Go To Recipes', and if user clicks on this button, it automatically takes them to the recipe page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/8eb65926-82d0-42d7-9b3e-966f121a78be)

- Home page also includes 2 images of dishes alog with their names, and a button that says 'Read More'. If user clicks on this button, it will take them to the recipe page of that particular dish.

- Underneath the 2 images, there is a section named 'The Best Recipes'. This has 6 enticing images of some dishes.
  
- There is also a feature titled 'Explore Deliciousness' which also includes a 'Discover More Recipes' button. If user clicks on this button, it will take user to the 'Recipes' page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/6ed1ab53-c0f5-4a85-8ab4-cb9dcd941f5b)

- After this, there is a feature that displays some dishes and the amount of comments submitted for them.
  
- Just to make this website more appealing to the user, there is a quote displayed in a box and a cookbook offer. This was added to make the page look better.
  
- This page also displays a compilation of images of dishes and if user hovers over them, there would be an instagram icon. If user clicks on the image, they will be taken to the instagram page.

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

- After the user has clicked the 'Register' button, the user will be sent an email to activate their account via a link. Once they click on the link, they'll be logged in,

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

## About Us Page
- This page is a reflection of the purpose and personality of the website.
- Includes a feature that shows the amount of dishes on the website, amount of dishes in each category (breakfast, lunch, dinner, beverages, salads, soups, snacks, and desserts).
- Underneath these features is a 'Contact Us' button.
- If user clicks on this button, it will take the user to the Contact page.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/f7f2998f-d936-406b-91b6-f561e1526faa)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/3f5b71c2-9edb-4e30-8ec4-5d4650a4067f)

## Contact Page
- This page includes the details necessary for the user to contact in case of any questions or assistance they may require.
- It includes a contact form where the user can input their name, email address, the subject of the email, and the actual message.
- There's a 'Send' button and if user clicks on it, it will allow them to submit the form.

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/438f5800-e3f8-4f56-9927-c23a3eff5c56)

![image](https://github.com/Rafz9Abz9/ABZRECIPE/assets/126483536/7eb9242a-bfac-4341-813b-5a3bb5249364)

## Recipes Page
- This page includes a list of all the dishes on the website.
- It displays images, the titles, introductory messages, and a 'Read More' button for each dish.
- If the user clicks on the 'Read More' button, it will take the user to a separate page which is the 'Recipe' page for the particular dish. 
- The page also has the 'Categories' feature displayed on the right side of the page. The categories include these sections: 'All, Breakfast, Lunch, Dinner, Soups, Salads, Beverages, Snacks, and Desserts'.
- Just to make this website more appealing to the user, there is a quote displayed in a box and a cookbook offer. This was added to make the page look better.


## Recipe Page
- This page has the ingredients, steps, and a comment section that allows the user to leave a comment under the dish.
- For example, the 'Yam and Egg Sauce' dish has the title, the image, and the introduction, along with a button that says 'Read More'. If the user clicks on the button, it will take the user to a page that has the ingredients, steps, a comment section that allows the user to leave a comment under the recipe of the dish, and a favorite feature that allows the user to favorite the recipe. Once that is favorited, it will be saved to the 'Favorite Recipe' page.
- There is a feature that says 'Other Recipes' which includes some images of the other dishes.
- The dishes being grouped into categories makes it easier for the user to access the dishes. It contributes to the purpose of making this a user-friendly website.
- Other features that have been put into place to make the page nicer to look at are the 'Newsletter' and a quote.
- The newsletter is a part of a future implementation so that the user can subscribe to it but for the purpose of this project, this feature has been displayed there to make the page look better. 

## Favorites Page

# Roadmap

# Technologies Used
- Django: for full-stack framework in order to develop the app.
- JavaScript:
- HTML:
- CSS:
  
## Core Development Technologies

## Libraries, Frameworks, and Packages

## Python/Django Packages

## Infrastructural Technologies
- Heroku: for hosting the application.
- 

# Testing

## Automatic Testing

## Manual Testing

## General Testing

# Credits
- ChatGPT: used this for getting the recipes for the dishes.





