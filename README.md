# LoKeramik
## Milestone Project 4
![Lokeramik Responsive Design](https://github.com/Natte-Z/LoKeramik/blob/94bec578ddcdd2bbf57006f74e0e8ddd4a94381f/documentation/readme_images/responsive.png)

## Introduction

LoKeramik is an e-commerce and general contact website offering ceramic products and course services.

-   [View the LoKeramik Heroku App](https://lo-keramik.herokuapp.com/)
-   [View the repository on GitHub](https://github.com/Natte-Z/LoKeramik)

![]()

This is my final project of four Milestone Projects that make up the Full-Stack Web Development Diploma Training at Code Institute. The project's main requirements are: to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database; as well as the implementation of a checkout functionality, which has been achieved through the use of Stripe. 

LoKeramik is therefore a Python-Django web application, backed by a PostgreSQL (and SQLite3) database, and deployed via the Heroku PaaS. This project uses the Stripe Checkout API (for educational purposes only: not currently taking real card payments) and is styled using the Bootstrap Grid System. 

**NOTE:** If you would like to test the payment functionality of this project, please create an account and use the card number 4242 4242 4242 4242 with any address details, expiry date and CVC that you choose.

It is also to mention that the project was created in discussion with a local client I have in Stockholm and that the Stripe test-functionality will be changed lateronwards. 


[Click here to view the project live.](https://lo-keramik.herokuapp.com/)
  
As you read this document, you will find my complete development process, from UX strategy to deployment.

## Contents table

 - [UX](https://github.com/Natte-Z/LoKeramik#ux)
	 - [Wireframe](https://github.com/Natte-Z/LoKeramik#wireframe)
	 - [Color Palette](https://github.com/Natte-Z/LoKeramik#color-palette)
 - [User Stories](https://github.com/Natte-Z/LoKeramik#user-stories)
	 - [User and Their Goals](https://github.com/Natte-Z/LoKeramik#user-and-their-goals)
	 - [User Avatar](https://github.com/Natte-Z/LoKeramik#user-avatar)
	 - [User's Main Challenges](https://github.com/Natte-Z/LoKeramik#users-main-challenges)
 - [Database Structure](https://github.com/Natte-Z/LoKeramik#database-structure)
	 - [Profiles App](https://github.com/Natte-Z/LoKeramik#profiles-app)
	 - [Checkout App](https://github.com/Natte-Z/LoKeramik#checkout-app)
	 - [Products App](https://github.com/Natte-Z/LoKeramik#products-app)
	 - [Courses App](https://github.com/Natte-Z/LoKeramik#courses-app)
 - [Features](https://github.com/Natte-Z/LoKeramik#features)
	 - [Existing Features](https://github.com/Natte-Z/LoKeramik#existing-features)
	 - [Features Left to Implement](https://github.com/Natte-Z/LoKeramik#features-left-to-implement)
 - [Technologies Used](https://github.com/Natte-Z/LoKeramik#technologies-used)
 - [Testing](https://github.com/Natte-Z/LoKeramik#testing)
	 - [Defensive Design](https://github.com/Natte-Z/LoKeramik#defensive-design)
	 - [Validators and Formatters](https://github.com/Natte-Z/LoKeramik#validators-and-formatters)
	 - [Compatibility Tests](https://github.com/Natte-Z/LoKeramik#compatibility-tests)
 - [Deployment](https://github.com/Natte-Z/LoKeramik#deployment)
	 - [Local Deployment](https://github.com/Natte-Z/LoKeramik#local-deployment)
	 - [Heroku Deployment](https://github.com/Natte-Z/LoKeramik#heroku-deployment)
 - [Credits](https://github.com/Natte-Z/LoKeramik#credits)
 - [Acknowledgements](https://github.com/Natte-Z/LoKeramik#acknowledgements)

## UX

### Wireframe
Link to the wireframe on [Figma](https://www.figma.com/file/tj0O4mqcPwjMKJZvnATuyw/Lo-Keramik?node-id=354%3A31)

### Color Palette
![enter image description here](x)
The color palette is made of 5 different colors: 
 - a darker grey #3d3d3f
 - a lighter grey #8f8d8a
 - a cobalt blue as the highlighting color #7395AE
 - Egg shade #eae7dc
 - Sand #D8C3A5


## User Stories
*Click on the image to see it larger:*
![](https://github.com/Natte-Z/LoKeramik/blob/150278ca4c2f85db49a76f8955c7b6c545766ce2/documentation/userstories.png)

### User and Their Goals

Since Covid-19 became a global pandemic, many people around the world began to live through lockdowns. Many began to work from home; others lost their jobs. With uncertainty becoming a norm, we can't know when, or if, our societies will return to normal and what consequences the pandemic will leave behind.

Overall, Covid-19 makes it harder for people to visit stores directly, which is why they look more for online alternatives. My client experienced a large drop of sales since the pandemic started and many less people that visited her hair dresser salong. Her side business, making ceramics became more and more like a second income, because people could still come to her small courses and liked her pottery a lot. 

So to make her products more visible to people, we decided to create an online webshop, so that customers could buy her products directly and also see what is all available. Because until now, my client only worked through instagram to showcase her products and get in contact with people to book her pottery courses. With the new website, she can showcase her products, easily add and delete them herself as well as showcase the difference between her courses and provides customers an easy and professional tool to contact her. 

LoKeramik is becoming more popular than ever and customers book months in advance her courses, however the products sale is not as stimulant, which is why a webshop was the best alternatives to market her products better. 

My client wished for a very simple design, without much colors or bright effects. For her it was mostly about bringing up the products so that she can add and delete them herself and show what she is working on at the moment. 

### User Avatar

- inhabitants of Stockholm and surrounding, who are interested in ceramics and nice table- and kitchenware;
- people, who are interested in trying pottery themselves.
        
### User's Main challenges

Some main challenges regular people encounter are:

- finding closeby made ceramics
- homemade products, that are not mass production
- homemade products, that are unique
- products that are special, but still affordable
- a good guidance to beginners and advanced pottery making
- many pottery courses only show half of the pottery process, the making, but not the whole process including burning and glazing

## Database Structure

LoKeramik is built on Django, and primarily uses the SQLite3 database during all development stages. Through the deployment to Heroku, the database was changed to a PostgreSQL database as that is provided by Heroku as an add-on for production.

The Django’s default user model for authorization is also in use, which allows the project to meet one of the main requirements of separating features by anonymous users, users in session and superusers.

The structure of the Checkout and Products apps are inspired by one of Code Institute's mini projects: _Boutique Ado_.

The main database structure models are documented below.

### Profiles App

#### ---->> UserProfile Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True
 Favourites | ManyToManyField | Product

### Checkout App

#### ---->> Checkout Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full Name | full_name | CharField | max_length=50, null=False, blank=False
 Email | email | EmailField | max_length=254, null=False, blank=False
 Phone number | phone_number | CharField | max_length=20, null=False, blank=False
 Country | country | CountryField | blank_label='Country*', null=False, blank=False
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Town/City | town_or_city | CharField | max_length=40, null=False, blank=False
 Street Address 1 | street_address1 | CharField | max_length=80, null=False, blank=False
 Street Address 2 | street_address2 | CharField | max_length=80, null=False, blank=True
 County | county | CharField | max_length=80, null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True
 Delivery Cost | DecimalField | max_digits=6 | decimal_places=2 | null=False | default=0
 Order Total | DecimalField | max_digits=10 | decimal_places=2 | null=False | default=0
 Grand Total | DecimalField | max_digits=10 | decimal_places=2 | null=False | default=0
 Original Bag | TextField | null=False | blank=False | default=''
 Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''
 
#### User Reviews App

*UserReviews Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=modals.SET_NULL, null=True, blank=True, related_name="user_profile"
 Service | service | ForeignKey 'Service' | on_delete=models.SET_NULL, null=True, blank=True, related_name="user_service"
 Review Title | review_title | Charfield | max_length=200
 Review Content | review_content | TextField | blank=True, null=True, default=""

### Products App

#### ---->> Services Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
Sku | sku | CharField | max_length=254, null=True, blank=True
Name | name | CharField | max_length=254
Description | description | TextField |max_length=700
Price | price | DecimalField | max_digits=6, decimal_places=2
Material | CharField | max_length=15 | null=True | blank=True
Colour | CharField | max_length=15 | null=True | blank=True
Image | image | ImageField | null=True, blank=True

#### ---->> Category Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | CharField | max_length=254
Friendly Name | friendly_name | Charfield | max_length=254, null=True, blank=True

### Courses App

#### ---->> Courses Model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name |CharField | max_length=254
Description | TextField | max_length=254
Price | DecimalField | max_digits=6 | decimal_places=0
Duration | CharField | max_length=15 | null=True | blank=True
Participants | DecimalField | max_digits=1 | decimal_places=0
Level | CharField | max_length=15 | null=True | blank=True
Image |ImageField | null=True | blank=True

### Review App

#### ---->> Review Model
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
UserProfile | ForeignKey | on_delete | null=True | blank=True | related_name
Course | ForeignKey | on_delete | null=True | blank=True | related_name
ReviewTitle | CharField | max_length=200 
ReviewContent | Textfield | null=True | blank=True

## Features

### Existing Features 
  
1. **Navbar and Menu:** the top main navbar contains the companies name, main nav items and the links to access user profile and shopping bag.
    - Main nav items: Home; products (all products; categories (kitchenware, tableware and interior)); courses (courses; reviews; add review); contact
	- These elements are consistent in design and are responsive throughout the website. However, the contents of the menu changes depending on if a user is logged in or not.  
	- The menu bar for users logged-in features a 'Logout' link where the 'Sign Up' link usually is. When a user in session chooses to logout, a toast message confirms this action, and they are redirected back to the home page.  
	- Users with items added to their Bag notice an additional 'Checkout' link in the bag view of the navbar, allowing them direct access to go straight to the shopping bag and from there to the checkout.  
	- The authentication pages (Sign In, Sign Up & Sign Out) were built with Django, and therefore include all Django's built-in features (including requesting an email for forgotten passwords.)
  
2. **Toasts:** All toast messages appear under the menu bar.  
	- Depending on the type of message, the toast color changes to reflect this message.  
	- Across the 'Product' page, toast messages appear to confirm the contents of a user's Bag when they add new product items. This message also includes the 'Go To Checkout' button: to prompt users to check their bag content or proceed to checkout.  
  
3. **Sign In / Sign Up:** These pages feature the consistent white overlay as a background, to maintain simplicity and design minimalism.  
	- On the top-left right, the user will find the respective Sign In or Sign Up forms, prompting them to access the parts of the website that require authentication.  
	- Regular registered users can check and edit their profile details and check their order history (they can't currently enter their full name)
    - logged in users will also find a list with their favourite items that they can save from the products page  
	- Admin with superuser privileges can add, edit and delete products from the database. This was especially a wish from my client, since she wanted to be able to do these later on herself. 
  
4. **Sign Out:** The content in this page displays a box that either prompts and verifies that a user wishes to leave the site, with a 'Sign Out' button. Once signed out, users are redirected back to the Home page.  
  
5. **Checkout Overlay:** A blue overlay with a spinner gif appears after checkout is initiated and while the transaction is being processed and until the checkout success page has fully loaded.  
  
6. **Product Pages:**   
	- this follows a Bootstrap responsive grid system, using the cards class.  
	- As the user scrolls down the page, they find cards for each product belonging to that category or to all product categories if the page is all products.  
	- Each card contains the products price; the client wanted this to be very clean and not with too much information, because all products follow a certain style with which they all can be matched together  
	- Produtc page include a filtering dropdown box, as well as a top category badges selection to facilitate finding the desired product page and details.  
	- Users can add the products to their bag from the products details page.
  
7. **Products Details Pages:** Users access these pages by clicking on the products image of the respective card.  
	- This page features the service image, title, description about it, customization options and the price.  
	- From this page users can add the products to their bag.  
	- Each product detailed view has an extra button with "add to favourites" that will allow the user to add this to their favourites list, which is listed on their profiles page
  
8. **Profile Page:** The content of the page changes depending on if the user is logged in or not, if they have items in their bag and if they have previous orders.   
	- Users can view and update their contact and billing details.  
	- If users have purchased products in the past, a table with their order history appears.
  
9. **Bag:** This page is similar to a shopping cart on e-commerce sites.  
	- The user can see each item in their bag.  
	- All information about service customization that a user has selected is included on this page, including price, quantity, subtotal and a image.  
	- A 'checkout' button prompts the user to confirm the order through payment.  
  
10. **Checkout:** When a user has added items to their bag, the 'Checkout' link appears in the dropdown navigation menu.  
	- Users can add their details to an input form and can select whether to save the information to their profile for future reservations.  
	- An order summary also includes the name, price, quantity of each item in their bag.  
	- Below these features, a user can either select the 'back to products' link or confirm the reservation with the 'Secure Checkout' button.  
  
11. **Checkout Success:** This page is accessed by completing the checkout process. However, it can also be accessed through the 'Profile' page when clicking on more information about a previous order. In this case, an alert message confirms that the user is viewing a previous order and that the confirmation email was sent during payment.  
  
12. **Back to Top Button:** Long pages feature a 'scroll to top' arrow that becomes visible when the user has scrolled down the page.

13. **Courses:** A page that renders all the courses that LoKeramik is currently offering. The courses show different information:
    - title, course description, amount of participants that can do the course, course duration, the level (advanced/beginner) and the price

14. **Reviews:** Here users can read through existing reviews that other users have posted.
    - reviews can only be written by logged in users
    - because there is currently no "add to bag" function for the courses, there is unfortunately no security that implies if users actually have been taken the course. This is part of the future implementations

15. **Add a review:** Users can leave a review with their username posted, a title, review content and the course to which they are referring


### Features Left to Implement

1. **Login with Social media:** Since living in Sweden everyone is very connected and people really want to login with their social media accounts. So this will be tackled once I have more time to fully finish my clients website. 
    
2. **Checkout payment with Klarna:** Klarna is a bank and online payment system, for which I currently work and which is highly in demand in Sweden and other countries. I know that Stripe supports Klarna payments, because know that we have many merchants that use this function so for february I will focus on implementing Klarna in the checkout payment option, so that customers can directly pay with that as an extra option to credit cards. 

3. **Full Name:** Currently, users cannot enter their full name in their details session; their name has to be entered at each new order. The implementation of this feature is beyond the scope of this project and planned to be developed in the future.

4. **Course add/edit function:** Currently there is no option for the super user to add/edit the courses, but this will also be implemented in the future, but hasnt been done for this project due to lack of time. 

5. **Review add/edit function:** Currently there is no option for the super user to add/edit the courses, but this will also be implemented in the future, but hasnt been done for this project due to lack of time. 

6. **Review security:** Future implementation will be to add a checking logic to see whether users have booked a course and then they can write a review about that.  

7. **Favourites button update:** At the moment the favourites button works with a get request, which is not very sustainable, because the page needs to reload everytime the user pushes the button. So for future implements it would be good to rethink the button functionality, so that the page does not need to reload once a user wants to add a item to their favourites list. 

8. **Course add to bag function:** In order to implement point 6 there needs to be an additional add to bag function for the user so that the info about the course registration/purchase can be registered on the profile and with that the security can be built. 

## Technologies Used

-   [HTML5](https://www.w3schools.com/html/)
-   [CSS3](https://www.w3schools.com/css/)
-   [JavaScript](https://www.w3schools.com/js/DEFAULT.asp)
-   [jQuery](https://jquery.com/)
-   [Python](https://www.python.org/)
-   [Django](https://www.djangoproject.com/)
-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
-   [SQLite](https://docs.djangoproject.com/en/3.1/ref/databases/#sqlite-notes)
-   [PostgresSQL](https://www.heroku.com/postgres)
-   [Psycopg2](https://pypi.org/project/psycopg2/)
-   [Bootstrap framework](https://getbootstrap.com/)
-   [Gitpod](https://www.gitpod.io/)
-   [Git Version Control](https://git-scm.com/)
-   [GitHub](https://github.com/)
-   [Heroku](https://www.heroku.com/)
-   [Stripe](https://stripe.com/en-se)
-   [AWS S3 Bucket](https://aws.amazon.com/s3/)
-   [Gmail](https://www.google.com/intl/sv/gmail/about/#)
-   [Figma](https://www.figma.com/)
-   [FontAwesome](https://fontawesome.com/)
-   [Google Fonts](https://fonts.google.com/)
    
## Testing

### Defensive Design

- I used a 'mobile first' approach to developing this project, and consistenly used Google Chrome's Dev Tools to view the view the output of my code on different screen sizes, however there are still some improvements to be made. 
- During debugging, my approach often included using print statements to check where an issue was coming from and checking the page source from the browser when reviewing the code. 
- Throughout the testing phase I came across many issues, but the print function as well as the "show source code" really helped me to understand where issues are coming from, whether it was python/javascript with the print or html and css with inspect and show page source. 

### Validators and Formatters
#### HTML
- I used the built-in formatter feature in Gitpod to clean my HTML Code, as well as passed my code through the [W3C Markup Validation Service](https://validator.w3.org/)
Doing so brought up a few errors throughout the project related to using Django templates. These included:
1. An issue in using '{}' brackets as part of the source for ```<a>``` elements and ```<img>``` elements. However, this syntax is necessary to access static files and urls and was therefore ignored.
2. All html templates led to errors that the doctype and language were not declared. As the templates were based on the base.html template where these were addressed, I declared the doctype, because I got annoyed by the errors, but the language I kept.
3. Some Bootstrap Modals on the site returned errors with their 'aria-labelledby' attribute. This error was related to using templating language to specify the item the modal was related to, so this error was also ultimately ignored.
4. Further regarding Bootstrap Modals, the validator showed that some buttons had been listed as ```<a>``` elements with no 'href' attribute. This issue was rectified by changing the element to a ```<button>``` element as it should be. Doing so led to no further errors.
5. The profile.html template returned a few errors shown on the screenshot below. However, these errors are related to using templating language in the html document and were therefore ignored as the validator was raising incorrect errors.
![profile.html validator errors](https://github.com/Natte-Z/LoKeramik/blob/150278ca4c2f85db49a76f8955c7b6c545766ce2/documentation/testing_screenshots/htmlvalidation.png)

#### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript code.
The issues that came up here were mostly related to comments that cannot be read as comments by the validator. 
![sendEmailJs validator errors](https://github.com/Natte-Z/LoKeramik/blob/150278ca4c2f85db49a76f8955c7b6c545766ce2/documentation/testing_screenshots/jsvalidation.png)

#### Python
I used [PEP8](http://pep8online.com/checkresult) to check the Python code stored within each app.
This returned indentation errors and warnings that some lines that were too long within a few files. I tried to take care of the too long lines and some other style issues, but could not resolve all of them, because they let to other issues in the code, so instead of having real issues I kept some of the style issues. 

#### CSS
I checked all CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). 
All individual CSS files passed without any errors. 
- I used  the Gitpod built in Flake8 input to check and format the Python code stored within each app.

### Compatibility tests

#### Using different browsers

I manually tested this project on the following web browsers, checking that all aspects worked as planned:
- Google Chrome
- Mozilla Firefox
-  Apple Safari

#### Using different devices

I tested this project on the following devices:
- Apple MacBook Pro 13"
- Samsung Galaxy
- HP EliteBook
- Lenovo Thinkpad

### Manual tests

#### Features consistent throughout the project
- The spinner overlay works on each template and covers the entire screen except the menu bar. It does not interfere with credit cards that require additional authentication.
- The return to top arrow scrolls smoothly to the top of the page regardless of which screensize the user has,however it corelates with the footer in mobile view and I did not have enough time to fix this. 
- Users who have not signed in are unable to access pages for authenticated users.

#### Menu
- *Logo* - clicking on the logo takes a user back to the home page.
- *Home* - as above, clicking on this link returns the user to the home page.
- *Ceramics* - directs a user to the products page, after choosing which category they want.
- *Courses* - directs a user to the courses, review or add review (if logged in) page
- *Contact* - directs a user to the contact page, were they are able to send a contact form that connects to the clients email and receive a autoreply.
- *Account* - opens a drop down menu with the following content:
    * Users not in session: *Sign In* and *Sign Up*, leading to respective forms.
    * Users who have signed in: *My Profile* and *Sign Out*. Each link leads to their respective pages.
    * Users with items in their bag: additionally, *Checkout* is added which directs them to the checkout page.

#### Footer
- Clicking on the Instagram icon directs the user to the respective websites on new tabs.

#### Home
- The 'Products' button takes users to the 'products' page.
- The 'courses' button, takes the user to the respective page.
- Contact button goes to the contact page. 

#### Courses
- the nav bar links for the three different pages function.
- when on courses, each course has a button that links the user to the contact page to contact LoKeramik to book in a course. Until now Lokeramik has only operated on instagram, so she is used to having people contact her this way, however with the contact form it became much more professional. 
- the add review page works with the button and after pushing it, it directs the user to the review page. 

#### Products pages
- Each product page only shows items related to the relevant category. 
- The clicking on the image within each item card directs users to the correct products details page.
- Users dont have to be signed in can add the item directly from the product detailed page , with a toast message that confirms this action. The toast box also features two buttons that link the user to their bag or the checkout page respectively. However, users are limited to adding 5 items of each to their bag, with an error message explaining this.

#### My Profile
- Users are able to save profile information
- users that are logged in are able to add favourite products from the products detailed page to their profile page.

#### Contact
- The contact form works, leaving an success or error message after sending an email. 
- also the auto reply from emailJS works and email JS sends LoKeramik the respective information to contact the user.

#### Checkout
- Users have to complete the form to confirm their reservation.
- Incorrect card details result in an error message at the bottom of the form.
- Users who have made previous purchases and have saved their details in the past will notice that they are already filled in. Otherwise, users can select the 'save details' checkbox to successfully save their details.
- When a purchase is complete, users are automatically redirected to the confirmation page.

#### Checkout Success 
- Users can see all of their purchase details .

#### Authorisation pages
- Trying to access the Sign In/ Sign Up pages when already in session does not work, just as accessing the Sign Out page when not authorised returns the user to the home page.

To return to the overview of the Hotel Eko project, please click [here](https://github.com/mkthewlis/hotel-eko/blob/master/README.md).

## Deployment

### Local Deployment

This project was developed using [Gitpod](https://gitpod.io) as the chosen IDE and [GitHub](https://github.com) as a remote repository. The Project's source files were regularly pushed to the [GitHub LoKeramik Repository](https://github.com/Natte-Z/LoKeramik) via the  `master`  branch. To reproduce this project within a local deployment, use the following steps and requirements:

1. Have the following installed in your IDE of choice:
	 - Git (for version control)
	 - pip (package installer for Python; pip3 was used at the time of production: October 2020)
	 - Python3 (the programming language used to produce the backend logic of this project)
2. Create an account with  [Stripe](https://stripe.com/en-se), necessary for payment features in the project.
3. Use an email provider (I used [Gmail](https://www.google.com/intl/sv/gmail/about/#) for this project) and sign in and navigate to the  [Google Account Security](https://myaccount.google.com/security)  page.
4. Create two-step authentication by creating an App password for your Django app.
5. Use the same email values to set up your email username and password in the steps below:
	- Scroll to the top of this repository and click on the "clone or download button".
	- Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    - HTTPS: click on the checklist icon to the right of the URL to copy it
    - SSH key: first click on 'Use SSH' then click on the same icon as above

6. Return to your IDE and open a new Terminal window.
7. Change the current working directory to the location where you want the cloned directory.
8. Enter the following command and press 'Enter' to create your local clone:
```
git clone https://github.com/Natte-Z/LoKeramik.git
```
9.  Install the required dependencies with the following command:
```
pip3 install -r requirements.txt
```
10.  Create an env.py file and add the following, complete with your own values:
```
import os
os.environ['AWS_ACCESS_KEY_ID'] = '<your value>'
os.environ['AWS_SECRET_ACCESS_KEY'] = '<your value>'
os.environ['DATABASE_URL'] = '<your value>'
os.environ['EMAIL_HOST_PASS'] = '<your value>'
os.environ['EMAIL_HOST_USER'] = '<your value>'
os.environ['SECRET_KEY'] = '<your value>'
os.environ['STRIPE_PUBLIC_KEY'] = '<your value>'
os.environ['STRIPE_SECRET_KEY'] = '<your value>'
os.environ['STRIPE_WH_SECRET'] = '<your value>'
os.environ['DEVELOPMENT'] = 'True'
os.environ['USE_AWS'] = 'True'
```
11.  Add your env.py file to .gitignore to make sure your database information is not viewable to others and to keep your values safe.

12. To set up the Django SQLite3 tables required for this project, use the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
13.  With this complete, create a superuser for your project with the following command and follow the instructions in the Terminal (note: this will be necessary to add data to your locally deployed version):
```
python3 manage.py createsuperuser
```
14.  Your cloned version is now ready to run locally with the following command:
```
python3 manage.py runserver
```
15.  Once you run your project locally, add '/admin' to the locally deployed project's URL. 
16. Add the service categories and service items to the database. This information can be copied from each individual service's page of the deployed version of the project found here:  [LoKeramik](https://lo-keramik.herokuapp.com/)

### Heroku Deployment

To deploy this project to Heroku, use the following steps as a continuitation from local deployment outlined above:

1. Create a [AWS S3 Bucket](https://aws.amazon.com/s3/), as this will be necessary to store static files and media for deployment.
2. Create an account and sign in to [Heroku](https://heroku.com).
3. Inside the Heroku Dashboard, create a new app with a unique name and set the region to the closest to you, eg. 'Europe'.
4. To use the Postgres database for deployment, select 'Heroku Postgres' as a free add-on.
5. With the app created, go to the 'Settings' tab, click on the 'Reveal Config Variables' button, and input the following values:

| **Key** | **Value** |
--- | ---
 AWS_ACCESS_KEY_ID | your AWS bucket ID
 AWS_SECRET_ACCESS_KEY | your AWS secret key
 DATABASE_URL | your Heroku Postgres database url
 EMAIL_HOST_PASS | your password to use your gmail account for emails
 EMAIL_HOST_USER | your email address
 SECRET_KEY | secret key used for your Django project
 STRIPE_PUBLIC_KEY | obtained through your Stripe account
 STRIPE_SECRET_KEY | obtained through your Stripe account
 STRIPE_WH_SECRET | obtained through your Stripe account
 USE_AWS | True

6. In Gitpod, create a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
7. Create a Procfile with the following content within (making sure that 'Procfile' was written with a capitalized 'P'):
```
echo web: gunicorn stripe_me.wsgi:application > Procfile
```
8. As with local deployment, set up the Postgres database with the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
8. Follow steps 11 to 13 from local deployment outlined above.
9. Commit these changes with the following:
```
git add .
```
```
git commit -m "<your commit message here>"
```
10. With these files committed, log in to Heroku from the terminal using this command and enter your details when prompt:
```
heroku login -i
```
11. Once logged in, link your Heroku app created above as the remote repository with this command:
```
heroku git:remote -a <your app name here>
```
12. Complete the deployment by pushing the projekt to Heroku:
```
git push heroku master
``` 
13. This completes the process of deploying the project to Heroku. Once deployed, continue to push all changes made to the project to Heroku with the final command listed above. It is highly recommend to do this deployment as early as possible in the coding process to not encounter future deployment issues. 

## Credits

### Media

All stock-free images were retrieved from [Unsplash](https://unsplash.com) and [Pexels](https://www.pexels.com/) and used with permission. The media images kept the same name to give credits to the photographer. 

All product and certain content images were made by me to show the clients products and courses. 


## Acknowledgements

Gratitude to the following people for their help, support and inspiration:  
  
- My mentor [Seun Owonikoko](https://github.com/seunkoko) for her calmness and humour, for staying available and supportive through this year of pandemic and struggles. I was very happy to have a female mentor that can act as a female tech role model.  
- To [Code Institute](https://codeinstitute.net/), their team and staff, to the student services and advisors for their support. Especially I would like to thank all the amazing tutors for their patience, communication skills through chat, good humour and dedication! Without them this programme wouldn't be the same and I am truly thankful to many of them!
- To my entourage aka roommates and friends for continually motivating me through struggles and challenges. For sending me out to take a walk and leave the computer and caring.  
  
Thank you!
