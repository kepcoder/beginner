import random


   #   LOGIC2
# def checkwin(x,y):
#    if x==y :
#         return("Match Draw")
#    if x=="stone" and y=="paper":
#        return("You won the match") 
#    if x=="stone" and y=="scissors":
#        return("You lose the match") 
#    if x=="paper" and y=="stone": 
#        return("you won the match")
#    if x=="paper" and y=="scissors": 
#        return("you lose the match")
#    if x=="scissors" and y=="stone": 
#        return("you lose th match")
#    if x=="scissors" and y=="paper": 
#        return("you won the match")
#    return "worng input"



# logic 1

def checkwin(x,y):
   if x==y :
        return("Match Draw")
   if x=="stone" and y=="paper":
       return("You won the match") 
   if x=="stone" and y=="scissors":
       return("You lose the match") 
   if x=="paper" and y=="stone": 
       return("you won the match")
   if x=="paper" and y=="scissors": 
       return("you lose the match")
   if x=="scissors" and y=="stone": 
       return("you lose th match")
   if x=="scissors" and y=="paper": 
       return("you won the match")
   return "worng input"


    #   LOGIC3
# outcomes = {
#     "stone": {"stone": "Match Draw", "paper": "You won the match", "scissors": "You lose the match"},
#     "paper": {"stone": "You lose the match", "paper": "Match Draw", "scissors": "You won the match"},
#     "scissors": {"stone": "You won the match", "paper": "You lose the match", "scissors": "Match Draw"},
# }
# def checkwin(x,y):
#     if x not in outcomes or y not in outcomes:
#         return "wrong input"
#     return outcomes[x][y]


while True:
    player1 = input("Enter your  name: ")
    print("Computer name is [ Djac leon darry ]")
    print("lets play Stone , paper , scissors")
    names = ["stone" , "paper" , "scissors"]
    x = input("What can you choose: ")
    print(f"{player1} : {x}")
    y = random.choice(names)
    print(f"Computer : {y}")

    result = checkwin(x,y)
    print(result)

    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
       break    