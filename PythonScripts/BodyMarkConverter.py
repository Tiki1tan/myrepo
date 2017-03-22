# -*- coding: utf-8 -*-
#set delimiters to _

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
    val = val + "\nINSERT ALL\n"
    return val
    
def createValuesLine(line, num, name):
    #line = removeChar(line)
    
    val = "INTO " + name + " VALUES "
    val =  val + "('" + str(num) + "','"
    val = val + '\',\''.join(line)
    val = val + "')" #active offenses
    if num%50 == 0:
        val = val + "\nSELECT * FROM dual;\n"
        val = val + "SET DEFINE OFF;\n"
        val = val + "\nINSERT ALL"
    return val
        


def main():
    print("Please enter the filepath of the file you would like to transform")
    filepath = input()
    lines = getLines(filepath)
    
    print("What is the name of the file that you would like to produce?")
    targetfile = input()
    f = open(targetfile, 'w')
    f.write(createHeaderInsertLine())
    
    print("What is the table name?")
    name = input()

    tLines = []
    print("currNum = ?")
    print("last inmate body_mark num: 383991")
    currNum = input()
    currNum = int(currNum)
    for line in lines:
        tLines.append(createValuesLine(line, currNum, name))
        currNum += 1
    
    f.write(' \n'.join(tLines))
    print("Remove backslashes from the file manually\n")
    print("Backslashes will be located in the description")
    
