# Three Prisoners Dilemma 

## Overview
This project is a python implementationo f the Three Prisoners Dilemma problem commonly implemented in Java. 
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
