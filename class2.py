class Student:
    def __init__(self, name, family, id):
        self.name = name
        self.family = family
        self.id = id
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        return sum(self.grades)/len(self.grades)

    def show(self):
        print(self.id, self.name, self.family, self.grades)

l = []
for i in range(1, 6):
    print(f"________________ person {i} ____________________")
    s = Student(input('Enter id: '), input('Enter name: '),
                input('Enter family: '))
    g1 = float(input('Enter grade:'))
    g2 = float(input('Enter grade:'))
    s.add_grade(g1)
    s.add_grade(g2)
    l.append(s)

print(l)
max_average = l[0].average()
best = l[0]
for s in l :
    s.show()
    if s.average() > max_average:
        max_average = s.average()
        best = s

print("\n\nBest person with average : ")
best.show()
print(max_average)
