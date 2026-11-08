"""
The "main" function:-

* The main function in python is used as the main boss function which controls the
  flow of other functions in python.

* The main function acts as the anchor for the linked functions.

* Input parameter is changed into the conditioned input parameter of the main function.






"""


def main():
    name = input("what is your name? ")
    hello(name)   # name is an undefined param in hello function.
                  # Yet the function works, as the function is called in the end.
                  # "to" param is changed into the "name"

def hello( to = "world"):
    print(f"Hello, {to}")

main()