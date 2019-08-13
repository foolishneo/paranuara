from __future__ import with_statement
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
import json 

company_data = []
people_data = []
fruits_data = []
alive_brown_eyes = []
company_employees = []

@api_view(['GET'])
def get_person_food(request, id):   
    global people_data
    load_json()

    person = [ p for p in people_data if p['index'] == id ][0]
    username = person['email'].split('@')[0]
    favourite_food = person['favouriteFood']
    fav_fruits = [ f for f in favourite_food if f.upper() in fruits_data ]
    fav_veg = [ f for f in favourite_food if f not in fav_fruits ]

    return Response({
        'username': username,
        'age': person['age'],
        'fruits': fav_fruits, 
        'vegetables': fav_veg
    })

@api_view(['GET'])
def get_employees_by_company_id(request, company_id):
    global company_employees
    load_company_employees()    
    
    for i in range(len(company_employees)):        
        if company_employees[i]["index"] == company_id:   
            return Response(company_employees[i].get('employees', 'This company has no employee'))         
    raise NotFound(f'Company (id={company_id}) not found. Check company_id in the URL')            

@api_view(['GET'])
def get_people_by_id(request, id1, id2):   
    global people_data   
    global alive_brown_eyes    
    load_json()
    
    person_1 = get_person_info(id1)
    person_2 = get_person_info(id2)

    common_friends = set(person_1['friends']).intersection(set(person_2['friends']))
    if not alive_brown_eyes:
        alive_brown_eyes = list(filter(lambda person: (person['eyeColor'].lower() == 'brown' and not person['has_died']), people_data))
    common_friends_alive_brown_eyes = [ f for f in alive_brown_eyes if f['index'] in common_friends ] 
    
    return Response({
        'person_1': person_1,
        'person_2': person_2,
        'common_friends_alive_brown_eyes': common_friends_alive_brown_eyes
    })

def get_person_info(id):
    global people_data
    person = [p for p in people_data if p["index"] == id][0]

    if person:
        properties = ['name', 'age', 'address', 'phone']
        filtered_person = {k:person[k] for k in properties}
        filtered_person['friends'] = {f['index'] for f in person['friends']}
        return filtered_person
    else:
        raise NotFound(f'Person (id={id}) not found. Check person_id in the URL')    

def load_company_employees():
    global company_data
    global people_data
    global company_employees

    load_json()
    
    if not company_employees:
        for i in range(len(people_data)):            
            company_employees = add_employees(company_data, people_data[i])

def add_employees(company_data, employee):
    for i in range(len(company_data)):
        if company_data[i]['index'] == employee['company_id']:
            if 'employees' not in company_data[i].keys():
                company_data[i]['employees'] = []
            company_data[i]['employees'].append(employee['name'])
    return company_data

def load_json():    
    global company_data
    if not company_data:
        company_data_file = 'resources/companies.json'
        try:
            with open(company_data_file) as f:                
                company_data = json.load(f) 
        except EnvironmentError:
            raise NotFound(f'Data file not found: {company_data_file}')
    
    global people_data
    if not people_data:
        try:
            people_data_file = 'resources/people.json'
            with open(people_data_file) as f:
                people_data = json.load(f)                      
        except EnvironmentError:
            raise NotFound(f'Data file not found: {people_data_file}')

    global fruits_data
    if not fruits_data:
        try:
            fruits_data_file = 'resources/fruits.json'
            with open(fruits_data_file) as f:
                fruits_data = json.load(f)    
                fruits_data = fruits_data['fruits']                  
        except EnvironmentError:
            raise NotFound(f'Data file not found: {fruits_data_file}')

          