import pygame
import numpy as np
import copy
from .board import Board 
from .game import Game
from .constants import ROWS, COLS
import math

class AI:

    def __init__(self, level =1 , turn =1): # level = 1 for random ai, 2 for minimax
        self.level = level
        self.turn = turn

    def random_pick(self, board):
        available_squares = np.array(board.available_squares())
        if not board.is_full():
            idx = np.random.choice(available_squares.shape[0], replace= False)
            pick = available_squares[idx]
            return pick
        
    def play_turn(self, board, game):
        if self.level == 1:
            pick = self.random_pick(board)
        if self.level == 2:
            pick = self.make_best_move(board, game)
        return pick

    def minimax(self, isMaxTurn, maximizerMark, board, game):
        state = game.result(board)
        if state != None:
            if (state == 0):
                return 0
            elif (state != 0):
                return 1 if game.result(board) == maximizerMark else -1

        scores = []
        for move in board.available_squares():
            board.occupy(move[0],move[1], game.turn)
            scores.append(self.minimax(not isMaxTurn, maximizerMark, board, game))
            game.undo(board)
        return max(scores) if isMaxTurn else min(scores)

    def make_best_move(self, board, game):
        bestScore = -math.inf
        bestMove = None
        for move in board.available_squares():
            board.occupy(move[0],move[1], game.turn)
            score = self.minimax(False, self.turn, board, game)
            game.undo(board)
            if (score > bestScore):
                bestScore = score
                bestMove = move
        return bestMove