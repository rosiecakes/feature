import requests
import unittest


API_URL = "http://127.0.0.1:1212/"

class TestApiGet(unittest.TestCase):
    def test_request_response_ok(self):
        response = requests.get(API_URL)
        self.assertTrue(response.ok)

    def test_request_response_not_ok(self):
        response = requests.get(API_URL + '{}'.format('invalid'))
        self.assertEqual(response.json()['_status'], 'ERR')

    def test_request_response_ok_endpoint(self):
        response = requests.get(API_URL + '{}'.format('clients'))
        self.assertTrue(response.ok)

    def test_request_response_ok_user(self):
        response = requests.get(API_URL + '{}'.format('users/rosie'))
        self.assertTrue(response.ok)

if __name__ == '__main__':
    unittest.main()
