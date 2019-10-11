# IMS BackEnd 

This is an API that registers a user and also includes an API that adds stock

## Installation

This project assumes you are familiar with Django and Django REST Framework, Postgres and are using Python 3.5 and above. Git Clone the repo to your 
computer and run the following commands to get started.

`pip install -r requirements.txt `

* Make and run migrations by using the following commands

`python manage.py make migrations `

` python manage.py migrate `

* Run the local server 

` python manage.py runserver `


## API Features

### Adding Stock

To Add Stock, go to this API URL 

`http://localhost:8000/api/CustomerStock/` 
 
 You can also Delete and Patch by adding the `id` of that user 

### User Registration 

To register a user, go to this API URL 
`http://localhost:8000/api/auth/register`  

### User Login

To login as a registered user, go to this API URL

`http://localhost:8000/api/auth/login`

### User Logout

To logout as a registered user, go to this API URL 

`http://localhost:8000/api/auth/logout`

### Password Reset 

To reset a password for a registered user, go to this API URL

`http://127.0.0.1:8000/rest-auth/password/reset/`
`http://127.0.0.1:8000/rest-auth/password/reset/confirm/`

### Change User Password

`http://127.0.0.1:8000/api/passwordchange/`

