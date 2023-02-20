import pygame
from tictactoe import WIDTH,HEIGHT
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.ai import AI
from tictactoe.gameplay import Gameplay

#Initiallize pygame
pygame.init()

#Create a display
FPS = 60
GAMESCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

#Main Loop
def main():

    infiniteLoop = True
    clock = pygame.time.Clock()
    board = Board()
    ai = AI()
    game = Game(GAMESCREEN)
    gameplay = Gameplay(GAMESCREEN)
    
    while infiniteLoop:
        clock.tick(FPS)
        for event in pygame.event.get():
            game.gamemode_selection(event)
            if event.type == pygame.QUIT:
                infiniteLoop = False
            if game.gamemode == "multiplayer":
                gameplay.multiplayer_gameplay(event, board, game)

            if game.gamemode == "ai":
                gameplay.ai_gameplay(event, board, game, ai)

            if game.gamemode != "pregame":
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE: # press space to reset
                        game.reset(board)
                game.update(board)

    pygame.quit()


#Run the game
main()