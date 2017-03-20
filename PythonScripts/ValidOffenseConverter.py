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
    
def createValuesLine(line, num, name, isActive):
    #line = removeChar(line)
    
    val = "INTO " + name + " VALUES "
    val =  val + "('" + str(num) + "','"
    val = val + '\'_\''.join(line)
    val = val + "'_'" + isActive + "')" #active offenses
    val = removeInjections(val)
    val = replace(val)
    val = toDate(val)
    if num%50 == 0:
        val = val + "\nSELECT * FROM dual;\n"
        val = val + "SET DEFINE OFF;\n"
        val = val + "\nINSERT ALL"
    return val
        
def replace(line):
    line = re.sub(r' 0:00:00', '', line, flags=re.IGNORECASE)
    return line

def removeInjections(line):
    #line = "'032681','3',11/26/1997 0:00:00,3/19/1999 0:00:00,'HILLSBOROUGH','0000000','DEAL DRGS-1000' SCH/DAYCARE'"
    words = line.split("_")
    
    temp = words[6]
    temp = temp[1:len(temp)-1]
    temp = temp.replace("\'","")
    temp = "\'" + temp + "\'"
    words[6] = temp;
         
    line = ",".join(words)
    return line
    
#382001 last active offense

def toDate(line):
    words = line.split(",")
    words[3] = "TO_DATE(" + words[3] + ",'MM/DD/YYYY')"
    words[4] = "TO_DATE(" + words[4] + ",'MM/DD/YYYY')"
    line = ",".join(words)
    return line


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
    
    print("Active offenses? Y/N")
    isActive = input()
    
    tLines = []
    print("currNum = ?")
    print("1 - Inmate Active Offenses")
    print("382002 - Inmate Inactive Offenses")
    print("675151 -")
    currNum = input()
    currNum = int(currNum)
    for line in lines:
        tLines.append(createValuesLine(line, currNum, name, isActive))
        currNum += 1
    
    f.write(' \n'.join(tLines))