from django.test import TestCase
from django.urls import reverse

class ListingsHomeViewTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('home'))
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Craiglist</title>', html)
        self.assertTrue(html.endswith('</html>'))