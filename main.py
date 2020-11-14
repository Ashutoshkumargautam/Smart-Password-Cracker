#!/usr/bin/env python
import time
import sys
import re
import os
#==========================================================================================
#taking first information file location here...
user_input_0 = raw_input("Enter the path of your file: ")
#now taking user own wordlist file location here....
user_input_1 = raw_input("Enter the path of your own wordlist file: ")
#====[user_input[1]]========================================================================================
assert os.path.exists(user_input_0), " [+] I did not find the file at, "+str(user_input_0)
f = open(user_input_0,'r+')
print(" [+] File founded")
f.close()
#====[user_input[2]]========================================================================================
assert os.path.exists(user_input_1), " [+] I did not find the file at, "+str(user_input_1)
f = open(user_input_1,'r+')
print(" [+] File founded")
f.close()
#========[Reading file here[0]]========================================================================
f = open(str(user_input_0),"r+")
print(f.read())
f.close()
#========[Reading file here[1]]========================================================================
f = open(str(user_input_1),"r+")
print(f.read())
f.close()
#==========================================================================================
