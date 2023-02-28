from django.test import TestCase
from django.urls import reverse,resolve

from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.

class TestSample(TestCase):

    def setup(self):
        self.client=APIClient
    
    def test_index(self): 
        url=reverse('ecommerce_admin:index')
        res=self.client.get(url)
        print(res.data)
        self.assertEquals(res.status_code,200)
        self.assertEquals(res.data,'congratulations, you have created an API')
