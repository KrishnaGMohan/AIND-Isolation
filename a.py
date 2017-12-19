# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 04:25:38 2017

@author: krgandhi
"""

import isolation
import game_agent
def time_left():
     return 100000.

#reload(game_agent)
player1 = game_agent.MinimaxPlayer()
player2 = game_agent.MinimaxPlayer()
game = isolation.Board(player1, player2)

gmoves = [[3, 0], [1, 1], [2, 2], [0, 3], [1, 4], [2, 4], [3, 5], [3, 2], [5, 4], [5, 3], [3, 3], [6, 5], [1, 2], [4, 6], [3, 1], [2, 5], [2, 3], [1, 3], [4, 2], [3, 4], [6, 3], [5, 5], [4, 4], [4, 3], [5, 2], [6, 4], [6, 0], [4, 5], [4, 1]]
#gmoves = [[3, 0], [1, 1], [4, 2], [3, 2], [2, 1], [2, 4], [1, 3], [4, 3], [2, 5], [3, 5], [4, 6], [5, 6], [3, 4], [6, 4], [2, 2], [4, 5], [1, 0], [3, 3], [3, 1], [5, 2], [2, 3], [6, 0], [0, 2], [4, 1], [1, 4], [2, 0]]
#gmoves = [[3, 0], [1, 1], [2, 2], [0, 3], [1, 4], [1, 5], [3, 5], [2, 3], [5, 4], [4, 4], [6, 6], [3, 6], [4, 5], [5, 5], [2, 4], [3, 4], [1, 2], [4, 2], [3, 3], [2, 1], [4, 1], [4, 0], [6, 2], [5, 2], [4, 3], [3, 1], [5, 1]]
#gmoves = [[3, 0], [1, 1], [4, 2], [2, 3], [2, 1], [3, 1], [1, 3], [4, 3], [2, 5], [5, 5], [3, 3], [3, 6], [4, 1], [2, 4], [2, 2], [3, 2], [1, 4], [4, 4], [3, 5], [6, 5], [5, 6], [5, 3], [6, 4], [4, 5], [5, 2], [6, 6]]
#gmoves = [[3, 0], [1, 1], [5, 1], [3, 2], [4, 3], [1, 3], [3, 5], [2, 1], [5, 6], [4, 2], [4, 4], [5, 4], [3, 6], [3, 3], [1, 5], [4, 1], [2, 3], [2, 2], [3, 1], [0, 3], [1, 2], [2, 4], [0, 4], [4, 5], [2, 5], [2, 6]]

for m in gmoves:
    game.apply_move(tuple(m))
print(game.print_board())
print(player2.get_move(game,time_left))    
print(game.get_legal_moves(player2))


# =============================================================================
# print(player1.get_move(game,time_left))
# game.apply_move((3,0))
# print(player2.get_move(game,time_left))
# game.apply_move((1,1))
# print(player1.get_move(game,time_left))
# game.apply_move((5,1))
# print(player2.get_move(game,time_left))
# # =============================================================================
# =============================================================================
# wplayer = game_agent.MinimaxPlayer()
# moves_list = []
# wreason = ''
# 
# wplayer, moves_list,wreason = game.play(time_limit=1000000.)
# print(wplayer)
# print(moves_list)
# print(wreason)
# =============================================================================


#print(game.print_board())

# =============================================================================

# print(moves_list)
# 
# =============================================================================
# =============================================================================
# # =============================================================================
# print(game.print_board())
# # print(game.get_player_location(player1))
# # print(game.get_player_location(player2))
# # =============================================================================
# game.apply_move((3,0))
# game.apply_move((1,1))
# game.apply_move((5,1))
# game.apply_move((3,2))
# game.apply_move((4,3))
# game.apply_move((1,3))
# print(game.print_board())
 # x = player1.get_move(game,time_left)
# print(x)
# =============================================================================
