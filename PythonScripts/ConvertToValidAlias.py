# -*- coding: utf-8 -*-


import csv
import os
import re

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
    val = "SET DEFINE OFF;\n"
    return val
    
def createValuesLine(line, num, name):
    val = "INSERT INTO " + name + " VALUES "
    val = val + "('" + str(num) + "','"
    val = val + '\',\''.join(line)
    val = val + "');"
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
    
    print("What is the table name?")
    name = input()
    

    tLines = []
    
    #last inmate alias value: 498913
    currNum = 1

    for line in lines:
        tLines.append(createValuesLine(line, currNum, name))
        currNum += 1
    
    f.write(' \n'.join(tLines))
    f.write('\nSELECT * FROM dual;')
    
