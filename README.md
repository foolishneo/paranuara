# Paranuara Challenge

A set of APIs to query data about Paranuara's companies and citizens.

## API endpoints

1. Given a company, the API needs to return all their employees.

> **GET** api/v1/company/:company_id/

2. Given 2 people, provide their information (Name, Age, Address, Phone) and the list of their friends in common which have brown eyes and are still alive.

> **GET** api/v1/person/:id1/:id2/

3. Given 1 people, provide a list of fruits and vegetables they like.

> **GET** api/v1/person/:id/food/

## Installation

0. You need to have python3 installed on your machine.   
> (MacOS) brew install python3

> (Linux) sudo apt-get install python3 

1. Clone the project
> git clone https://github.com/foolishneo/paranuara.git

2. Create and activate a virtualenv:
> cd paranuara

> python3 -m venv env

> source env/bin/activate

**Note:** if you don't have *virtualenv* installed
> (MacOS) pip3 install virtualenv

> (Linux) sudo apt-get install python3-venv

3. Install *django* and *django-rest-framework*

> (env) paranuara$ pip3 install django

> (env) paranuara$ pip3 install djangorestframework

4. Run the application
> python3 manage.py runserver

The application is running at localhost:8000

5. Run the tests
> python3 manage.py test

## Notes:

1. All APIs use *id* as the parameter to query data.

2. To distinguish between fruits and vegetables, a list of fruits is declared in fruits.json. It would be better if I can verify it using a public API but I couldn't find such a resource.

3. *username* is constructed from the person's email. As all people in this planet are using the same domain name (earthmark.com), their respective email handle should be unique and could be used as their username. If necessary, we can mix it with the *guid* or implement a *check_if_username_exists* function to make sure there is no duplication.

