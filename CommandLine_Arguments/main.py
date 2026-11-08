"""
Command line Arguments: 
    Arguments passed through the command line interface while running the python program. These arguemts
    alter the way in which our program was orgianlly supposed to work. 



"""

# Sys Library

import sys 

a = sys.argv[1]  # Sys ARGV stands for System argument vector. 

# Prints out the list of arguments passed in the command line after python. I deliberately modified the list index to 1. 


print("My name is", a )

if len(sys.argv) < 2:
    print("Few arguments entered")

for name in sys.argv[1:]: #Sliced list in python. Modifyihng the list structure can be done with brackets and list modyfication number. 
    print("Hello, ", name )


import cowsay

if len(sys.argv) == 2: 

    cowsay.trex("hello, " + sys.argv[1]) # Prints a dino saying Hi!