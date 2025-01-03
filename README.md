# Three Prisoners Dilemma 

## Overview
This project is a python implementation of the Three Prisoners Dilemma problem commonly implemented in Java. 
I did the project in Java for a school assignment for the Intelligent Agents module and am creating this project for practice of converting Java code to python and to reinforce my learning from this project about multi-agent systems

## Background
In the game Prisoners' Dilemma, the doment strategy equilibrium is for agents to defect, even though both agents would be best off cooperating. If we move to a repeated version of the Prisoners' Dilemma, then this lack of coooperation could possibly disappear. 

In a repeated game, a given game is played multiple times by the same set of players. (Can be understood as many rounds conducted in a tournament)
The (average) reward of a player in a repeated game can be computed.

A strategy in a repeated game specifies what action the agent should take in each stage of the game, given all actions taken by all players in the past. 
Example Strategies: 
1. Trigger Strategy: an agent starts by cooperating, but if the other player ever defects, then the first palyer defects forever.
2. Tit-for-Tat (T4T) Strategy: an agent starts by cooperating, and thereafter chooses in round j+1 with the same action that the other agent had chosen in round j.
etc.

In this project, MyPlayer is pitted against 7 other types of specified players. 
MyPlayer performs exceptionally well, placing consistently in the top 3 in the tournaments that had been run.

![image](https://github.com/solarspaceclouds/ThreePrisonersDilemma-Python/assets/65459827/4a1b8402-2d08-45fd-953b-86fdfd0d7126)

# Instructions: 
run the python file: ThreePrisonersDilemma.py to see the results for a tournament which consists of (90-110) rounds

## Additional Information:
Add modifications to the Player classes or new Player classes as desired to try out different stratgies.

Have fun exploring!

### Additional Details on MyPlayer strategy
#### Short-term strategy
The short-term strategy looks at the action taken by the opponents only in the previous round and assumes they are likely to behave in the same way again. MyPlayer would observe the behaviour of the other agents.
If both other players cooperated in the previous, it would continue to cooperate in the next round (and this is a situation of Pareto Optimality and Maximum Social Welfare.) All agents choosing to cooperate together would result in all players being able to achieve the highest payoff. However, if one player defected in the previous round, MyPlayer would cooperate with the other cooperating player and in effect, ‘defect’ against the player who defected in the previous round. This choice would be punishing the defector while simultaneously deterring future defection from occurring.

In the case where both other players defect, MyPlayer would also defect. The
outcome would be least desirable, but ensures that MyPlayer doesn’t end up
with the lowest payoff.
The result of the short-term strategy is recorded in a variable short_res.

#### Long-term strategy
This strategy is inspired by the Tolerant player who looks at his opponents’ history and if at
least have of the other players’ actions have been defects, MyPlayer would also
choose to defect. Otherwise, MyPlayer would choose to cooperate. The result
of the long-term strategy is recorded in a variable long_res.

#### Final chosen strategy (decision to cooperate or defect)
If the action to cooperate or defect recommended by long_res and short_res are in conflict,
then the long_res action would be taken with 75% probability and the short_res action would
be taken with 25% probability.
