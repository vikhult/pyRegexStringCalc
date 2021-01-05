# -*- coding: utf-8 -*-
"""
Reads input strings and partitions them according to
arithmetical rules
"""
# import regex module
import re

class ExprReader():
    def __init__(self, expression=None):
        if expression != None:
            self.expr = expression
        else:
            self.expr = None
        
        self.operators = ['**','*','/','-','+']
        self.decimalSgn = '.'
        # self.separator = ['(',')']
        self.expr = ''
        self.partitions = []
        self.result = 0.0
        
        self.reOper = re.compile('([\+|\-|\*|\/|\*\*]{1,1})')
        # seper = re.compile('(\()\d+[\+|\-|\*|\\|\*\*]\d+(\))')
        self.reSeper = re.compile('(\(+)|(\)+)')
                
        
    def setExpr(self, expression):
        self.expr = expression


    def breakDownExpr(self, expression):
        self.partitions = re.split('\W')
        
        
    def report(self):
        print(self.result)
        
    def calculateExpr(self, expression=None):
        if expression != None:
            self.setExpr(expression)
        if self.expr != None:
            self.partitions = self.reOper.split(self.expr)
            partitionsCp = self.partitions
            for oper in self.operators:
                while oper in partitionsCp:
                    operIndx = partitionsCp.index(oper)
                    a = partitionsCp[operIndx-1]
                    b = partitionsCp[operIndx+1]
                    
                    partitionsCp.pop(operIndx-1)
                    partitionsCp.pop(operIndx-1)
                    partitionsCp[operIndx-1] = arithmetics(
                        int(a),oper,int(b))

            for number in partitionsCp:
                self.result += int(number)
            self.report()
 
def arithmetics(a,operator,b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    elif operator == '**':
        return a**b
    else:
        print("Bad operator")
        return 0
                