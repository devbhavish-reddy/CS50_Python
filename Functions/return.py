# "Return" keyword in python

"""
The return keyword in python is used to exit the function and to send a specific
data back to the caller.


"""


def main():
    n = float(input("Enter a number:  "))
    print("Sqaure of number is", sqaure(n))

def sqaure(n):
    return n * n  # Ends the function here and gives the value when the function is called.




main()











