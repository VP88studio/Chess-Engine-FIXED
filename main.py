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
#white pieces
wkingoldimg = pygame.image.load(os.path.join("Pieces/white/whiteking.png"))
wkingimg = pygame.transform.scale(wkingoldimg, (100, 100))
wqueenoldimg = pygame.image.load(os.path.join("Pieces/white/whitequeen.png"))
wqueenimg = pygame.transform.scale(wqueenoldimg, (100, 100))
wleftbishopoldimg = pygame.image.load(os.path.join("Pieces/white/whitebishop.png"))
wleftbishopimg = pygame.transform.scale(wleftbishopoldimg, (100, 100))
wrightbishopoldimg = pygame.image.load(os.path.join("Pieces/white/whitebishop.png"))
wrightbishopimg = pygame.transform.scale(wrightbishopoldimg, (100, 100))
wleftknightoldimg = pygame.image.load(os.path.join("Pieces/white/whiteknight.png"))
wleftknightimg = pygame.transform.scale(wleftknightoldimg, (100, 100))
wrightknightoldimg = pygame.image.load(os.path.join("Pieces/white/whiteknight.png"))

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

for board_y in range(8):
    for board_x in range(8):
        square_y = 13 + (125 * board_y)
        square_x = 13 + (125 * board_x)

        chess_board[board_y][board_x] = (square_x, square_y)


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