# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:06:35 2017

@author: Alex
"""

import csv
import os
    
def getLines(filePath):
    rows = []
    with open(filePath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\'')
        for row in reader:
            rows.append(row)
    return rows
    
def readLines(arr):
    for line in arr:
        print(line)
        
def createHeaderInsertLine():
    val = "INSERT INTO "
    print(val)
    ap = input()
    val = val + ap + " VALUES "
    return val
    
def createValuesLine(line, num):
    val = "('" + str(num) + "',"
    val = val + '\',\''.join(line)
    val = val + "')"
    return val
        

def main():
    print("Please enter the filepath of the file you would like to transform")
    filepath = input()
    #filepath = 'INMATE_ACTIVE_ALIASES.csv'
    lines = getLines(filepath)
    
    print("What is the name of the file that you would like to produce?")
    targetfile = input()
    f = open(targetfile, 'w')
    f.write(createHeaderInsertLine())
    
    tLines = []
    currNum = 1
    for line in lines:
        tLines.append(createValuesLine(line, currNum))
        currNum += 1
    
    f.write(', \n'.join(tLines))
    
    