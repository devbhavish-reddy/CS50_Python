def main(): 
    student = get_students()
    print(f"Name is {student["name"] }, {student["grade"]} ")
    




def get_students():
    
    while True: 
        try: 
            grade = int(input("Enter Grade: "))
            name = input("Enter Name: ")
            break

        except ValueError: 
            print("Data criteria not met.")

    
    students = {"name": name, "grade": grade}
    return students

if __name__ == "__main__": 
    main()


