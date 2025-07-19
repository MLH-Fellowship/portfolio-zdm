import unittest
from peewee import *
from datetime import datetime

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(
            name="John Doe",
            email="john.doe@example.com",
            content="Hello, I am John Doe!",
            created_at=datetime.now()
        )
        assert first_post.id == 1

        second_post = TimelinePost.create(  
            name="Jane Doe",
            email="jane.doe@example.com",
            content="Hello, I am Jane Doe!",
            created_at=datetime.now()
        )

        assert second_post.id == 2
    
        # TODO: Get timeline posts and assert that they are correct
        posts = TimelinePost.select().order_by(TimelinePost.created_at)
        self.assertEqual(posts.count(), 2)

        # Check the older post is John
        earlier_post = posts[0]
        self.assertEqual(earlier_post.name, 'John Doe')
        self.assertEqual(earlier_post.email, 'john.doe@example.com')
        self.assertEqual(earlier_post.content, 'Hello, I am John Doe!')

        recent_post = posts[1]
        self.assertEqual(recent_post.name, 'Jane Doe')
        self.assertEqual(recent_post.email, 'jane.doe@example.com')
        self.assertEqual(recent_post.content, 'Hello, I am Jane Doe!')


