#!/usr/bin/env python
import time
import sys
import re
import os
#===[Database of script here]====================================================================================
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = [1,2,3,4,5,6,7,8,9,0]
special = ["~","!","@","#","^","*","(",")","-","+"]
#==================================================================================================================
#taking first information file location here...
user_input_0 = raw_input("Enter the path of your Info.txt file: ")
#now taking user own wordlist file location here....
user_input_1 = raw_input("Enter the path of your own wordlist file: ")
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
#==========================================================================================
