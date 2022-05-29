# #NazGallery

## Author
Nazarena Wambura.</br>
[Github](https://github.com/nazarena254)

### Homepage
![nazzblog](./picture/static/images/nazgallery.png)
### Wireframe sample
![nazzblog](./picture/static/images/wirefrm.jpeg)
### Admin panel
![nazzblog](./picture/static/images/djangoAdmin.png)

## Description
This is a Django web application. It is a photo gallery  where a user can view different photos based on locations they were taken, search the photos by categories they belong to and copy the photo link to share with others.The admin is the one who populates the database.


## User Story
1. View different photos that interest them
2. Click a single image to expand it and view the details of that photo
3. Search for different categories
4. View photos based on the location they were taken.


## Behaviour Driven Development (BDD)

1. View by Location

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the location you want from the tabs in the landing page  | location| Only images from that location are displayed  | 

2. Search by Category 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter a search category on the search form   | searchTerm| Images that belong to that category are displayed  | 


3. Admin View

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on Admin on navigation bar | Username, Password| User is redirected to the admin page where they can manage the database  |  

4. Copy Image Link

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the copy icon on the image modal that appears after clicking on the image | copy link| The image link is copied to clipboard  |  


## Setup/Installation Requirements
1. clone repository
    https://github.com/nazarena254/NazGallery.git   
2. Move to the folder and install requirements
    cd gallery
    pip install -r requirements.txt
3.  Type code . or atom . based on the text editor you have and work on it.   

### Database
1. Set up Database,and put your username and password in the code

2. Make migrations
    python3 manage.py makemigrations picture

3. Migrate
   python3 manage.py migrate 
    
### Running the Application
1. Run main apllication
   * python3 manage.py runserver

2. Run tests    
   * python3.6 manage.py test picture

###
1. Creating Admin Locally
    python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.6
* Django 3.2
* Bootstrap
* PostgreSQL
* Heroku
* Markdown

## Support & Contact Information
For any further inquiries, bugs, contributions or comments, reach me at:<br>
Email:<nancyngunjiri1@gmail.com>

### License
[MIT License](https://github.com/nazarena254/NazGallery/blob/master/license)
Copyright (c) 2021 **Nazarena Wambura**