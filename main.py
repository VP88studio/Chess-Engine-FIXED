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
#Row1
chess_board[1][0] = 13, 13
chess_board[1][1] = 138, 13
chess_board[1][2] = 263, 13
chess_board[1][3] = 388, 13
chess_board[1][4] = 513, 13
chess_board[1][5] = 638, 13
chess_board[1][6] = 763, 13
chess_board[1][7] = 888, 13
#Row2
chess_board[2][0] = 13, 138
chess_board[2][1] = 138, 138
chess_board[2][2] = 263, 138
chess_board[2][3] = 388, 138
chess_board[2][4] = 513, 138
chess_board[2][5] = 638, 138
chess_board[2][6] = 763, 138
chess_board[2][7] = 888, 13
#Row3
chess_board[3][0] = 13, 263
chess_board[3][1] = 138, 263
chess_board[3][2] = 263, 263
chess_board[3][3] = 388, 263
chess_board[3][4] = 513, 263
chess_board[3][5] = 638, 263
chess_board[3][6] = 763, 263
chess_board[3][7] = 888, 263
#Row4
chess_board[4][0] = 13, 388
chess_board[4][1] = 138, 388
chess_board[4][2] = 263, 388
chess_board[4][3] = 388, 388
chess_board[4][4] = 513, 388
chess_board[4][5] = 638, 388
chess_board[4][6] = 763, 388
chess_board[4][7] = 888, 388
#Row5
chess_board[5][0] = 13, 513
chess_board[5][1] = 138, 513
chess_board[5][2] = 263, 513
chess_board[5][3] = 388, 513
chess_board[5][4] = 513, 513
chess_board[5][5] = 638, 513
chess_board[5][6] = 763, 513
chess_board[5][7] = 888, 513
#Row6
chess_board[6][0] = 13, 638
chess_board[6][1] = 138, 638
chess_board[6][2] = 263, 638
chess_board[6][3] = 388, 638
chess_board[6][4] = 513, 638
chess_board[6][5] = 638, 638
chess_board[6][6] = 763, 638
chess_board[6][7] = 888, 638
#Row7
chess_board[7][0] = 13, 763
chess_board[7][1] = 138, 763
chess_board[7][2] = 263, 763
chess_board[7][3] = 388, 763
chess_board[7][4] = 513, 763
chess_board[7][5] = 638, 763
chess_board[7][6] = 763, 763
chess_board[7][7] = 888, 763
#Row8
chess_board[8][0] = 13, 888
chess_board[8][1] = 138, 888
chess_board[8][2] = 263, 888
chess_board[8][3] = 388, 888
chess_board[8][4] = 513, 888
chess_board[8][5] = 638, 888
chess_board[8][6] = 763, 888
chess_board[8][7] = 888, 888
#Peice Classes

class pawn:
    def ___init___(self):
        self
#testing area
test_bloc = {
    'x': chess_board[2][1][0],
    'y': chess_board[2][1][1],
    'width': 100,
    'height': 100,
    'color': (0, 0, 0)
}

while running:
    
    gameboard.blit(chessimg, (0,0))
    gameboard.blit(wkingimg, (test_bloc['x'], test_bloc['y']))
    pygame.display.flip()