student_grade=[]
student_grade.append((1,"ankitha"))
student_grade.append((4,"yoch"))
student_grade.sort(reverse=True)
print("True")
print(student_grade)
student_grade.append((3,"gayathri"))
student_grade.sort(reverse=True)
student_grade.append((5,"asha"))
student_grade.sort(reverse=True)
print("priority wise sorted")
print(student_grade)
print("original queue")
while student_grade:
    print(student_grade.pop())