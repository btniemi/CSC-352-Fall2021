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
        if self.lose == 0 and self.win > 0:
            self.percentage = '100%'
        elif self.lose == 0 and self.win == 0:
            self.percentage = 'not_enough_data_to_compute'
        else:
            self.percentage = self.win / self.lose


teams = [League() for x in range(0, 8)]

# loop for adding scores in
# while True:

pickTeam = str(input("Which team do you want to change there scores? (type done if finished) "))
    # if pickTeam == 'done':
    #     break
gameResult = input("Did they win, lose, or tie? ")

if pickTeam == "ONE" or '1' or 'one' and gameResult == 'win':
    teams[0].win_score()
elif pickTeam == "ONE" or '1' or 'one' and gameResult == 'lose':
    teams[0].lose_score()
elif pickTeam == "ONE" or '1' or 'one' and gameResult == 'tie':
    teams[0].tie_score()
if pickTeam == "TWO" or '2' or 'two' and gameResult == 'win':
    teams[1].win_score()
elif pickTeam == "TWO" or '2' or 'two' and gameResult == 'lose':
    teams[1].lose_score()
elif pickTeam == "TWO" or '2' or 'two' and gameResult == 'tie':
    teams[1].tie_score()
elif pickTeam == "THREE" or '3' or 'three' and gameResult == 'win':
    teams[2].win_score()
elif pickTeam == "THREE" or '3' or 'three' and gameResult == 'lose':
    teams[2].lose_score()
elif pickTeam == "THREE" or '3' or 'three' and gameResult == 'tie':
    teams[2].tie_score()
elif pickTeam == "FOUR" or '4' or 'four' and gameResult == 'win':
    teams[3].win_score()
elif pickTeam == "FOUR" or '4' or 'four' and gameResult == 'lose':
    teams[3].lose_score()
elif pickTeam == "FOUR" or '4' or 'four' and gameResult == 'tie':
    teams[3].tie_score()
elif pickTeam == "FIVE" or '5' or 'five' and gameResult == 'win':
    teams[4].win_score()
elif pickTeam == "FIVE" or '5' or 'five' and gameResult == 'lose':
    teams[4].lose_score()
elif pickTeam == "FIVE" or '5' or 'five' and gameResult == 'tie':
    teams[4].tie_score()
elif pickTeam == "SIX" or '6' or 'six' and gameResult == 'win':
    teams[5].win_score()
elif pickTeam == "SIX" or '6' or 'six' and gameResult == 'lose':
    teams[5].lose_score()
elif pickTeam == "SIX" or '6' or 'six' and gameResult == 'tie':
    teams[5].tie_score()
elif pickTeam == "SEVEN" or '7' or 'seven' and gameResult == 'win':
    teams[6].win_score()
elif pickTeam == "SEVEN" or '7' or 'seven' and gameResult == 'lose':
    teams[6].lose_score()
elif pickTeam == "SEVEN" or '7' or 'seven' and gameResult == 'tie':
    teams[6].tie_score()
elif pickTeam == "EIGHT" or '8' or 'eight' and gameResult == 'win':
    teams[7].win_score()
elif pickTeam == "EIGHT" or '8' or 'eight' and gameResult == 'lose':
    teams[7].lose_score()
elif pickTeam == "EIGHT" or '8' or 'eight' and gameResult == 'tie':
    teams[7].tie_score()

# calc win percentage

teams[0].win_lose_percentage()
teams[1].win_lose_percentage()
teams[2].win_lose_percentage()
teams[3].win_lose_percentage()
teams[4].win_lose_percentage()
teams[5].win_lose_percentage()
teams[6].win_lose_percentage()
teams[7].win_lose_percentage()

count = 1
for team in teams:
    print("Team", count, ": Wins", team.win, "Loses", team.lose, "Ties", team.tie, "Win/Lose Percentage",
          team.percentage)
    count += 1
