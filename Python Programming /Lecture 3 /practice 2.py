# WAP to check the list contains the palindrome of elements or not 
d1=input("Enter first Element :-")
d2=input("Enter second Element :-")
d3=input("Enter third Element :-")
d4=input("Enter fourth Element :-")
d5=input("Enter fifth Element :-")

l1=[d1,d2,d3,d4,d5]

l2=l1.copy()
l1.reverse()

if(l1==l2):
    print("The list contains palindrome of elements")
else:
    print("The list does not contains palindrome of elements")