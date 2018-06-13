#encoding:UTF-8

import os
import numpy as np
import pandas as pd
import redis
import unittest

import tushare
from jaqs.data import DataApi

import turtle

class TurtleTest(unittest.TestCase):
    
    def setUp(self):
        api = DataApi(addr='tcp://data.tushare.org:8910')
        api.login("1881~", "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MjY5MDQ0NTgwODAiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTg4MTAyOTkyMDAifQ.M9d07UvpEWVWugga0d2UtbWsRRZubS5mgMXaTxrieSk")
    
    def tearDown(self):
        pass
    
    def test_0(self):
        pass
    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TurtleTest('test_0'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
