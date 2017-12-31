# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:26:02 2017

@author: krgandhi
"""
import isolation
import game_agent
import random

player1 = game_agent.AlphaBetaPlayer(score_fn=custom_score)
player2 = game_agent.AlphaBetaPlayer(score_fn=custom_score_2)
game = isolation.Board(player1, player2)

moves = [[6, 3], [4, 1], [4, 2], [2, 2], [6, 1], [1, 0], [5, 3], [0, 2], [6, 5], [2, 3], [4, 4], [3, 1], [3, 6], [1, 2], [5, 5], [2, 4], [3, 4], [4, 5], [2, 6], [3, 3], [1, 4], [2, 5], [3, 5]]

for i in moves:
    game.apply_move(i)


print(game.print_board())
print(player1)
print(player2)
print(game.get_player_location(player1))
print(game.get_player_location(player2))
print(game.active_player)
print(ktour_length(game, player1))
print(ktour_length(game, player2))

# =============================================================================
# wplayer, moves_list,wreason = game.play()
# 
# print(wplayer)
# print(moves_list)
# print(wreason)
# print(game.print_board())
# =============================================================================
