#encoding:UTF-8

import os
import sys
import numpy as np
import pandas as pd
import redis
import unittest

import tushare
from jaqs.data import DataApi

import turtle

class TurtleTest(unittest.TestCase):
    user_id = ''
    
    def setUp(self):
        self.api = DataApi(addr='tcp://data.tushare.org:8910')
        self.api.login(self.user_id, "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MjY5MDQ0NTgwODAiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTg4MTAyOTkyMDAifQ.M9d07UvpEWVWugga0d2UtbWsRRZubS5mgMXaTxrieSk")
    
    def tearDown(self):
        pass
    
    def test_api(self):
        df, msg = self.api.daily(
            symbol="cu1801.SHF",
            start_date="2017-10-26",
            end_date="2018-11-06",
            fields="",
            adjust_mode="post")
        self.assertEqual(msg, '0,')
        self.assertTupleEqual(df.shape, (57, 16))
    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TurtleTest('test_api'))
    return suite

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('***Must set the user id,\n'
              '***e.g\n'
              '***python turtle_test.py 18812345678')
    else:
        TurtleTest.user_id = sys.argv.pop()
    unittest.main(defaultTest='suite')
