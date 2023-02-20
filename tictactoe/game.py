import pygame
from .constants import COLS, FONTSIZE, GAMEFONT, ROWS, SQUARE_SIZE, HEIGHT, WIDTH, TEXTMARGIN_x, TEXTMARGIN_Y
from .colors import BLUE, GREY, YELLOW, WHITE, BLACK
from .board import Board

class Game:
    def __init__(self, win):
        self.turn = 1
        self.win = win
        self.gamemode = "pregame"

    def update(self,board):
        if self.gamemode != "pregame":
            board.draw_squares(self.win)
        board.update_board(self.win)
        self.claim_victory(board)
        self.end_text(board)
        pygame.display.update()
        
    def toggle_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def play(self,row,col,board):
        if not self.over(board):
            if board.check_availablity(row,col):
                board.occupy(row,col,self.turn)
                if self.check_win(board) == False:
                    self.toggle_turn()

    def reset(self,board):
        if self.over(board):
            board.initialize()
            self.gamemode = "pregame"
            self.turn = 1 #reset turn
            self.win.fill(BLACK)
            board.moves = []

    def win_condition(self, board):
        cond = 0
        player = self.turn
        board = board.board
        for col in range(COLS):
            if board[0][col] ==  player and board[1][col] == player and board[2][col] == player:
                cond = col+1
        for row in range(ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                cond = row+4
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            cond = 7
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            cond = 8
        return cond

    def check_win(self, board):
        cond = self.win_condition(board)
        return cond != 0 

    def claim_victory(self, board):
        if self.check_win(board):
            cond = self.win_condition(board)
            board.draw_winline(self.win, cond)
            self.win_text()

    def over(self, board):
        if self.check_win(board) or board.is_full():
            return True
            

    def end_text(self,board):
        if self.over(board):
            text_surface = GAMEFONT.render('GAME ENDED: PRESS SPACE TO RESET', False, BLUE)
            self.win.blit(text_surface, (0,HEIGHT/2))

    def win_text(self):
        if self.turn == 1:
            text_surface = GAMEFONT.render('RED WINS', False, BLUE)
        if self.turn == 2:
            text_surface = GAMEFONT.render('GREEN WINS', False, BLUE)
        self.win.blit(text_surface, ((WIDTH/2)-TEXTMARGIN_x,(HEIGHT/2)+ TEXTMARGIN_Y))

    def gamemode_text(self, win):
        text_vector = ['WELCOME TO TICTACTOE','PRESS 1 FOR MULTIPLAYER','PRESS 2 TO PLAY WITH AI']
        for i in range(len(text_vector)):
            PAD = (WIDTH//2)-len(text_vector[i])*0.5
            text_surface = GAMEFONT.render(text_vector[i], False, GREY)
            win.blit(text_surface, ((WIDTH//2)-PAD,(HEIGHT//2)+FONTSIZE*i))
            if self.gamemode == "pregame":
                pygame.display.update()

    def gamemode_selection(self, event):
        self.gamemode_text(self.win)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                self.gamemode = "multiplayer"
            if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                self.gamemode = "ai"

    def result(self, board):
        if self.over(board):
            if self.check_win(board) and self.turn == 1:
                return 1
            if self.check_win(board) and self.turn == 2:
                return 2
            if board.is_full():
                return 0
        else:
            return None

    def undo(self, board):
        last_move = board.moves.pop()
        if last_move: 
            board.board[last_move[0]][last_move[1]] = 0
            board.occupied_squares -= 1
            self.toggle_turn()
