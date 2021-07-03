# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:43:52 2021

@author: Rashmikant
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())