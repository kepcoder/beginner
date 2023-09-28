


print("lets check you how you scrored in each subject")
marks = float(input("Enter Your marks out of 100 in each subject:"))
passingmarks = float(input("Enter you passing marks:"))
if(marks==passingmarks):
    print("You are close to fail but pass")   
elif(marks>=85 and marks<=100):
    print('''You earn Grade "A"''')
elif(marks>100):
    print("marks is not more than 100 in 1 subject")
elif(marks<passingmarks):
    print("You are fail")   
elif(marks>=75 and marks<=84):
    print('''You Earn Grade "B" ''' )
elif(marks>=65 and marks<=74):
    print(''' You Earn Grade"C" ''' )
elif(marks>=50 and marks<=64):
    print('''You Earn Grade "D" ''')
elif(marks>=36 and marks<=50):
    print("You Need To Study Hard")
elif(marks<=35 and marks>=0):
    print("you are close to fail")    
else:
    print("You are fail")   