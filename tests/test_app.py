import unittest
import os

os.environ["TESTING"] = "true"

from app import app, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        # Clear all timeline posts between tests
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1>Zidanni Clerigo</h1>" in html

    def test_timeline(self):
        # Test the API endpoint returns JSON with empty timeline initially
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Test posting a new timeline post (John Doe)
        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "content": "Hello, I am John Doe!"
        })
        assert response.status_code == 201
        assert response.is_json
        json = response.get_json()
        assert "name" in json
        assert "email" in json
        assert "content" in json
        assert "created_at" in json
        assert "id" in json
        assert json["name"] == "John Doe"

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

    def test_malformed_post(self):
        res = self.client.post("/api/timeline_post", data={
            "name": "",
            "email": "bob@example.com",
            "content": "Missing name field"
        })
        assert res.status_code == 400
        html = res.get_data(as_text=True)
        assert "Invalid name" in html

        res = self.client.post("/api/timeline_post", data={
            "name": "Bob",
            "email": "invalid-email",
            "content": "Bad email format"
        })
        assert res.status_code == 400
        html = res.get_data(as_text=True)
        assert "Invalid email" in html

        res = self.client.post("/api/timeline_post", data={
            "name": "Bob",
            "email": "bob@example.com",
            "content": ""
        })
        assert res.status_code == 400
        html = res.get_data(as_text=True)
        assert "Invalid content" in html