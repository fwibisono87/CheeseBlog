from django.test import TestCase, Client


# Create your tests here.

class mainPageTest(TestCase):
    def test_mainpage_exists(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)
