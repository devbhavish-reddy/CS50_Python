
class Indus:
    def __init__(self, name):
        self.name = name


class Student(Indus):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


class Teacher(Indus):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


def main():
    stu = Student("Bhavish", "Computer_Sci")
    print(stu.name)
    print(stu.subject)


if __name__ == "__main__":
    main()
