class Rank:

    rank_list = ("C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "S0", "S1", "S2", "S+0", "S+1", "S+2")
    next_rank_points = tuple([
        10*(4-int(j[-1])*(int(j[-1])-1)) if j[0] == "S" else 100 for j in rank_list
    ])
    def __init__(self, rank, points=0):
        assert rank in self.rank_list or rank == "S" or rank == "S+", "invalid rank"
        self.rank = rank

        assert 0 <= points and points < 100, "invalid points"
        self.points = points

        if rank[0] == "S" and rank not in self.rank_list:
            if points < 40:
                self.rank += "0"
                self.points -= 0
            elif points < 80:
                self.rank += "1"
                self.points -= 40
            elif points < 100:
                self.rank += "2"
                self.points -=80

        self.rank_i = self.rank_list.index(self.rank)
    
    def real_points(self):
        if self.rank[0] != "S":
            return self.points
        elif self.rank[-1] == "0":
            return self.points
        elif self.rank[-1] == "1":
            return self.points + 40
        elif self.rank[-1] == "2":
            return self.points + 80
    
    def total_points(self):
        output = 0
        for i in range(self.rank_i):
            output += self.next_rank_points[self.rank_list[i]]
    
    def step(self):
        s = [
            (20, -10),
            (15, -10)
        ]
        s += [(12, -10)]*2
        s += [(10, -10)]*5
        s += [
            (5, -5),
            (4, -5),
            (4, -6),
            (4, -4),
            (3, -5),
            (2, -5)
        ]
        s = tuple(s)
        return s[self.rank_i]
    
    def threshold(self):
        t = self.step()
        return t[1]/(t[1]-t[0])

    def earned(self, probability=0.5):
        """
        0<=probability<=1
        """
        t = self.step()
        out = probability*(t[0] - t[1]) + t[1]
        if out // 1 == out:
            out = int(out)
        return out

    def adjust(self, probability):
        if isinstance(probability, str):
            if probability[0] == "w":
                probability = 1
            elif probability[0] == "l":
                probability = 0
            else:
                probability = 0.5

        self.points += self.earned(probability)

        if self.points >= self.next_rank_points[self.rank_i]:
            if self.rank != "S+2":
                stuff = (
                    self.rank_list[self.rank_i + 1],
                    self.points - self.next_rank_points[self.rank_i]
                )
                self.__init__(stuff[0],stuff[1])

            else:
                self.points = 19

        if self.points < 0:
            if self.rank != "C-":
                stuff = [
                    self.rank_list[self.rank_i - 1],
                    self.next_rank_points[self.rank_i] + self.points
                ]
                self.__init__(stuff[0],stuff[1])
            else:
                self.points = 0
        return self
    
    def __str__(self):
        output = self.rank
        if self.rank[0] == "S":
            output = output[:-1]
        return "{0} {1}".format(output,(10*self.real_points())//10)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    
    def draw(p):
        """
        p is for probability
        """
        s = [
            {"name": "C-" , "size": 100, "wager": (20, -10),},
            {"name": "C"  , "size": 100, "wager": (15, -10),},
            {"name": "C+" , "size": 100, "wager": (12, -10),},
            {"name": "B-" , "size": 100, "wager": (12, -10),},
            {"name": "B"  , "size": 100, "wager": (10, -10),},
            {"name": "B+" , "size": 100, "wager": (10, -10),},
            {"name": "A-" , "size": 100, "wager": (10, -10),},
            {"name": "A"  , "size": 100, "wager": (10, -10),},
            {"name": "A+" , "size": 100, "wager": (10, -10),},
            {"name": "S0" , "size":  40, "wager": ( 5,  -5),},
            {"name": "S1" , "size":  20, "wager": ( 4,  -5),},
            {"name": "S2" , "size":  20, "wager": ( 4,  -6),},
            {"name": "S+0", "size":  40, "wager": ( 4,  -4),},
            {"name": "S+1", "size":  20, "wager": ( 3,  -5),},
            {"name": "S+2", "size":  20, "wager": ( 2,  -5),},
        ]
        for i in range(len(1,s)):
            s[i]["cumulative"] = 0 if i == 0 else s[i-1]["cumulative"] + s[i-1]["size"]
            s[i]["mean"] = sum(s[i]["wager"])/2
            s[i]["fun"] = {"original": lambda x: s[i]["wager"][0] * x + s[i]["wager"][1] * (1 - x)}
            
            