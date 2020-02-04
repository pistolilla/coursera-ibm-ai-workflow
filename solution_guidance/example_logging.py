#!/usr/bin/env python
"""
use the iris data to demonstrate how logging is tied to 
a machine learning model to enable performance monitoring
"""

import time,os,re,csv,sys,uuid,joblib
from datetime import date

def _update_predict_log(country,y_pred,y_proba,query,runtime,MODEL_VERSION,test=False):
    """
    update predict log file
    """

    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    logdir = os.path.join("..","logs")
    logfile = os.path.join(logdir, "example-predict-{}-{}.log.csv".format(today.year, today.month))

    ## write the data to a csv file    
    header = ['unique_id','country','timestamp','y_pred','y_proba','target_date','model_version','runtime','test']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if write_header:
            writer.writerow(header)

        to_write = map(str,[uuid.uuid4(),country,time.time(),y_pred,y_proba,query,MODEL_VERSION,runtime,test])
        writer.writerow(to_write)
