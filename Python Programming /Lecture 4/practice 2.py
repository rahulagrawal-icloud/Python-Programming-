# WAP to enter marks of 3 subjects from user and store in empty dictionary in form fo subject as key and marks as value 

Eng=input("Enter Marks of Eng :-")
Hin=input("Enter Marks of Hindi :-")
Mts=input("Enter Marks of Maths :-")

student={}

student.update({"English" : Eng}) 
student.update({"Hindi" : Hin}) 
student.update({"Maths" : Mts})
print(student)
