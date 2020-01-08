"""
Victor Wu 1731253
420-LCU Computer Programming, Section 2
S. Hilal
Assignment 3
"""

class Student:  #Create class
    'Base class for all students' 
    Count = 0   

    def __init__(self,stname,stid, t1, t2, a1, a2, a3, a4): 
        self.name = stname
        self.id = stid
        self.t1 = t1
        self.t2 = t2
        self.a1= a1
        self.a2= a2
        self.a3= a3
        self.a4= a4
        self.grade = int(t1)+int(t2)+int(a1)+int(a2)+int(a3)+int(a4) #calculate total grade
        if self.grade > 86: #associate grade to student 
            grade = "A"
        elif self.grade>74:
            grade ="B"
        elif self.grade>64:
            grade ="C"
        elif self.grade<65:
            grade = "F"
        self.lg = grade
        Student.Count += 1

    def get_letter_grade(self):
        return (self.lg)

    def __del__(self):
        Student.Count -= 1
        print ("Deleting Student instance!")

    def __eq__(self,student):
        return (self.id == student.id)

    def __repr__(self):
        return("{} {} {} {} {} {} {} {} {} {}".format(self.name,self.id,self.grade,self.lg,self.t1,self.t2,self.a1,self.a2,self.a3,self.a4))

    def update_grade (self, which_grade,new_grade):
        if which_grade == 't1':
            self.t1 = int(new_grade)
        if which_grade == 't2':
            self.t2 = int(new_grade)
        if which_grade == 'a1':
            self.a1 = int(new_grade)
        if which_grade == 'a2':
            self.a2 = int(new_grade)
        if which_grade == 'a3':
            self.a3 = int(new_grade)
        if which_grade == 'a4':
            self.a4 = int(new_grade)
        
    def displayStudentInfo(self):
        txt = "Name:{} ID:{} Grade:{}"
        print(txt.format(self.name,self.id,self.grade,self.lg,self.t1,self.t2,self.a1,self.a2,self.a3,self.a4))

students_list = []
option=True

while option: #keep going until not true
#menu options
    #The menu options
    print("\nWelcome to the Teacher’s Simple Class Calculator. Here’s the list of options:")
    print("\n1- Read and process all students’ records")
    print("2- Display all student records including total and letter grades and class average")
    print("3- Display the complete record of a particular student")
    print("4- Update a student's grade")
    print("5- Display a list of all students who achieved a particular letter grade")
    print("6- Exit")
#Select Option
    option=input("\nSelect an option by entering its number or 6 to exit:")

#Option 1
    if option=="1":
        fp = open('students.txt')   #open document
        lines = fp.readlines()
        for line in lines: # keep reading
            if not line:
                break
            line=line.strip("\n") # remove newline
            record= line.split(",")
            s= Student (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]) #assign values to attributes from class
            students_list.append(s) #add objects to list 
        fp.close()

#Option 2        
    elif option=="2":
        while option:
            if students_list==[]:
                print ("\nNo Data. Please Initiate with option 1")   #Forces the user to enter the students' report before accessing Option 2
                break
            else:
                for i in students_list: 
                        print ("\n",i) #print objects in list
                gtot=0
                n=0
                for s in students_list:
                    gtot += s.grade #calculate total grade using for loop that checks grade for each object 
                    n +=1
                average = gtot/n #calculate average
                print("\nThe average is", average)
                break
            
#Option 3        
    elif option=="3":
        while option:
            if students_list == []: #check if list empty
                    print ("\nNo Data. Please Initiate with option 1") #Forces the user to enter the students' report before accessing Option 3
                    break
            student_records = input("Enter Student name and id (Separate by commas, no spaces) or done: ") #ask user to input their search
            if student_records=="done":
                break   #allows user to exit 
            else:
                naminput, idinput = student_records.split(",")
                for s in students_list: #for loop to search all objects in list
                    if (s.name == naminput) and (s.id == idinput): #check for which index name and id match
                        print (s.name,s.id,s.grade, s.lg, s.t1,s.t2, s.a1, s.a2, s.a3, s.a4)
                        break
                    else:
                        continue    #skip object if name and id do not match
                
#Option 4
    elif option=="4":
        while option:
            if students_list == []: #check if list empty
                    print ("\nNo Data. Please Initiate with option 1")  #Forces the user to enter the students' report before accessing Option 4
                    break
            student_update = input("\nEnter the Student name and id of the student whose grades you want to update (Separate by commas, no spaces) or done: ") #ask user to input their search
            if student_update=="done":
                break     #allows user to exit
            else:
                naminput, idinput = student_update.split(",")
                for s in students_list: #for loop to search all objects in list
                    if (s.name == naminput) and (s.id == idinput): #check for which index name and id match
                        update=input("\nEnter the grade you want to update (t1,t2,a1,a2,a3,a4) and the new grade (Seperate by commas, no spaces):")
                        which_grade, new_grade = update.split(",")
                        if which_grade == 't1':
                            if int(new_grade)<21 and int(new_grade)>(-1):    #force user to enter a grade on 20 for t1
                                s.t1 = int(new_grade)
                            else:
                                print("\nYou must enter a valid test grade")
                        elif which_grade == 't2':
                            if int(new_grade)<21 and int(new_grade)>(-1):    #force user to enter a grade on 20 for t2
                                s.t2 = int(new_grade)
                            else:
                                print("\nYou must enter a valid test grade")
                        elif which_grade == 'a1':
                            if int(new_grade)<16 and int(new_grade)>(-1):    #force user to enter a grade on 15 for a1
                                s.a1 = int(new_grade)
                            else:
                                print("\nYou must enter a valid test grade")
                        elif which_grade == 'a2':
                            if int(new_grade)<16 and int(new_grade)>(-1):     #force user to enter a grade on 15 for a2
                                s.a2 = int(new_grade)
                            else:
                                print("\nYou must enter a valid test grade")
                        elif which_grade == 'a3':
                            if int(new_grade)<16 and int(new_grade)>(-1):    #force user to enter a grade on 15 for a3
                                s.a3 = int(new_grade)
                            else:
                                print("\nYou must enter a valid test grade")
                        elif which_grade == 'a4':
                            if int(new_grade)<16 and int(new_grade)>(-1):    #force user to enter a grade on 15 for a4
                                s.a4 = int(new_grade)
                            else:
                                print("\nYou must enter a valid test grade")    
                        else:
                            print("\nYou must enter a valid test or assignment")
                
#Option 5            
    elif option == "5":
        while option:
            if students_list == []: #check if list empty
                    print ("\nNo Data. Please Initiate with option 1")  #Forces the user to enter the students' report before accessing Option 5
                    break
            letter_grade = input("Enter a letter grade or done: ") #ask user to input their search
            if letter_grade=="done":
                break   #allows user to exit
            else:
                a=0
                a_list=[]
                b=0
                b_list=[]
                c=0
                c_list=[]
                f=0
                f_list=[]
                for s in students_list: #calculate count of grade using for loop that checks letter grade for each object
                    if s.lg is "A":
                        a +=1
                        a_list+=str(s.name)    #add name to list of students with A
                        a_list+=", "
                    if s.lg is "B":
                        b +=1
                        b_list+=str(s.name)   #add name to list of students with B
                        b_list+=", "
                    if s.lg is "C":
                        c +=1
                        c_list+=str(s.name)   #add name to list of students with C
                        c_list+=", "
                    if s.lg is "F":
                        f +=1
                        f_list+=str(s.name)   #add name to list of students with F
                        f_list+=", "
                A = str("".join(a_list))  #turn list into string
                B = str("".join(b_list))  #turn list into string
                C = str("".join(c_list))  #turn list into string
                F = str("".join(f_list))  #turn list into string
        
            print("\nHere is the Distribution of grades: \n",a,"students got an A","\n",b,"students got a B","\n",c,"students got a C","\n",f,"students got a F")
            if letter_grade=="A":
                print("\nHere is the list of students who got an A:",A)
            elif letter_grade=="B":
                print("\nHere is the list of students who got an B:",B)
            elif letter_grade=="C":
                print("\nHere is the list of students who got an C:",C)
            elif letter_grade=="F":
                print("\nHere is the list of students who got an F:",F)
            else:
                print("\nYou must enter a valid letter grade")

#Option 6
    elif option=="6":    #stop program
        print("\nGoodbye! See you next time!")
        break

#If input is not one of the 6 options
    else:
          print("\nYou must enter one of the six options. Try again")
