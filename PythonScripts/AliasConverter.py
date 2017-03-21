# -*- coding: utf-8 -*-


import csv
import os
import re

def getLines(filePath):
    rows = []
    with open(filePath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='_', quotechar='\'')
        for row in reader:
            rows.append(row)
    return rows
    
def readLines(arr):
    for line in arr:
        print(line)
        
def createHeaderInsertLine():
    val = "SET DEFINE OFF;\n"
    val = val + "INSERT ALL\n"
    return val
    
def createValuesLine(line, num, name):
    val = "INTO " + name + " VALUES "
    val = val + "('" + str(num) + "','"
    val = val + '\',\''.join(line)
    val = val + "')"
    if num%50 == 0:
        val = val + "\nSELECT * FROM dual;"
        val = val + "\nSET DEFINE OFF;"
        val = val + "\nINSERT ALL\n"
        
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
    print("currNum = ?")
    print("last inmate alias value: 498913")
    currNum = int(input())
    

    for line in lines:
        tLines.append(createValuesLine(line, currNum, name))
        currNum += 1
    
    f.write(' \n'.join(tLines))
    f.write("SELECT * FROM dual;")

    
