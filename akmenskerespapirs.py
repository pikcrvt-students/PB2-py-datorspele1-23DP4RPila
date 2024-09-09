import random, time

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

win = '''
 __      _____ _  _ 
 \\ \\    / /_ _| \\| |
  \\ \\/\\/ / | || .` |
   \\_/\\_/ |___|_|\\_|
'''

loss = '''
  _    ___  ___ ___ 
 | |  / _ \\/ __/ __|
 | |_| (_) \\__ \\__ \\
 |____\\___/|___/___/
'''

draw = '''
  ___  ___    ___      __
 |   \\| _ \\  /_\\ \\    / /
 | |) |   / / _ \\ \\/\\/ / 
 |___/|_|_\\/_/ \\_\\_/\\_/  
'''

choices = ["rock", "scissors", "paper"]
chosen_action = {rock: "rock", scissors: "scissors", paper: "paper"}

games = 0
wins = 0
losses = 0
draws = 0
invalid_choices = 0
extra_gameSystem = 1
playagain = 0

while extra_gameSystem > 0:
    for i in range(5):           
        player_choice = input('''                          -----------------------------------------------------------------------------------------------
                            Play the game: rock, paper, scissors! Choose your element by typing - rock, paper or scissors: ''')    
        computer_choice = random.choice(choices)
            
        time.sleep(0.25)
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
            invalid_choices = invalid_choices + 1
            print("Invalid input. Accepted inputs: 'rock', 'paper' or 'scissors'. (no spaces, no capital letters)")
        print(f"{player_choice}")

        time.sleep(1.5)
        print("Computer chose:", '''
          -------
         /        \\
        |  O   O   |
        |          |   
         \\  ---   /
          -------
        ''', end = '')
        if computer_choice == "rock":
            print(rock)
        elif computer_choice == "paper":
            print(paper)
        elif computer_choice == "scissors":
            print(scissors)
        print(f"{computer_choice}")
        time.sleep(1.5)
            
        if player_choice == "rock" and computer_choice == "scissors":
            games = games + 1
            wins = wins + 1        
            print(win)
        elif player_choice == "paper" and computer_choice == "rock":
            games = games + 1
            wins = wins + 1        
            print(win)
        elif player_choice == "scissors" and computer_choice == "paper":
            games = games + 1
            wins = wins + 1        
            print(win)


        if player_choice == "rock" and computer_choice == "paper":
            games = games + 1
            losses = losses + 1        
            print(loss)
        elif player_choice == "paper" and computer_choice == "scissors":
            games = games + 1
            losses = losses + 1        
            print(loss)
        elif player_choice == "scissors" and computer_choice == "rock":
            games = games + 1
            losses = losses + 1        
            print(loss)

        if player_choice == "rock" and computer_choice == "rock":
            games = games + 1
            draws = draws + 1        
            print(draw)
        elif player_choice == "paper" and computer_choice == "paper":
            games = games + 1
            draws = draws + 1        
            print(draw)
        elif player_choice == "scissors" and computer_choice == "scissors":
            games = games + 1
            draws = draws + 1        
            print(draw)
    print('''-------------------------------------------
        Restults from the last 5 games: ''')
    print()
    print("Wins: ", wins)
    print("Losses: ", losses)
    print("Draws: ", draws)
    if invalid_choices > 0:
        print("Invalid choices: ", invalid_choices)
    extra_gameSystem -= 1

    print()
    playagain = input("Play 5 rounds again? (y/n)")
    if playagain == "y":
        extra_gameSystem += 1
    if playagain == "n":
        print("Ok, bye!")
