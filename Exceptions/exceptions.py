"""
Exceptions

There can be various ways in which our code can break, we call these bugs exceptions to our 
code. 

Errors: 

1. Syntax: 

        The langauge of the code just goes wrong, u might have missed a bracket or just messed
        up with a semi colon. Fix the grammer and your good to go. 

2. Run Time: 

        Explicit errors in logic, while it does not seem as obivious as a syntax error, it can
        do enough damage, infact at times even more. 

        Simple logical and thought based errors often are the most damage causing Run-time erors. 



"""


# Syntax error: 

# name = input("Enter your Name), a closing paranthesis causes the syntax error. 


# Runtime Error: 

num = int(input("enter your num: "))  #If the user prompts in with a stirng, a value eror occurs, which is a Run time error.
print(f"Users num is {num}")

# Preventing Run-Time Errors. 

def input_number(): 

    while True: 

        try: 
            num1 = int(input("Num: "))             
            print("Num is", num1)
            break

        except ValueError: 
            print("N is not an integer.")

input_number()
"""
A Run-time error can be combated with the typical try and except format. This is essentialy
just a mathematical function, where there are certain limitations for the domain and range. 

During Run_Time, the script does not crash, instead it justs throws back a message at the user
to be more cautious. 
"""



"""
3. Name Error
    When a variable is not defined or the spelling of the variable which the code is reffering to 
    is spelled wrong. 
 Note: Name error is part of a logical error. It comes under a Run-Time Error. 

"""

# Solving a Run-Time Error. 

while True:  

    try: 
        marks = int(input("Marks: "))
        

    except ValueError or NameError: 
        print("Marks need to be integer")


    else: 
        break

print(f"Marks are {marks}")


#Pass
"""
The pass keyword in python, enables to just skip a command in python, for example to just prompt back to something
important. 


A real life analogy: 
    At the end of a math class, when the teacher asks u if u have any doubts u choose to skip. The question passes on to the next child. This delibrate choice of skiiping the sequecne is known as pass. 

"""

def name_nba():
    while True: 
        try: 
            name = input("Enter Player Name: ")
            return name
            break

        except ValueError: 
            pass

print(f"Name of the player is", name_nba())

# Raise Keyword

"""
A raise keyword in python, lets the programmer to manally raise an exception to the code. In simple words, it stops the execution
of the code and throws in a message/error.
"""

def number_input(prompt): 
    while True: 
        
        num_8 = int(input(prompt))
        return num_8
        break

        if num_8 < 0: 
            raise ValueError

print("Your Natural Number is: ", number_input("Enter Your Natural Number: "))




                        






