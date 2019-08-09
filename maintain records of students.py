total_num_of_students = int(input("enter total number of students:"))
print ("you entered %s students" %total_num_of_students)
student_info = {}
student_data = [ 'rollno', 'age', 'gender']
for i in range(0,total_num_of_students):
    student_name = input("Name :")
    student_info[student_name] = {}
    for j in student_data:
        student_info[student_name][j] = input(j)
name = input("to find info enter valid student name")
if name in student_info.keys():
    print (student_info[student_name])
else:
    print("please enter valid name")


    


