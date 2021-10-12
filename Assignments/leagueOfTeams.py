class League():
    # leagues have teams which will have all the attributes of this league

    def __init__(self):
        self.win = 0
        self.lose = 0
        self.tie = 0

    def change_score_by_one(self):
        self.win += 1
        self.lose += 1
        self.tie += 1

    def change_score_by_num(self, num):
        self.win += num
        self.lose += num
        self.tie += num


teams = [League() for x in range(0, 8)]
