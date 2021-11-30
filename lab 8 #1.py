#Max Huynh
#11/29/21
#Checking if input from user is equal or not
'''
Check the author's name
'''


a = int(input("enter numbers: "))
b = int(input("enter another number: "))
if a == b:
    print("numbers are equal")
else:
    print("numbers are not equal")
    
#should be a function
def check_equal(a, b):
    if a == b:
        print("numbers are equal")
    else:
        print("numbers are not equal")
    
#test the function
a = int(input("enter numbers: "))
b = int(input("enter another number: "))
check_equal(a, b)
