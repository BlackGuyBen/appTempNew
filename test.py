#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
        self.expected = ['','','','','','','','','','']

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        
    def test_temp10(self):
        self.assertEqual(app.temp10(), self.expected)
        
    def test_recent_temps(self):
        tv = self.app.get('/recent_temps')
        self.assertEqual(tv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
