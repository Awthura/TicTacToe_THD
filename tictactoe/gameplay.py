import pygame
from .game import Game
from .board import Board
from .ai import AI



class Gameplay:
    def __init__(self, win):
        self.win = win
        self.game = Game(self.win)
        self.board = Board()
        self.ai = AI()

    def multiplayer_gameplay(self, event, board, game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            row, col = board.catch_coordinate(event.pos[0],event.pos[1])
            game.play(row,col,board)

    def ai_gameplay(self, event, board, game, ai):
        if game.turn != ai.turn:
            self.multiplayer_gameplay(event, board, game)
        if game.turn == ai.turn:
            if board.state == "not_full":
                row, col = ai.play_turn(board, game)
                game.play(row,col,board)