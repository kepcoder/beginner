


# input = input("Enter any number: ")
# number = {
# "1":"one",
# "2":"two",
# "3":"three",
# "4":"four",
# "5":"five",
# "6":"six",
# "7":"seven",
# "8":"eight",
# "9":"nine",
# }
# output  = ""
# for ch in input:
#     output += number.get(ch, " !") + " "
# print(output)


# emozi converter
# try: 
#  name = input("Type here: ")
#  word = name.split(" ")

#  emozis = {
#     ":)" : "😃" , 
#     ":(" : "😔" , 
#     ":-" : "😶" ,
#     ":=" : "😑"
# } 
#  output = ""
#  for i in word:
#   output += emozis.get(i,i) + " "
#   print(output)
# except:
#     print(" Smilie Not found")


# using try: and except methods 

# def set():
#     try:
#         L = [1,2,3,4,5]
#         i = int(input("Enter the index: "))
#         print(L[i])
#         return 1
#     except:
#         print("Some error occured")  
#         return 0

#     finally:
#      print("I am always exceuted")    

# z = set()

print("Lets Play Kaun Bnaega Carorepati ")

questions = [ 
  [
        "If you call someone ‘Makkhichoos’, then what are you calling him?",
        "Evil",
        "Humble",
        "Dishonest",
        "Miserly",
        "none",
        4
    ],
    [
        "What number is used with reference to a type of cricket match as well as normal vision?",
        "50",
        "5",
        "1",
        "20",
        "none",
        3
    ],
   [
        "Which planet is known as the 'Red Planet'?",
        "Venus",
        "Mars",
        "Jupiter",
        "Saturn",
        "none",
        2
    ],
    [
        "What is the capital of France?",
        "Berlin",
        "London",
        "Madrid",
        "Paris",
        "none",
        4
    ],
    [
        "What is the largest mammal in the world?",
        "African Elephant",
        "Blue Whale",
        "Giraffe",
        "Hippopotamus",
        "none",
        2
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?",
        "Charles Dickens",
        "Mark Twain",
        "William Shakespeare",
        "Leo Tolstoy",
        "none",
        3
    ],
    [
        "What is the chemical symbol for gold?",
        "Au",
        "Ag",
        "Fe",
        "Hg",
        "none",
        1
    ],
    [
        "Which gas is most abundant in Earth's atmosphere?",
        "Oxygen",
        "Carbon Dioxide",
        "Nitrogen",
        "Hydrogen",
        "none",
        3
    ],
    [
        "What is the largest organ in the human body?",
        "Brain",
        "Heart",
        "Liver",
        "Skin",
        "none",
        4
    ],
    [
        "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "Oxygen",
        "Carbon Dioxide",
        "Nitrogen",
        "Hydrogen",
        "none",
        2
    ],
    [
        "What is the chemical symbol for water?",
        "H2O",
        "CO2",
        "O2",
        "N2",
        "none",
        1
    ],
    [
        "Who is the author of the 'Harry Potter' book series?",
        "J.R.R. Tolkien",
        "George Orwell",
        "J.K. Rowling",
        "Agatha Christie",
        "none",
        3
    ],
    [
        "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "Mars",
        "Jupiter",
        "Venus",
        "Saturn",
        "none",
        3
    ],
    [
        "What is the largest mammal on Earth?",
        "African Elephant",
        "Giraffe",
        "Hippopotamus",
        "Blue Whale",
        "none",
        4
    ],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,1600000,3200000,
640000,1250000,2500000,5000000,"1crore"] 
money = 0
for i in range(0,len(questions)):
  question = questions[i]
  print(f"question for Rs.{levels[i]}\n")
  print(question[0]) 
  print(f"a.{question[1]}     b.{question[2]}")
  print(f"c.{question[3]}     d.{question[4]}")
  reply = int(input("Enter the answer (1-4)"))
  if(reply == 0):
    print(f"Your take home money is Rs. {money}")
    break
  if (reply == question[-1] ):
   print(f"Correct  answer,  you won money {levels[i]} ")
   print(f"Wallet Balance :{levels[i]}\n")
   if(i == 4):
    money = 10000
   elif(i == 8):
    money = 320000
   elif(i == 14):
    money ="1crore"
  else:
   print("wrong answer") 
   print(f"your take home money is {money}")
   break 
   





