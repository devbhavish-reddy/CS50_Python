"""
The main code is tested with an exisiting another test file adjcent to it in the same directory.
It involves new techniques, such as assert. 
 

Unit tests: 
    Tests for functions which we have written in our code. 
    
"""

def main(): 
    n = int(input("Enter a non zero positive integer: "))
    square(n)

def square(m):
    return m * m


if __name__ == "__main__": 
    main()
