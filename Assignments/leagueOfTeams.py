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
            self.percentage = '100'
        elif self.lose == 0 and self.win == 0:
            self.percentage = 'not_enough_data_to_compute'
        else:
            total = self.win + self.lose
            self.percentage = self.win / total * 100


teams = [League() for x in range(0, 8)]

# loop for adding scores in
while True:

    pickTeam = str(input("Which team (1,2,3,4,5,6,7,8) do you want to change there scores? (type done if finished) "))
    if pickTeam == 'done':
        break
    gameResult = input("Did they win, lose, or tie? ")

    # not sure why i cant give this multiple value to check upon just kept giving it to team one wins every time ie if
    # pickTeams == '1' or 'one' or 'ONE' and gameResult == 'win' but if you do that for all cases it just does not work
    if pickTeam == '1' and gameResult == 'win':
        teams[0].win_score()
    elif pickTeam == '1' and gameResult == 'lose':
        teams[0].lose_score()
    elif pickTeam == '1' and gameResult == 'tie':
        teams[0].tie_score()
    elif pickTeam == '2' and gameResult == 'win':
        teams[1].win_score()
    elif pickTeam == '2' and gameResult == 'lose':
        teams[1].lose_score()
    elif pickTeam == '2' and gameResult == 'tie':
        teams[1].tie_score()
    elif pickTeam == '3' and gameResult == 'win':
        teams[2].win_score()
    elif pickTeam == '3' and gameResult == 'lose':
        teams[2].lose_score()
    elif pickTeam == '3' and gameResult == 'tie':
        teams[2].tie_score()
    elif pickTeam == '4' and gameResult == 'win':
        teams[3].win_score()
    elif pickTeam == '4' and gameResult == 'lose':
        teams[3].lose_score()
    elif pickTeam == '4' and gameResult == 'tie':
        teams[3].tie_score()
    elif pickTeam == '5' and gameResult == 'win':
        teams[4].win_score()
    elif pickTeam == '5' and gameResult == 'lose':
        teams[4].lose_score()
    elif pickTeam == '5' and gameResult == 'tie':
        teams[4].tie_score()
    elif pickTeam == '6' and gameResult == 'win':
        teams[5].win_score()
    elif pickTeam == '6' and gameResult == 'lose':
        teams[5].lose_score()
    elif pickTeam == '6' and gameResult == 'tie':
        teams[5].tie_score()
    elif pickTeam == '7' and gameResult == 'win':
        teams[6].win_score()
    elif pickTeam == '7' and gameResult == 'lose':
        teams[6].lose_score()
    elif pickTeam == '7' and gameResult == 'tie':
        teams[6].tie_score()
    elif pickTeam == '8' and gameResult == 'win':
        teams[7].win_score()
    elif pickTeam == '8' and gameResult == 'lose':
        teams[7].lose_score()
    elif pickTeam == '8' and gameResult == 'tie':
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
          team.percentage, '%')
    count += 1
