"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    ----------------------------------------------------------------------
    
    Chase or Run

    Adjust the values as per the following rules:
        If the players are on squares of different colors:
            If the player is located on one of the opponents possible move squares:
                Increase the value by a factor of number of possible opponent 
                moves by 8
        else if the players are on squares of the same color:
            If the opponent can block the player on the next move:
                Reduce the value by a factor of the number of possible moves 
                by 8
                
    The effect is that:
        If the players are on squares of opposite color, preference is given to 
        moves that block the opponent. The weight is adjusted according to the number
        of moves available to the opponent. If the opponent has less squares
        then the higher the preference to blocking the opponent
        
        If the players are on squares of the same color, then it is possible
        that the opponent can block the player on the next move. So preference 
        is given to positions where the opponent cannot play a blocking move.
        The weight is in proportion to the number of moves available to the 
        player. The effect is that the player tends to move away from the 
        opponent
        
        The difference of player moves and opponent moves then give the final
        evaluation
        
    ----------------------------------------------------------------------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

   
    opp = game.get_opponent(player)
    
    own_moves_list = game.get_legal_moves(player)
    opp_moves_list = game.get_legal_moves(opp)
    own_moves = len(own_moves_list)
    opp_moves = len(opp_moves_list)
    
    own_loc = game.get_player_location(player)
    opp_loc = game.get_player_location(opp)   
    
    if opp_loc is None:
        return float(own_moves - opp_moves)
    
    #if players are on the opposite color
    if abs(sum(own_loc)%2 - sum(opp_loc)%2) == 1:
        r, c = opp_loc
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
        
        # Adjust own_moves score if opponent is being restricted
        if own_loc in [(r + dr, c + dc) for dr, dc in directions]:
            own_moves = own_moves + own_moves * (9.-opp_moves)/8.
            
    else:
        # if players are on the same color squares
        # Reduce own_moves score if opponent can block on next move
        if len([i for i in own_moves_list if i in opp_moves_list]) != 0:
            own_moves = own_moves - own_moves * (9.-own_moves)/8.
        
    val = float(own_moves - opp_moves)
    return float(val)
  

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    ----------------------------------------------------------------------
    Least Onward Squares
    
    This idea comes from Warnsdorf's rule. 
    https://en.wikipedia.org/wiki/Knight%27s_tour
    
    The idea is to keep the knight on the board for the longest time, which
    means we try and do a knight's tour algorithm. The knight is moved so that 
    it always proceeds to the square from which the knight will have the fewest 
    onward moves.
    
    This has one issue though: the knight will try to go to a square with no
    moves. To counter this, we modify the rule a bit to find the square with
    the fewest onward moves, but only it it has at least one onward move.
    
    If there is only one onward move then choose that only if the onward move 
    cannot be blocked by the opponent
    ----------------------------------------------------------------------
   
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")
 
    if game.is_winner(player):
        return float("inf")

    own_moves_list = game.get_legal_moves(player)
    own_moves = len(own_moves_list)
    val = float(9-own_moves)
    
    if val == 9.0:
        return float("-inf")
    
    # if player has only one move left
    if val == 8.0:
        game_think = game.forecast_move(own_moves_list[0])
        opp_moves_list = game.get_legal_moves(game.get_opponent(player))
        
        # check if there is atleast one onward move
        if len(game_think.get_legal_moves(player)) > 0 :
            if len([i for i in own_moves_list if i in opp_moves_list]) == 0:
                return val
        else:
            return float(-100)

    return val
   


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    
    ----------------------------------------------------------------------
    Longer Tour
    
    This heuristic evaluates the position by comparing the length of the 
    player's knights tour and the number of open moves to that of the opponent. 
    
    The difference between the lengths + open moves of player to the 
    opponent is the value of the position.
    
    The idea is that the player seeks to retain the knight for longer on the
    board while trying to shorten the opponents knights tour length. At the 
    same time the player seeks to find the position with the mosr open moves.
    
    
    This idea comes from Warnsdorf's rule. The knight is moved so that it 
    always proceeds to the square from which the knight will have the fewest 
    onward moves.
    
    https://en.wikipedia.org/wiki/Knight%27s_tour
    ----------------------------------------------------------------------
    
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
  
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    opp = game.get_opponent(player)
    
    own_ktour_length = ktour_length(game, player)
    opp_ktour_length = ktour_length(game, opp)    
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opp))
        
    return float((own_ktour_length + own_moves) - (opp_ktour_length + opp_moves))
    


def ktour_length(game, player):
    '''
    This idea comes from Warnsdorf's rule. The knight is moved so that it 
    always proceeds to the square from which the knight will have the fewest 
    onward moves.
    
    https://en.wikipedia.org/wiki/Knight%27s_tour

    '''
    # make a copy of the game
    tmpgame = game.copy()
    ktour_length = 0
    
    while tmpgame.get_legal_moves(player):
        candidate_moves = []
        move_count = []
        tmp_moves_list = tmpgame.get_legal_moves(player)
   
        # make a list of all legal moves and the number of onward moves
        for m in tmp_moves_list:
            x = tmpgame.forecast_move(m)
            move_count.append(len(x.get_legal_moves(player)))
        
        # get a list of moves where the there is at least one onward move
        min_move_list = list(filter(lambda a: a != 0, move_count))
        if len(min_move_list) == 0:
            return ktour_length + 1
        
        
        min_move_count = min(min_move_list)
        # get a list of candidate moves which have the least onward moves
        # and have at least one onward move
        for i in range(len(move_count)):
            if move_count[i] == min_move_count:
                candidate_moves.append(tmp_moves_list[i])
        
        # choose a candidate move from the list at random 
        move = candidate_moves[random.randint(0,len(candidate_moves)-1)]
        
        #apply the move on the copy of the board
        tmpgame.apply_move(move)
        
        #apply_move switches players, so switch back players
        tmpgame._active_player, tmpgame._inactive_player = tmpgame._inactive_player, tmpgame._active_player
        
        ktour_length = ktour_length + 1
    
    return ktour_length



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        
        best_move = (-1, -1)
        
        legal_moves = game.get_legal_moves(self)
        
        if len(legal_moves) > 0:
            best_move = legal_moves[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            return best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move
    

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        # TODO: finish this function!        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()        
        
        best_score = float("-inf")
        best_move = (-1, -1)
        
        legal_moves = game.get_legal_moves(self)
        
        if len(legal_moves) > 0:
            best_move = legal_moves[0]
        
        for move in game.get_legal_moves(self):
            val = self.min_value(game.forecast_move(move), depth-1)

            if val > best_score:
                best_score = val
                best_move = move

        return best_move           


    def max_value(self, game, depth):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
    
        if depth == 0:
            val = self.score(game, self)
            return val
            
        val = float("-inf")
        for move in game.get_legal_moves(self):
            val = max(val,self.min_value(game.forecast_move(move), depth-1))
        return val

    
    def min_value(self, game, depth):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        opponent = game.get_opponent(self) 
           
        if depth == 0:
            val = self.score(game, self)
            return val
        
        val = float("inf")
        for move in game.get_legal_moves(opponent):
            val = min(val,self.max_value(game.forecast_move(move), depth-1))
        return val
    
        
class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
                
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        
        best_move = (-1, -1)
        
        legal_moves = game.get_legal_moves(self)
        
        if len(legal_moves) > 0:
            best_move = legal_moves[0]
        
        max_depth = (game.width * game.height) - game.move_count
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
        try:
            for depth in range(1, max_depth):
                best_move = self.alphabeta(game, depth)
                
        except SearchTimeout:
                return best_move

        # Return the best move from the last completed search iteration
        return best_move
        

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
       
        best_score = float("-inf")
        best_move = (-1, -1)
        
        legal_moves = game.get_legal_moves(self)
        
        if len(legal_moves) > 0:
            best_move = legal_moves[0]
            
        for move in legal_moves:
            val = self.min_value(game.forecast_move(move), alpha, beta, depth-1)

            if val > best_score:
                best_score = val
                best_move = move

            if val >= beta:
                return best_move
            alpha = max(alpha, val)
            
        return best_move     

    def max_value(self, game, alpha, beta, depth):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
                
        if depth == 0:
            val = self.score(game, self)
            return val
            
        val = float("-inf")
        for move in game.get_legal_moves(self):
            val = max(val,self.min_value(game.forecast_move(move), alpha, beta, depth-1))
            if val >= beta:
                return val
            alpha = max(alpha, val)
        return val

    def min_value(self, game, alpha, beta, depth):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
    
        opponent = game.get_opponent(self) 
           
        if depth == 0:
            val = self.score(game, self)
            return val
        
        val = float("inf")
        for move in game.get_legal_moves(opponent):
            val = min(val,self.max_value(game.forecast_move(move), alpha, beta, depth-1))
            if val <= alpha:
                return val
            beta = min(beta, val)
        return val
    
        
