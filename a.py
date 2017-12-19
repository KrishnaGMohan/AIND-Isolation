# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 04:25:38 2017

@author: krgandhi
"""

import isolation
import game_agent
def time_left():
     return 10000.

#reload(game_agent)
player1 = game_agent.MinimaxPlayer()
player2 = game_agent.MinimaxPlayer()
game = isolation.Board(player1, player2)
print(player1.get_move(game,time_left))
#game.apply_move((3,0))
# print(player2.get_move(game,time_left))
# game.apply_move((1,1))


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
