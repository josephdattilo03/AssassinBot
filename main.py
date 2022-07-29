from tkinter import *
import smtplib
import ssl
import random
import re

rawList = []
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
print("""

      _                     _      
     /_\   ________ _ _____(_)_ _  
    / _ \ (_-<_-< _` (_-<_-< | ' \ 
   /_/ \_\/__/__|__,_/__/__/_|_||_|
   """)
print("Welcome to the Dattilo Assassin Launcher, please enter all contestant emails. Type 'start' to"
      " begin the game and "
      "'quit' to exit the application.")
print("")
print("Please make sure that you are connected to the internet. If the application "
      "quits unexpectedly, that is most likely the issue.")
print("")


class Student:
    gmail = ""
    rawName = ""
    name = ""

    def __init__(self, gmail):
        self.gmail = gmail
        for char in self.gmail:
            if char.isdigit():
                break
            self.rawName = self.rawName + char
        self.name = self.rawName.replace(".", " ")


def createStudentList(designatedList):
    studentList = []
    for y in designatedList:
        currStudent = Student(y)
        studentList.append(currStudent)
    return studentList


def startGame(designatedList):
    gmail = ""
    gmailPass = ""
    while (True):
        gmail = input("Please enter a valid email that the program will use to send the assignment emails: ")
        exitAns = input("is the email correct? Please enter yes or no: ")
        if exitAns.upper() == "YES":
            break
    while (True):
        gmailPass = input("Please enter your password: ")
        exitAns = input("is the password correct? Please enter yes or no: ")
        if exitAns.upper() == "YES":
            break
    assassinList = createStudentList(designatedList)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    print(gmail + gmailPass)
    server.login(gmail, gmailPass)
    currAssassin = random.choice(assassinList)
    firstAssassin = currAssassin
    while len(assassinList) >= 2:
        assassinList.remove(currAssassin)
        currTarget = random.choice(assassinList)
        print(currAssassin.name.upper() + ": target received: " + currTarget.name)
        message = """From: MBA Assassin Bot <mbassassingame@gmail.com>
    To: """ + currAssassin.name + """ <""" + currAssassin.gmail + """>
Subject: Let the Hunt Begin
Dear """ + currAssassin.name.upper() + """, 

Congratulations, you have been elected to participate in a contest of champions against your fellow classmates. at the end of this transmission you will receive a target, who you have been contracted to eliminate as quickly and efficiently as possible (for details please refer to the rules provided by your class officers). Be wary in your travels, as you will most certainly be pursued yourself. 

    Your target is: """ + currTarget.name.upper() + """


    Best of luck
 
    
                                  
   / \   ___ ___  __   __  __(_)_ 
  / _ \ / __/ __|/ _` / __/ __| | '_ \          
 / ___ \\__ \__ \ (_| \__ \__ \ | | | |            
/_/   \_\___/___/\__,|___/___/_|_|                              
Bot created by Joseph Dattilo

           
    """
        server.sendmail("mbassassingame@gmail.com", currAssassin.gmail, message)
        currAssassin = currTarget
    currTarget = firstAssassin
    server.sendmail("mbassassingame@gmail.com", currAssassin.gmail, message)
    print(currAssassin.name.upper() + ": target received: " + firstAssassin.name)
    # server.quit()


while True:
    usrInput = input("Input Command:")
    if usrInput.upper() == "QUIT":
        print("quitting")
        break
    if usrInput.upper() == "START":
        print("starting")
        startGame(rawList)
        input("Program finished, press enter to quit.")
        break
    if re.fullmatch(regex, usrInput):
        rawList.append(usrInput.lower())
    else:
        print("Value was not a proper email address.")