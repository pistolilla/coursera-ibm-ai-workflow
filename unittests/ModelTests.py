#!/usr/bin/env python
"""
model tests
"""


import unittest,os,sys,random
## import model specific functions and variables
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)
from solution_guidance.model import *

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        data_dir = os.path.join(PARENT_DIR,"cs-train")
        model_train(data_dir,test=True,regressor="randomforest")
        models = [f for f in os.listdir(MODEL_DIR) if re.search("test",f)]
        #print(models)
        self.assertTrue(len(models) >=  2)

    def test_02_load(self):
        """
        test the load functionality
        """
                        
        ## load the model
        all_models = model_load_only()
        models_loaded = list(all_models.keys())
        models_indir = [f for f in os.listdir(MODEL_DIR) if re.search("sl",f)]
        # were all models loaded?
        self.assertTrue(len(models_loaded) == len(models_indir))

        # take a random model and ensure it has methods
        model = all_models[random.choice(models_loaded)]
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

    def test_03_predict(self):
        """
        test the predict functionality
        """
        ## example predict
        country='all'
        year='2018'
        month='01'
        day='05'
        result = model_predict(country,year,month,day,test=True)
        print(result)
        self.assertTrue(180000 <= result['y_pred'][0] <= 200000)

        
### Run the tests
if __name__ == '__main__':
    unittest.main()
