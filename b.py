# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:39:43 2017

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
game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 60]
print(game.print_board())
print(player1.get_move(game,time_left))
# =============================================================================
# wplayer = game_agent.MinimaxPlayer()
# moves_list = []
# wreason = ''
# 
# wplayer, moves_list,wreason = game.play(time_limit=1000000.)
# print(wplayer)
# print(moves_list)
# print(wreason)
# print(game.print_board())
# =============================================================================
