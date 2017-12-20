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
player1 = game_agent.MinimaxPlayer(search_depth = 2)
player2 = game_agent.MinimaxPlayer(search_depth = 2)
game = isolation.Board(player1, player2)

# =============================================================================
# print(player1.get_move(game,time_left))
# game.apply_move((4,4))
# print(player2.get_move(game,time_left))
# game.apply_move((3,4))
# print(player1.get_move(game,time_left))
# game.apply_move((3,2))
# print(player2.get_move(game,time_left))
# game.apply_move((4,2))
# print(game.print_board())
# =============================================================================


wplayer = game_agent.MinimaxPlayer()
moves_list = []
wreason = ''

wplayer, moves_list,wreason = game.play(time_limit=1000000.)
print(wplayer)
print(moves_list)
print(wreason)
print(game.print_board())

# =============================================================================
# player1 = game_agent.MinimaxPlayer()
# player2 = game_agent.MinimaxPlayer()
# game = isolation.Board(player1, player2)
# 
# gmoves = moves_list
# 
# for m in gmoves:
#     game.apply_move(tuple(m))
# print(game.print_board())
# print(player2.get_move(game,time_left))    
# print(game.get_legal_moves(player2))
# =============================================================================


# =============================================================================
# print(player1.get_move(game,time_left))
# game.apply_move((3,0))
# print(player2.get_move(game,time_left))
# game.apply_move((1,1))
# print(player1.get_move(game,time_left))
# game.apply_move((5,1))
# print(player2.get_move(game,time_left))
# # =============================================================================


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