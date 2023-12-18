import random

"""_summary_

0: cooperate
1: defect

"""

class ThreePrisonersDilemma:
    def __init__(self):
        self.payoff = [
            [
                [6,3], # payoffs when 1st and 2nd players cooperate
                [3,0], # payoffs when 1st player coop, 2nd player defects
            ],
            [
                [8,5], # payoffs when 1st player defects ,2nd player coops
                [5,2], # payoffs when both 1st and 2nd players defect
            ],
        ]
    class Player:
        def select_action(self, n, my_history, opp_history1, opp_history2):
            raise NotImplementedError("You need to override the select_action method")
        
        def name(self):
            return self.__class__.__name__
        
    class NicePlayer(Player):
        def select_action(self, n, my_history, opp_history1, opp_history2):
            return 0 # always cooperate
        
    class NastyPlayer(Player):
        def select_action(self, n, my_history, opp_history1, opp_history2):
            return 1
        
    class RandomPlayer(Player):
        def select_action(self, n, my_history, opp_history1, opp_history2):
            return random.choice([0,1]) # randomly choose to cooperate or defect
        
    class TolerantPlayer(Player):
        def select_action(self, n, my_history, opp_history1, opp_history2):
            opponent_coop = opp_history1.count(0) + opp_history2.count(0)
            opponent_defect = opp_history1.count(1) + opp_history2.count(1)
            
            if opponent_defect > opponent_coop:
                return 1 # choose to defect
            else:
                return 0 # choose to cooperate
            
    class FreakyPlayer(Player):
        def __init__(self):
            self.action = 0 if random.random() < 0.5 else 1
        
        def select_action(self, n, my_history, opp_history1, opp_history2):
            return self.action
        
        
    class T4TPlayer(Player):
        # Tit-for-Tat 
        def select_action(self, n, my_history, opp_history1, opp_history2):
            if n==0:
                return 0 # cooperate by default
            return opp_history1[-1] if random.random() < 0.5 else opp_history2[-1]
        
        
    class OtherPlayer(Player):
        def select_action(self, n, my_history, opp_history1, opp_history2):
            random_num = random.random()
            if random_num < 0.1:
                # Tolerant Player strategy
                opponent_coop = opp_history1.count(0) + opp_history2.count(0)
                opponent_defect = opp_history1.count(1) + opp_history2.count(1)
                if opponent_defect > opponent_coop:
                    return 1  # Defect
                else: 
                    return 0  # Cooperate
                
            elif random_num < 0.3:
                # Freaky player strategy
                return 0 if random.random() < 0.5 else 1
                
            elif random_num < 0.5:
                # T4T player strategy
                if n == 0:
                    return 0  # cooperate by default
                return opp_history1[-1] if random.random() < 0.5 else opp_history2[-1]
                
            else:  # 0.5 of the time
                # Nasty player strategy
                return 1

            # Ensure that it always returns 0 or 1
            return random.choice([0, 1])
            

    class MyPlayer(Player):
        def __init__(self):
            self.res = 0
            self.long_res = 0
            self.short_res = 0
            self.opponent_coop = 0
            self.opponent_Defect = 0
            
        def select_action(self, n, my_history, opp_history1, opp_history2):
            if n <2:
                return 0 # cooperate by default
            
            # short term
            if opp_history1[-1] ==0 and opp_history2[-1] == 1:
                self.short_res = 0
            elif opp_history1[-1] ==1 and opp_history2[-1] == 0:
                self.short_res = 0
            elif opp_history1[-1] == 1 and opp_history2[-2] == 1:
                self.short_res = 1 # default
            elif opp_history1[-1] == 0 and opp_history2[-2] == 0:
                self.short_res = 0 # cooperate
            
            # Long term
            opponent_coop = opp_history1.count(0) + opp_history2.count(0)
            opponent_defect = opp_history1.count(1) + opp_history2.count(1)
            if opponent_defect > opponent_coop:
                self.long_res = 1 # defect
            else:
                self.long_res = 0 # cooperate    
            
            # combining long-term and short-term strategy
            if self.long_res == 0 and self.short_res == 0:
                self.res = 0
            elif self.long_res == 1 and self.short_res == 1:
                self.res = 1
                
            else:
                if random.random() < 0.75:
                    self.res = self.long_res
                else:
                    self.res = self.short_res
            return self.res
                    
    def scores_of_match(self, A, B, C, rounds):
        history_A, history_B, history_C = [], [], []
        score_A, score_B, score_C = 0, 0, 0
        
        for i in range(rounds):
            play_A = A.select_action(i, history_A, history_B, history_C)
            play_B = B.select_action(i, history_B, history_C, history_A)
            play_C = C.select_action(i, history_C, history_A, history_B)
            
            play_A = int(play_A)
            play_B = int(play_B)
            play_C = int(play_C)
            
            score_A += self.payoff[play_A][play_B][play_C]
            score_B += self.payoff[play_B][play_C][play_A]
            score_C += self.payoff[play_C][play_A][play_B]
            
            history_A.append(play_A)
            history_B.append(play_B)
            history_C.append(play_C)
            
        result = [score_A/rounds, score_B/rounds, score_C/rounds]
        return result
    
    def extend_int_array(self, arr, next):
        result = arr.copy()
        result.append(next)
        return result
    
    def make_player(self, which):
        if which ==0:
            return self.NicePlayer()
        elif which == 1:
            return self.NastyPlayer()
        elif which == 2:
            return self.FreakyPlayer()
        elif which == 3:
            return self.RandomPlayer()
        elif which == 4: 
            return self.TolerantPlayer()
        elif which == 5: 
            return self.T4TPlayer()
        elif which == 6:
            return self.OtherPlayer()
        elif which == 7:
            return self.MyPlayer()
        
        
    def run_tournament(self):
        num_players = 8
        total_score = [0] * num_players
        
        for i in range(num_players):
            for j in range(i, num_players):
                for k in range(j, num_players):
                    A = self.make_player(i)
                    B = self.make_player(j)
                    C = self.make_player(k)
                    
                    rounds = 90 + int(round(20 * random.random())) # b/w 90 - 110 rounds
                    match_results = self.scores_of_match(A,B,C, rounds)
                    total_score[i] +=match_results[0]
                    total_score[j] +=match_results[1]
                    total_score[k] +=match_results[2]
                    
        sorted_order = sorted(range(num_players), key = lambda x: total_score[x], reverse = True)
        
        print("\n Tournament Results")
        for i in sorted_order:
            player = self.make_player(i)
            print(f"{player.name()}: {total_score[i]} points.")


if __name__ == "__main__":
    instance = ThreePrisonersDilemma()
    instance.run_tournament()
            