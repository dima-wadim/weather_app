import unittest
from app import create_app, db
from app.models import SearchHistory
from datetime import datetime

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/weather_app_test'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_history_endpoint(self):
        with self.app.app_context():
            new_search = SearchHistory(city="New York", timestamp=datetime.utcnow())
            db.session.add(new_search)
            db.session.commit()

        response = self.client.get('/history')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['city'], 'New York')

if __name__ == '__main__':
    unittest.main()
