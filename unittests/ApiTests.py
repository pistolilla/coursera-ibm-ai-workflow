#!/usr/bin/env python
"""
api tests

these tests use the requests package however similar requests can be made with curl

e.g.

data = '{"key":"value"}'
curl -X POST -H "Content-Type: application/json" -d "%s" http://localhost:8080/predict'%(data)
"""

import sys
import os
import unittest
import requests, json
import re
from ast import literal_eval
import numpy as np

# Ensuring consistency among modules
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)
from app import HOST, PORT
server = HOST
port = PORT

try:
    requests.post('http://{}:{}/predict'.format(server, port))
    server_available = True
except:
    server_available = False
    
## test class for the main window function
class ApiTest(unittest.TestCase):
    """
    test the essential functionality
    """
    
    @unittest.skipUnless(server_available,"local server is not running")
    def test_predict_badrequest(self):
        """
        ensure appropriate failure types
        """
    
        ## provide no data at all 
        r = requests.get('http://{}:{}/predict'.format(server, port))
        self.assertTrue(int(r.status_code) == 400)
        self.assertEqual(re.sub('\n|"','',r.text),"[]")

        ## provide improperly formatted data
        r = requests.get('http://{}:{}/predict?target_date={}'.format(server, port, "06-30-2019"))
        self.assertTrue(int(r.status_code) == 400)
        self.assertEqual(re.sub('\n|"','',r.text),"[]")

        ## provide target_date not in range (2017-11-29,2019-06-30)
        r = requests.get('http://{}:{}/predict?target_date={}'.format(server, port, "2015-03-02"))
        self.assertTrue(int(r.status_code) == 400)
        self.assertEqual(re.sub('\n|"','',r.text),"[]")
    
    @unittest.skipUnless(server_available,"local server is not running")
    def test_predict(self):
        """
        test the predict functionality
        """
      
        r = requests.get('http://{}:{}/predict?target_date={}'.format(server, port, "2018-02-17"))
        txt = r.text
        response = json.loads(txt)
        self.assertTrue(int(r.status_code) == 200)
        self.assertTrue(160000 < response['y_pred'][0] < 200000)

    @unittest.skipUnless(server_available,"local server is not running")
    def test_train(self):
        """
        test the train functionality
        """
      
        request_json = {'mode':'test'}
        r = requests.get('http://{}:{}/train?regressor={}'.format(server, port, "randomforest"))
        self.assertTrue(int(r.status_code) == 200)
        self.assertTrue('true' in r.text)

### Run the tests
if __name__ == '__main__':
    unittest.main()
