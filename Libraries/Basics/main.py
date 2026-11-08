#Library in Python. 

"""
Library vs Module vs Package

    Module: 

        A single file containing Python definitions, functions, classes, 
        and statements intended for reuse.


    Package: 

        A directory containing modules and sub-packages.


    Library: 

        A conceptual collection of reusable code that provides specific functionality to developers.



    











"""

import random # The import keyword is the standrad way of pulling a predefined block of code into our workspace. 

choice = random.choice(["steph", "kyrie"])
print(choice)

 

from random import choice # The from keyword imports a targeted library from a huge scope. Imagine the Random library as your home
                          # folder in your laptop. This ensures to get a specific subfolder inside Desktop or Downloads. 

phone = choice(["Apple", "Samsung", "Google"])
print(phone)



num = random.randint(1,100)
print(num)


 


