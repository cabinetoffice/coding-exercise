import unittest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestAPI(unittest.TestCase):
    def test_hello(self):
        response = client.get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World!"})

    def test_add(self):
        """Testing the addition of two numbers."""

        response = client.get("/add", params={"num1": 5, "num2": 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 15})

    def test_add_with_string(self):
        """Tests to see if a string provided returns a failure message non 200 HTTP
        status code, indicating incorrect type provided."""

        response = client.get("/add", params={"num1": "Not a number", "num2": "10"})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["detail"][0]["msg"],
                          "value is not a valid integer")

    def test_join_words(self):
        """Testing the joining of two words with a dash in between."""

        response = client.get("/join-words", params={"word1": "hello", "word2": "world"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": "hello-world"})


if __name__ == "__main__":
    unittest.main()
