import random

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
'''
paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
'''
scissors = '''
         _______        
     ---'   ____)____         
               ______)            
            __________)              
           (____)          
     ---.__(___)           
'''

draw = '''     ___  ___    ___      __
    |   \\| _ \\  /_\\ \\    / /
    | |) |   / / _ \\ \\/\\/ / 
    |___/|_|_\\/_/ \\_\\_/\\_/  '''

win = ''' __      _____ _  _ 
 \\ \\    / /_ _| \\| |
  \\ \\/\\/ / | || .` |
   \\_/\\_/ |___|_|\\_|'''

loss = '''  _    ___  ___ ___ 
 | |  / _ \\/ __/ __|
 | |_| (_) \\__ \\__ \\
 |____\\___/|___/___/
                    '''


player_choice = input("Play the game: rock, scissors, paper! Choose your element by typing - rock, paper or scissors. > ")
choices = ["rock", "scissors", "paper"]
chosen_action = {rock: "rock", scissors: "scissors", paper: "paper"}
computer_choice = random.choice(choices)


    

print("User chose:", '''
  O O
   -
\\_____/  
''', end = '')
if player_choice == "rock":
    print(rock)
elif player_choice == "paper":
    print(paper)
elif player_choice == "scissors":
    print(scissors)
elif player_choice != choices:
    print("???")
print(f"{player_choice}")


print("Computer chose:", '''
  -------
 /        \\
|  O   O  |
|         |   
 \\  ---  /
  -------
''', end = '')
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
elif computer_choice == "scissors":
    print(scissors)
print(f"{computer_choice}")


if player_choice == "rock" and computer_choice == "rock":
    print(draw)
elif player_choice == "paper" and computer_choice == "paper":
    print(draw)
elif player_choice == "scissors" and computer_choice == "scissors":
    print(draw)

    
if player_choice == "rock" and computer_choice == "scissors":
    print(win)
elif player_choice == "paper" and computer_choice == "rock":
    print(win)
elif player_choice == "scissors" and computer_choice == "paper":
    print(win)


if player_choice == "rock" and computer_choice == "paper":
    print(loss)
elif player_choice == "paper" and computer_choice == "scissors":
    print(loss)
elif player_choice == "scissors" and computer_choice == "rock":
    print(loss)