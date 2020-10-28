# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:51:26 2020

@author: SM51998
"""

from PyPDF2 import PdfFileReader

#opening the pdf file in a read binary mode
file = open('SQL.pdf','rb')

reader = PdfFileReader(file)

#print(reader.getDocumentInfo())

print("''''''''''''''''''''''''''''''''''''")
print()
print("Number of pages : ",reader.getNumPages())

print("PDF fiel created by : ",reader.getDocumentInfo().creator)

print("''''''''''''''''''''''''''''''''''''")
pages = reader.getNumPages()
for i in range(0,pages):
    print("Page Number : ",i+1)
    print("----------------------------------")
    pageObj = reader.getPage(i)
    print(pageObj.extractText())
    print("---------------------------------")
    
file.close()