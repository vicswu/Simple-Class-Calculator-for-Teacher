'''
Victor Wu 
'''
#Examples of students
#Victor, 173, 10,15,12,12,13,10
#Andrew, 183, 15,20,10,14,9,12
#Vincent, 193, 12,19,10,7,14,12
#Anne,234,20,18,12,10,15,11
#Bob,124,15,18,12,15,15,12
#Greg,134,15,18,12,15,13,12
#Kailong,420,20,20,15,15,15,15

students = []
row=0
intstudent_id_temp=0
total=0
average=0
option=True
grade_list=[]
student_average=0
deviation=0

while option:
#The menu options
    print("\nWelcome to the Teacher’s Simple Class Calculator. Here’s the list of options:")
    print("\n1- Enter student records (Name, ID, and 6 marks separated by commas) or done.")
    print("2- Display the class average.")
    print("3- Display the total grade, letter grade and relation to class average for a given student.")
    print("4- Display a simple bar chart to show grade distribution.")
    print("5- Exit.")
#Select Option
    option=str(input(("\nSelect an option by entering its number or 5 to exit:")))

#Option 1
    if option=="1":
        while option:
            student_records=input("\nEnter Student Record (Separate by commas, no spaces) or done:")
            if student_records=="done":  #To exit option 1
                break
            if student_records.count(",") <7: 
                print("\nThere is not enough data entered. Record Rejected")     #Forces user to input the 8 elements
                break
            if student_records.count(",") >7: 
                print("\nThere is too much data entered. Record Rejected")         #Forces user to input the 8 elements
                break
            student_name, student_id, test1, test2, ass1, ass2, ass3, ass4=student_records.split(",")    #Each element is associated to a variable
            intstudent_id=int(student_id)
            if intstudent_id_temp == intstudent_id:
                print ("\nThis student ID is already present. Record rejected")     #Forces user to input different ID's for each student
                break 
            if intstudent_id<100:
                print("\nThe student ID must be 3 digits.")
                break                                                                                            #Forces user to input valid ID with 3 digits
            if intstudent_id>999:
                print("\nThe student ID must be 3 digits.")
                break
            inttest1=int(test1) 
            inttest2=int(test2)
            if inttest1>20: 
              print ("\nThe grade for test 1 must be between 0 and 20. Record Rejected")      #Restrictions for test grades
              break
            if inttest1<0: 
              print ("The grade for test 1 must be between 0 and 20. Record Rejected")      #Restrictions for test grades
              break
            if inttest2>20:
              print ("\nThe grade for test 2 must be between 0 and 20. Record Rejected")      #Restrictions for test grades
              break
            if inttest2<0: 
              print ("\nThe grade for test 2 must be between 0 and 20. Record Rejected")      #Restrictions for test grades
              break
            intass1=int(ass1) 
            intass2=int(ass2)
            intass3=int(ass3)
            intass4=int(ass4)
            if intass1>15:
              print ("\nThe grade for assignment 1 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass1<0:
              print ("\nThe grade for assignment 1 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass2>15:
              print ("\nThe grade for assignment 2 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass2<0:
              print ("\nThe grade for assignment 2 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass3>15:
              print ("\nThe grade for assignment 3 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass2<0:
              print ("\nThe grade for assignment 3 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass4>15:
              print ("\nThe grade for assignment 4 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            if intass4<0:
              print ("\nThe grade for assignment 4 must be betweem 0 and 15. Record Rejected") #Restrictions for assignment grades
              break
            intstudent_id_temp=intstudent_id
            student_list=[student_name,intstudent_id,inttest1,inttest2,intass1, intass2,intass3,intass4]
            students.append(student_list)   #Creates 2D list
            print ("\nRecord Accepted")

#Option 2
            student_grade=students[row][2]+students[row][3]+students[row][4]+students[row][5]+students[row][6]+students[row][7]    #Calculating overall grade of each student
            total=student_grade+total   #Calculating total of entire class
            average=int(total/(row+1))
            row=row+1
    elif option=="2":
        while option:
            if students==[]:
                print("\nUnable to process Option 2 if students list is empty") #Forces the user to enter the students' report before accessing Option 2
                break
            else:
                print("\nClass Average =", average)
                break

#Option 3
    elif option=="3":
        while option:
            student_search=input("\nEnter the name and ID of the student (Separate by commas, no spaces) or done: ")
            if students==[]:
                print("\nUnable to process Option 3 if students list is empty") #Forces the user to enter the students' report before accessing Option 3
                break
            elif student_search=="done":            #Allows user to exit option 3
                break
            else:
                naminput, idinput = student_search.split(",")
                intidinput=int(idinput)
                for i in range(len(students)):     
                    if naminput in students [i][0] and intidinput == students [i][1]:   #Both equations need to be true 
                        student_average=students[i][2] + students[i][3] + students[i][4] +students[i][5] +students[i][6] +students[i][7]
                        deviation = int(abs(student_average - average))
                    if student_average>86: 
                        grade = "A"
                    elif student_average>74:
                        grade ="B"
                    elif student_average>64:
                        grade ="C"
                    elif student_average<65:
                        grade = "F"
                if (student_average - average)>0:
                    print ("\nGrade for", naminput, "ID=",intidinput,":", student_average, grade, deviation, "points above average")
                elif (student_average - average)<0:
                    print ("\nGrade for", naminput, "ID=",intidinput,":", student_average, grade, deviation, "points below average")

#Option 4
    elif option=="4":
        while option:
            if students==[]:
                print("\nUnable to process Option 4 if students list is empty") #Forces the user to enter the students' report before accessing Option 4
                break
            else:
                print("\nClose the barchart if you want to exit Option 4")    #Informs the user on how to go back to menu
                for i in range(len(students)):
                    student_average=students[i][2] + students[i][3] + students[i][4] +students[i][5] +students[i][6] +students[i][7]
                    if student_average>86: 
                        grade = "A"
                    elif student_average>74:
                        grade ="B"
                    elif student_average>64:
                        grade ="C"
                    elif student_average<65:
                        grade = "F"
                    grade_list.append(grade)
                import numpy as np
                import matplotlib.pyplot as plt
                grades=("A","B","C","F")
                markings=np.arange(len(grades))
                distribution=[grade_list.count("A"), grade_list.count("B"), grade_list.count("C"), grade_list.count("D")]
                plt.bar(markings,distribution,align='center',alpha=0.3)
                plt.xticks(markings,grades)
                plt.title("Student Grade Distribution")
                plt.xlabel("Grades")
                plt.ylabel("Distribution")
                plt.show()
                break                                 #Leave Option 4 when you close the bargraph

#Option 5
    elif option == "5":
        print("\nGoodbye! See you next time!")         #Closes the program
        break

#Other inputs
    else:
        print("\nYou must enter one of the four options. Try again.")     #Restricts the inputs in menu to 1,2,3,4,5
