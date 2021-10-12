class League():
    # leagues have teams which will have all the attributes of this league

    def __init__(self):
        self.win = 0
        self.lose = 0
        self.tie = 0
        self.percentage = 0

    def win_score(self):
        self.win += 1

    def lose_score(self):
        self.lose += 1

    def tie_score(self):
        self.tie += 1

# might not need this function because might be able to do it above in __init__
    def win_lose_percentage(self):
        self.percentage = self.win / self.lose


teams = [League() for x in range(0, 8)]

#loop to do this for 8 teams each round its like a double loop type thing should be easy to figure out

pickTeam = input("Which team do you want to change there scores? (ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN, or EIGHT) ")
gameResult = input("Did they win, lose, or tie? ")

if pickTeam == "ONE" and gameResult == 'win':
    teams[0].win_score()
elif pickTeam == "ONE" and gameResult == 'lose':
    teams[0].lose_score()
elif pickTeam == "ONE" and gameResult == 'tie':
    teams[0].tie_score()
elif pickTeam == "TWO" and gameResult == 'win':
    teams[1].win_score()
elif pickTeam == "TWO" and gameResult == 'lose':
    teams[1].lose_score()
elif pickTeam == "TWO" and gameResult == 'tie':
    teams[1].tie_score()
elif pickTeam == "THREE" and gameResult == 'win':
    teams[2].win_score()
elif pickTeam == "THREE" and gameResult == 'lose':
    teams[2].lose_score()
elif pickTeam == "THREE" and gameResult == 'tie':
    teams[2].tie_score()
elif pickTeam == "FOUR" and gameResult == 'win':
    teams[3].win_score()
elif pickTeam == "FOUR" and gameResult == 'lose':
    teams[3].lose_score()
elif pickTeam == "FOUR" and gameResult == 'tie':
    teams[3].tie_score()
elif pickTeam == "FIVE" and gameResult == 'win':
    teams[4].win_score()
elif pickTeam == "FIVE" and gameResult == 'lose':
    teams[4].lose_score()
elif pickTeam == "FIVE" and gameResult == 'tie':
    teams[4].tie_score()
elif pickTeam == "SIX" and gameResult == 'win':
    teams[5].win_score()
elif pickTeam == "SIX" and gameResult == 'lose':
    teams[5].lose_score()
elif pickTeam == "SIX" and gameResult == 'tie':
    teams[5].tie_score()
elif pickTeam == "SEVEN" and gameResult == 'win':
    teams[6].win_score()
elif pickTeam == "SEVEN" and gameResult == 'lose':
    teams[6].lose_score()
elif pickTeam == "SEVEN" and gameResult == 'tie':
    teams[6].tie_score()
elif pickTeam == "EIGHT" and gameResult == 'win':
    teams[7].win_score()
elif pickTeam == "EIGHT" and gameResult == 'lose':
    teams[7].lose_score()
elif pickTeam == "EIGHT" and gameResult == 'tie':
    teams[7].tie_score()

# HOW TO DO WIN LOSE PERCENTAGE in loop here to get them to print out

count = 1
for team in teams:
    print("Team", count, ": Wins", team.win, "Loses", team.lose, "Ties", team.tie, "Win/Lose Percentage", team.percentage)
    count += 1
