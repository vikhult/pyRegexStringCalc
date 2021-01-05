# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:33:51 2021

@author: mrsup
"""
from ExprReader import ExprReader

if __name__ == '__main__':
    myReader = ExprReader()
    myReader.calculateExpr("3*7+7*8*3")
    ans = myReader.result