class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, age, height, weight):
        self.students.append(Student(age, height, weight))
    
    def avg_age(self):
        return sum(s.age for s in self.students) / len(self.students) if self.students else 0.0
    
    def avg_height(self):
        return sum(s.height for s in self.students) / len(self.students) if self.students else 0.0
    
    def avg_weight(self):
        return sum(s.weight for s in self.students) / len(self.students) if self.students else 0.0

# ورودی کلاس A
n_a = int(input("smt: "))
class_a = ClassRoom("A")
ages_a = list(map(int, input().split()))
heights_a = list(map(int, input().split()))
weights_a = list(map(int, input().split()))

for i in range(n_a):
    class_a.add_student(ages_a[i], heights_a[i], weights_a[i])

# ورودی کلاس B
n_b = int(input("smt:  "))
class_b = ClassRoom("B")
ages_b = list(map(int, input().split()))
heights_b = list(map(int, input().split()))
weights_b = list(map(int, input().split()))

for i in range(n_b):
    class_b.add_student(ages_b[i], heights_b[i], weights_b[i])

# چاپ میانگین‌ها
print(f"{class_a.avg_age():.1f}")
print(f"{class_a.avg_height():.1f}")
print(f"{class_a.avg_weight():.1f}")
print(f"{class_b.avg_age():.1f}")
print(f"{class_b.avg_height():.1f}")
print(f"{class_b.avg_weight():.1f}")

# مقایسه
if class_a.avg_height() > class_b.avg_height():
    print("A")
elif class_b.avg_height() > class_a.avg_height():
    print("B")
else:
    if class_a.avg_weight() < class_b.avg_weight():
        print("A")
    elif class_b.avg_weight() < class_a.avg_weight():
        print("B")
    else:
        print("Same")
