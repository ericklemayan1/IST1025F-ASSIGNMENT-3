import random

def get_choices():
    player_choice=input("Enter a choice(stone, paper,knife):")
    options=["stone","paper","knife"]
    computer_choice=random.choice(options)
    choices={"player":player_choice, "computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player==computer:
     return"It's a tie "
    elif player== "stone":  
       if computer=="knife":
          return "stone blunts knife! you win!"
       else:
         return "paper wraps stone! you lose!"
    elif player== "paper":  
       if computer=="stone":
          return "paper wraps stone! you win!"
       else:
         return " knife cuts paper! you lose!"
    elif player== "knife":  
       if computer=="paper":
          return "knife cuts paper! you win!"
       else:
         return "stone blunts knife! you lose!"
    
choices=get_choices()
result =check_win(choices["player"], choices["computer"])
print(result)