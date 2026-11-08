def main():

    c = int(input("Enter your Value:  "))
    if c_even(c):
        print("Even")

    else:
        print("Odd")


def c_even(n):
    if n % 2 == 0:
        return True # True is a boolean date type, this kind only has either true or false
                    # True refers to "1" in the machine language.



    else:
        return False # False refers to "0" in the machine language.

    """
    The whole idea of the conditional statement is to check whether something is 
    true or false, with directly prompting with the boolean value, the conditional
    executes the statement with even less effort. 
    """





main()


