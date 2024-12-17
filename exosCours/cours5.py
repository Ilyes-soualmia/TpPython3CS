team1 = "Houma"
team2 = "Braniya"
scoreHouma = -1
scoreBraniya = -1
while scoreHouma < 0:
    scoreHouma = int(input(f"Please type in the score of {team1}: "))
while scoreBraniya < 0:    
    scoreBraniya = int(input(f"Please type in the score of {team2}: "))

if scoreHouma > scoreBraniya:
    print(f"{team1} Wins the game!")
elif scoreHouma < scoreBraniya:
    print(f"{team2} Wins the game!")
else:
    print("It's a draw!")    