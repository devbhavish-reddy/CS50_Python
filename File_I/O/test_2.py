for f in range(8): 
    n = input("name: ")
    with open("names.txt", "a" ) as file: # This way, we dont need to close any files, the function gets called autmoatically. 
        file.write(f"{n} \n")  #File is closed after the code moves away from the intendation. 


names = []

with open("names.txt", "r") as file: 
    for line in file: 
        names.append(line.rstrip)  #Sorting 


for name in sorted(names, reverse=True): #Reverse = true, flips the order of the coming of the names. 
    print(f"Hello, {name}" )

















