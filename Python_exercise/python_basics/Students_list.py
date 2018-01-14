students=[]
def add_students():
    while True:
        list=input("Enter the student name to enroll:")
        students.append(list)
        prompt=input("if you want to continue (Y/N):")
        if prompt=='y' or prompt=='Y':
            continue
        elif prompt=='n' or 'N':
            break
    print(students)
add_students()
