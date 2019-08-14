import json 
from django.urls import reverse
from rest_framework.test import APITestCase

class ParanuaraAPITest(APITestCase):

    def test_get_company_employees(self):
        url = reverse('get-company-employees', kwargs={ 'company_id': 0 })
        result = self.client.get(url).data              
        self.assertEqual(result, 'This company has no employee')   

        url = reverse('get-company-employees', kwargs={ 'company_id': 9999 })
        result = self.client.get(url).data           
        self.assertEqual('not found' in result['detail'], True)    

        url = reverse('get-company-employees', kwargs={ 'company_id': 1 })
        result = self.client.get(url).data           
        self.assertEqual(len(result),7)    

    def test_get_person_favourite_food(self):
        url = reverse('get-person-favourite-fruits-vegetables', kwargs={ 'id': 0 })
        result = self.client.get(url).data                 
        self.assertEqual(result['username'], 'carmellalambert') 
        self.assertEqual('orange' in result['fruits'], True) 

        url = reverse('get-person-favourite-fruits-vegetables', kwargs={ 'id': 9999 })
        result = self.client.get(url).data                 
        self.assertEqual('not found' in result['detail'], True)    
        
    def test_get_people_common_friends(self):
        url = reverse('get-people-common-friends', kwargs={ 'id1': 1, 'id2': 2 })
        result = self.client.get(url).data                         
        self.assertEqual(result['person_1']['name'], 'Decker Mckenzie') 
        self.assertEqual(result['person_2']['name'], 'Bonnie Bass') 
        self.assertEqual(len(result['common_friends_alive_brown_eyes']), 1) 
        
        # url = reverse('get-people-common-friends', kwargs={ 'id1': 9999, 'id2': 2 })
        # result = self.client.get(url).data                 
        # self.assertEqual('not found' in result['detail'], True)
    