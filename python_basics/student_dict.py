students=[]

def add_students(student_name='',student_id=''):
    while True:

        # ask the user to enter the values needed
        student_name = input("Enter the student name to enroll:")
        student_id = int(input("Enter the student Id:"))

        #Appending  values to students list
        students_list = {"Name": student_name, "Student_ID": student_id}
        students.append(students_list)

        # prompt user to continue or not
        prompt = input("if you want to continue (Y/N):")


        if prompt == 'y' or prompt == 'Y':
            continue
        elif prompt == 'n' or 'N':
            break
        else:
            print("Completed enrollment. Here is the list of Students Enrolled")

    print(students)


add_students()
