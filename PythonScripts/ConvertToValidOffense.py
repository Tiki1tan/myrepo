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
    val = "INSERT ALL \n"
    return val
    
def createValuesLine(line, num, name, isActive):
    val = "INTO " + name + " VALUES "
    val =  val + "('" + str(num) + "','"
    val = val + '\',\''.join(line)
    val = val + "','" + isActive + "')" #active offenses
    val = replace(val)
    val = toDate(val)
    return val
        
def replace(line):
    line = re.sub(r' 0:00:00', '', line, flags=re.IGNORECASE)
    return line

#382001 last active offense

def toDate(line):
    words = line.split(",")
    words[3] = "TO_DATE(" + words[3] + ",'MM/DD/YYYY')"
    words[4] = "TO_DATE(" + words[4] + ",'MM/DD/YYYY')"
    line = ",".join(words)
    return line

def test():
    s = "INSERT INTO offense VALUES ('1','000371','1','3/16/1970','3/16/1970','ORANGE','0200000','SEXUAL BATTERY UNSPECIFIED',Y)"
    words = s.split(",")
    #test = ",".join(words)

    words[3] = "TO_DATE(" + words[3] + ",'MM/DD/YYYY')"
    words[4] = "TO_DATE(" + words[4] + ",'MM/DD/YYYY')"
    test = ",".join(words)
    return test

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
    
    print("Active offenses? Y/N")
    isActive = input()
    
    tLines = []
    currNum = 382002
    for line in lines:
        tLines.append(createValuesLine(line, currNum, name, isActive))
        currNum += 1
    
    f.write(' \n'.join(tLines))
    f.write('\nSELECT * FROM dual;')
    