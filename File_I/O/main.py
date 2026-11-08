"""
File I/O: 
    Refers to the managamnt of the memory used in a program to access it thorugh a file without
    it getting deleted after the program executes. 

    The data produced while the program runs is ensured to be saved using File I/O.



"""

names = "bhavish" # Empty list

for n in range(3): 
    names.append(input("Name: "))

for name in sorted(names): 
    print(f"Hello, {name}")

with open("names.txt", "a") as file:
     # w is write, a is append, r stands for read. The second param can be replaced based on the requirement. 
    file.write(names)


