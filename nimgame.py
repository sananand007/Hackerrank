'''
https://www.hackerrank.com/challenges/nim-game-1/problem
Check the link above for input files
Nim is the most famous two-player algorithm game! The basic rules for this game are as follows:

The game starts with  piles of stones indexed from  to . Each pile  (where ) has  stones.
The players move in alternating turns, with First always playing first and Second always playing second. During each move, the current player must remove one or more stones from a single pile.
The first player who is unable to remove a stone (e.g., a stone can't be removed if all piles are already empty) loses the game.
Given the value of  and the number of stones in each pile, determine the game's winner if both players play optimally.

Input Format

The first line contains an integer, g, denoting the number of games they play.
Each of the 2g subsequent lines defines a game. Each game is described over the following two lines:

An integer, n, denoting the number of piles.
n space-separated integers, si, where each  describes the number of stones at pile .

1<=g<=100
1<=n<=100
0<=si<=100

Output Format

For each game, print the name of the winner on a new line (i.e., either First or Second).
'''

import sys
from functools import reduce
from operator import xor
g = int(sys.stdin.readline()) #number of games
# each of 2g next lines defines a game
def find(np, nv):
    if np==1:
        if not res:
            print("First")
    elif np>1:
        if reduce(xor, nv)==0:
            print("Second")
        else:
            print("First")

while g:
    npiles = int(sys.stdin.readline())
    values = (sys.stdin.readline().split())
    #nvalues = ['{0:08b}'.format(x) for x in values]
    nvalues = [int(x) for x in values]
    find(npiles, nvalues)
    g-=1
