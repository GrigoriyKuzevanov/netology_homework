from django.test import TestCase, Client


class TestArticles(TestCase):
    def test_articles(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
