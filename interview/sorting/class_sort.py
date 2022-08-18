class Student:

    def __init__(self, name=None, grade=None):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return "name: {} grade {}".format(self.name, self.grade)

    def __repr__(self):
        return "name: {} grade {}".format(self.name, self.grade)



def main():
    students = [
        Student('A', 4.0),
        Student('B', 3.0),
        Student('C', 2.0),
        Student('D', 3.2),
    ]

    print(sorted(students))
    students.sort(key=lambda student: student.grade, reverse=True)
    print(students)

if __name__ == '__main__':
    main()