students={}

def add_students():
    count = 0
    while True:
        student_names=input("Enter the student name to enroll:")
        count+=1
        student_id=count
        students[list]=student_id
        prompt=input("if you want to continue (Y/N):")
        if prompt=='y' or prompt=='Y':
            continue
        elif prompt=='n' or 'N':
            break
    print(students.items())
add_students()
