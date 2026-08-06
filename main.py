'''github save if my dumbass cant remember
git add .
git commit -m "Fixing repo and adding latest updates"
git push origin main'''

import pygame, math, time, sys, os
WIDTH = 1000
HEIGHT = 1000
gameboard = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
#load imgs
chessoldimg = pygame.image.load(os.path.join("Assets/gameboard.png"))
chessimg = pygame.transform.scale(chessoldimg, (1000, 1000))
wkingoldimg = pygame.image.load(os.path.join("Pieces/white/whiteking.svg"))
wkingimg = pygame.transform.scale(wkingoldimg, (100, 100))

#chess board nested list

chess_board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

#chess board pos allocation
                        #Cords Here
chess_board[1][0] = 13, 13
chess_board[1][1] = 138, 13
chess_board[1][2] = 263, 13
chess_board[1][3] = 350, 13
chess_board[1][4] = 450, 13
chess_board[1][5] = 550, 13
chess_board[1][6] = 650, 13
chess_board[1][7] = 750, 13
print('x', chess_board[1][0][0])
print('y', chess_board[1][0][1])

#Peice Classes

class pawn:
    def ___init___(self):
        self
#testing area
test_bloc = {
    'x': chess_board[1][2][0],
    'y': chess_board[1][2][1],
    'width': 100,
    'height': 100,
    'color': (0, 0, 0)
}

while running:
    
    gameboard.blit(chessimg, (0,0))
    gameboard.blit(wkingimg, (test_bloc['x'], test_bloc['y']))
    pygame.display.flip()