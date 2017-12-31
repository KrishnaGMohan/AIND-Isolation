# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:39:43 2017

@author: krgandhi
"""
import isolation
import game_agent
import random

player1 = game_agent.AlphaBetaPlayer(score_fn=custom_score_3)
player2 = game_agent.AlphaBetaPlayer(score_fn=custom_score_3)
game = isolation.Board(player1, player2)

move_list = [(i,j) for j in range(7) for i in range(7)]
random.shuffle(move_list)
moves = random.sample(move_list, 2)

print(moves)
game.apply_move(moves[0])
game.apply_move(moves[1])
print(game.print_board())

#reload(game_agent)
# =============================================================================
# player1 = game_agent.MinimaxPlayer(search_depth = 2)
# player2 = game_agent.MinimaxPlayer(search_depth = 2)
# game = isolation.Board(player1, player2)
# game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 60]
# print(game.print_board())
# print(player1.get_move(game,time_left))
# =============================================================================
wplayer = game_agent.AlphaBetaPlayer()
moves_list = []
wreason = ''

wplayer, moves_list,wreason = game.play()
moves_list = [list(moves[1])] + moves_list
moves_list = [list(moves[0])] + moves_list

print(wplayer)
print(moves_list)
print(wreason)
print(game.print_board())



# =============================================================================
# def custom_score_3(game, player):
#     """Calculate the heuristic value of a game state from the point of view
#     of the given player.
# 
#     Note: this function should be called from within a Player instance as
#     `self.score()` -- you should not need to call this function directly.
# 
#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).
# 
#     player : object
#         A player instance in the current game (i.e., an object corresponding to
#         one of the player objects `game.__player_1__` or `game.__player_2__`.)
# 
#     Returns
#     -------
#     float
#         The heuristic value of the current game state to the specified player.
#     """
#     # TODO: finish this function!
# 
#     if game.is_loser(player):
#         return float("-inf")
# 
#     if game.is_winner(player):
#         return float("inf")
#     
#     opp = game.get_opponent(player)
#     
#     own_moves = len(game.get_legal_moves(player))
#     opp_moves = len(game.get_legal_moves(opp))
#     
#     val = float(own_moves - opp_moves)
#     
#     own_loc = game.get_player_location(player)
#     opp_loc = game.get_player_location(opp)
#     
#     if opp_loc is None:
#         return val
#     
#     r, c = opp_loc
#     directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
#                   (1, -2), (1, 2), (2, -1), (2, 1)]
#     
#     if own_loc in [(r + dr, c + dc) for dr, dc in directions]:
#         val = val * 2
#                         
#     return float(val)
# =============================================================================


# =============================================================================
# def custom_score_2(game, player):
#     """Calculate the heuristic value of a game state from the point of view
#     of the given player.
# 
#     Note: this function should be called from within a Player instance as
#     `self.score()` -- you should not need to call this function directly.
# 
#     Find the square with the least number of onward moves with the number of
#     moves greater than 0. If there is only one onward move then choose that 
#     only if the onward move cannot be blocked by the opponent
#     
#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).
# 
#     player : object
#         A player instance in the current game (i.e., an object corresponding to
#         one of the player objects `game.__player_1__` or `game.__player_2__`.)
# 
#     Returns
#     -------
#     float
#         The heuristic value of the current game state to the specified player.
#     """
#     # TODO: finish this function!
#     if game.is_loser(player):
#         return float("-inf")
# 
#     if game.is_winner(player):
#         return float("inf")
# 
#     own_moves_list = game.get_legal_moves(player)
#     own_moves = len(own_moves_list)
#     val = float(9-own_moves)
#     
#     if val == 9.0:
#         return float("-inf")
#     
#     if val == 8.0:
#         only_own_move = own_moves_list[0]
#         game_think = game.forecast_move(only_own_move)
#         if len(game_think.get_legal_moves(player)) > 0:
#             return val
#         else:
#             return float(-100)
#     else:
#         return val
# =============================================================================
