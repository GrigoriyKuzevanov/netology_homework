from django.test import TestCase, Client


class TestSampleCase(TestCase):
    def test_sample_view(self):
        client = Client()
        response = client.get('/test/')
        self.assertEqual(response.content.decode(), 'Hello!')
