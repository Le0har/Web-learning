from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from linkshortener.models import Links


class LinkshortenerAPITests(APITestCase):
    fixtures = ['linkshortener_links.json']

    def test_create_link(self):
        url = reverse('home')
        data = {'url': 'http://localhost:8000/api/v1/testlinkcreate'}
        number_records = Links.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Links.objects.count(), number_records + 1)
        self.assertTrue(Links.objects.filter(full_link=data['url']).exists())
        last_id = Links.objects.last().id
        self.assertEqual(Links.objects.get(pk=last_id).full_link, 'http://localhost:8000/api/v1/testlinkcreate')
        self.assertEqual(Links.objects.get(pk=last_id).short_link, f'http://localhost:8000/{last_id}')

    def test_unique_link(self):
        url = reverse('home')
        data = {'url': 'http://localhost:8000/hello_from_DRF'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_wrong_url(self):
        url = reverse('home')
        data = {'wrong_url': 'http://localhost:8000/api/v1/tmp_link2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_short_link(self):
        url = reverse('home') + '1'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_link'], 'http://localhost:8000/hello_from_DRF')
        self.assertNotEqual(response.data['full_link'], 'abrakadabra')

    def test_get_wrong_short_link(self):
        url = reverse('home') + '999'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
