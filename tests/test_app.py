# tests/test_app.py

import unittest
import os

os.environ["TESTING"] = "true"

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        zidanni_response = self.client.get("/")
        assert zidanni_response.status_code == 200
        html = zidanni_response.get_data(as_text=True)
        assert "<title>Zidanni Clerigo</title>" in html
        assert '<img src= "./static/img/zidanni.jpg" alt="Profile Picture">' in html
        assert '<header class="nav-bar">' in html

        manav_response = self.client.get("/manav")
        assert manav_response.status_code == 200
        html = manav_response.get_data(as_text=True)
        assert "<title>Manav</title>" in html
        assert '<img src= "./static/img/manav.jpg" alt="Profile Picture">' in html
        assert '<header class="nav-bar">' in html

        deeptanshu_response = self.client.get("/deeptanshu")
        assert deeptanshu_response.status_code == 200
        html = deeptanshu_response.get_data(as_text=True)
        assert "<title>Deeptanshu</title>" in html
        assert '<img src= "./static/img/deeptanshu.jpg" alt="Profile Picture">' in html
        assert '<header class="nav-bar">' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        post_response = self.client.post(
            "/api/timeline_post",
            json={"name": "Bob", "email": "bob@example.com", "content": "hi im bob"},
        )
        assert post_response.status_code == 200
        assert post_response.is_json
        post_json = post_response.get_json()
        assert post_json["name"] == "Bob"
        assert post_json["email"] == "bob@example.com"
        assert post_json["content"] == "hi im bob"

        new_response = self.client.get("/api/timeline_post")
        assert new_response.status_code == 200
        assert new_response.is_json
        new_json = new_response.get_json()
        assert "timeline_posts" in new_json
        assert len(new_json["timeline_posts"]) == 1
        assert new_json["timeline_posts"][0]["name"] == "Bob"

        timeline_page = self.client.get("/timeline")
        assert timeline_page.status_code == 200
        timeline_html = timeline_page.get_data(as_text=True)
        assert "<title>Timeline</title>" in timeline_html
        timeline_author = '<div class="post-author">${post.name}</div>'
        timeline_content = '<div class="post-content">${post.content}</div>'
        assert timeline_author in timeline_html
        assert timeline_content in timeline_html
