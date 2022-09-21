# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:43 2022
save to a C drive location to make it faster and avoid the "already exists repladce yes/no question on each download"
The weekly download list contains mostly reports we already have that need to be overwritten for some reason

This is python 3 code written and run in Spyder 

in chrome:
    settings, advanced, set download directory
    make it so PDFS dont auto open in bluebeam
    highlight red text with file name - EDITED 9/20/22 script will auto populate file name into clipboard
    control+c - EDITED 9/20/22 script will auto populate file name into clipboard
    click pdf download button - EDITED 9/20/22 script will auto click this button in a full screen chrome window
    control+v
    save
    
Sleep times are used to give the web page time to load before clicking the download button and to pause for manual interaction; 
    at home on google fiber a sleep time of 3 seconds is sufficient
    at work an intial sleep time of 5 or more seconds is needed, sometimes pages take 10 seconds or more

you can also add a breakpoint in the for loop and step through each one individually in debug mode, setting sleep time to 1 or 0

some files reference 2011 or older crashes that cant be queried in the TRS

copy downloaded files to \\citydata\public\MSO_Engr\KDOT\CrashReports

log into TRS at https://portal.kstrs.org/private/SimpleSearch.aspx

@author: kgonterwitz
"""

import webbrowser
#import pdfkit
from time import sleep
import pyperclip
import ctypes

ws = r'//citydata/public/MSO_Engr/KDOT/CrashReports/'
#move the list local while hte VPN is down
ws = r'C:/Users/kgonterwitz/Downloads/crashdownload20220726/'
download_folder = r'C:/Users/kgonterwitz/Downloads/crashdownload20220726'

#start a counter to print and match to text file line numbers
#open list in notepad ++ and turn on row numbers
#if a file isnt downloaded in time it can be quickly retrieved from the TRS url
index = 0

text_file = ws+"DISTINCT_LIST.txt"
#text_file = ws+"KDOTtest.txt"
from numpy import loadtxt
lines = loadtxt(text_file, dtype=str, comments="#", delimiter=" | ", unpack=False)

def click():
    ctypes.windll.user32.SetCursorPos(1805, 83)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

for line in lines:
    index +=1
    file_name = str((line[0:1]))[2:13]+".pdf"
    print(str(index)+" "+str(file_name))
    pyperclip.copy(file_name)
    url = "https://portal.kstrs.org/private/PDF.aspx?itemID="+str((line[1:2]))[2:10]+"&VerNbr=1&rType=PDF&rSource=AccidentLib"
    webbrowser.open(url, new=0, autoraise=True)
    sleep(2.5)
    click()
    sleep(1)
    #pyperclip.paste()
    sleep(0.5)

