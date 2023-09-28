def sum (a,b,c):
   return a+b+c
def print_board(xstate,ystate):
    one = 'X' if xstate[1] else ('O' if ystate[1] else 1)
    two = 'X' if xstate[2] else ('O' if ystate[2] else 2)
    three = 'X' if xstate[3] else ('O' if ystate[3] else 3)
    four = 'X' if xstate[4] else ('O' if ystate[4] else 4)
    five = 'X' if xstate[5] else ('O' if ystate[5] else 5)
    six = 'X' if xstate[6] else ('O' if ystate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if ystate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if ystate[8] else 8)
    nine = 'X' if xstate[9] else ('O' if ystate[9] else 9)
    print(f" {one}  | {two}  | {three} ")
    print(f"----|----|---")
    print(f" {four}  | {five}  | {six} ")
    print(f"----|----|---")
    print(f" {seven}  | {eight}  | {nine} ")
def restart():
    global xstate , ystate , turn      
    xstate = [0,0,0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0,0,0]
    turn = 1    

def checkwin(xstate,ystate):
   wins = [ [1,2,3],[4,5,6],[7,8,9,],[1,4,7,],[2,5,8,],[3,6,9,],[1,5,9,],[3,5,7,] ]
   for win in wins :
     if sum(xstate[win[0]] , xstate[win[1]] , xstate[win[2]])==3:
        print("X won the match")
        return 1
     if sum(ystate[win[0]] , ystate[win[1]] , ystate[win[2]])==3:    
        print("O won the match")
        return 0
   if all(xstate[i] + ystate[i] == 1 for i in range(1, 10)):
      print("It's a draw!")  
      print_board(xstate,ystate)
      return restart()
   return -1
if  __name__=="__main__":
 while True:
  restart()    
  while True:
    
     print_board(xstate,ystate)
     if turn==1:
      print("X's chance: ")
      value = int(input("Enter the value: "))
      xstate[value] = 1
     else :
      print("O's Chance: ")
      value1 = int(input("Enter the value: "))
      ystate[value1] = 1 
       
     check = checkwin(xstate,ystate)
     if check != -1: 
      print_board(xstate,ystate)
      break
     turn  = 1-turn
  play_again = input("Do you want to play again(yes/no): ").lower()
  if play_again != "yes" :
        break
 



          #PRACTISE

# class employee:
#     def __init__(self,Name,salary):
#         self.name = Name
#         self.salary = salary
#     def details(self):
#         print(f"the name of the employee is {self.name} with salary {self.salary}")

#     @classmethod
#     def tukda(cls,data):
#         return cls (data.split("-")[0] , data.split("-")[1])    
 
# a = employee("shubham" , 14000)
# a1 = employee("shivam",18000)
# data = "shubham-14000"
# data1 = "shivam-20000"
# a = employee(data.split("-")[0] , data.split("-")[1])
# a1 = employee(data1.split("-")[0] , data1.split("-")[1])
# a = employee.tukda(data)
# b = employee.tukda(data1)
# a.details()
# b.details()
# print(a.name)
# print(a.salary)

   #