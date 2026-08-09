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

#pos
for board_y in range(8):
    for board_x in range(8):
        square_y = 13 + (125 * board_y)
        square_x = 13 + (125 * board_x)

        chess_board[board_y][board_x] = (square_x, square_y)

#load imgs
chessoldimg = pygame.image.load(os.path.join("Assets/gameboard.png"))
chessimg = pygame.transform.scale(chessoldimg, (1000, 1000))
#white pieces
#King
wkingoldimg = pygame.image.load(os.path.join("Pieces/white/whiteking.png"))
wkingimg = pygame.transform.scale(wkingoldimg, (100, 100))

#Queen
wqueenoldimg = pygame.image.load(os.path.join("Pieces/white/whitequeen.png"))
wqueenimg = pygame.transform.scale(wqueenoldimg, (100, 100))

#Bishop
wbishopoldimg = pygame.image.load(os.path.join("Pieces/white/whitebishop.png"))
wbishopimg = pygame.transform.scale(wbishopoldimg, (100, 100))

#Knight
wknightoldimg = pygame.image.load(os.path.join("Pieces/white/whiteknight.png"))
wknightimg = pygame.transform.scale(wknightoldimg, (100, 100))

#Rook
wrookoldimg = pygame.image.load(os.path.join("Pieces/white/whiterook.png"))
wrookimg = pygame.transform.scale(wrookoldimg, (100, 100))

#Pawn
wpawnoldimg = pygame.image.load(os.path.join("Pieces/white/whitepawn.png"))
wpawnimg = pygame.transform.scale(wpawnoldimg, (100, 100))

#Black Pieces
#King
bkingoldimg = pygame.image.load(os.path.join("Pieces/black/blackking.png"))
bkingimg = pygame.transform.scale(bkingoldimg, (100, 100))

#Queen
bqueenoldimg = pygame.image.load(os.path.join("Pieces/black/blackqueen.png"))
bqueenimg = pygame.transform.scale(bqueenoldimg, (100, 100))

#Bishop
bbishopoldimg = pygame.image.load(os.path.join("Pieces/black/blackbishop.png"))
bbishopimg = pygame.transform.scale(bbishopoldimg, (100, 100))

#Knight
bknightoldimg = pygame.image.load(os.path.join("Pieces/black/blackknight.png"))
bknightimg = pygame.transform.scale(bknightoldimg, (100, 100))

#Rook
brookoldimg = pygame.image.load(os.path.join("Pieces/black/blackrook.png"))
brookimg = pygame.transform.scale(brookoldimg, (100, 100))

#Pawn
bpawnoldimg = pygame.image.load(os.path.join("Pieces/black/blackpawn.png"))
bpawnimg = pygame.transform.scale(bpawnoldimg, (100, 100))


pieces = {
    'white': {
        'king': {
            'load': wkingoldimg,
            'scale': wkingimg,
            'startpos': chess_board[7][4]
        },
        'queen': {
            'load': wqueenoldimg,
            'scale': wqueenimg,
            'startpos': chess_board[7][3]
        },
        'bishop': {
            'load': wbishopoldimg,
            'scale': wbishopimg,
            'startpos1': chess_board[7][2],
            'startpos2': chess_board[7][5]
        },
        'knight': {
            'load': wknightoldimg,
            'scale': wknightimg,
            'startpos1': chess_board[7][1],
            'startpos2': chess_board[7][6]
        },
        'rook': {
            'load': wrookoldimg,
            'scale': wrookimg,
            'startpos1': chess_board[7][0],
            'startpos2': chess_board[7][7]
        },
        'pawn': {
            'load': wpawnoldimg,
            'scale': wpawnimg,
            'startpos1': chess_board[6][0],
            'startpos2': chess_board[6][1],
            'startpos3': chess_board[6][2],
            'startpos4': chess_board[6][3],
            'startpos5': chess_board[6][4],
            'startpos6': chess_board[6][5],
            'startpos7': chess_board[6][6],
            'startpos8': chess_board[6][7]
        }
    },
    'black': {
        'king': {
            'load': bkingoldimg,
            'scale': bkingimg,
            'startpos': chess_board[0][4],
        },
        'queen': {
            'load': bqueenoldimg,
            'scale': bqueenimg,
            'startpos':chess_board[0][3]
        },
        'bishop': {
            'load': bbishopoldimg,
            'scale': bbishopimg,
            'startpos1': chess_board[0][2],
            'startpos2': chess_board[0][5]
        },
        'knight': {
            'load': bknightoldimg,
            'scale': bknightimg,
            'startpos1': chess_board[0][1],
            'startpos2': chess_board[0][6]
        },
        'rook': {
            'load': brookoldimg,
            'scale': brookimg,
            'startpos1': chess_board[0][0],
            'startpos2': chess_board[0][7]
        },
        'pawn': {
            'load': bpawnoldimg,
            'scale': bpawnimg,
            'startpos1': chess_board[1][0],
            'startpos2': chess_board[1][1],
            'startpos3': chess_board[1][2],
            'startpos4': chess_board[1][3],
            'startpos5': chess_board[1][4],
            'startpos6': chess_board[1][5],
            'startpos7': chess_board[1][6],
            'startpos8': chess_board[1][7]
        }
    }
    
}


while running:
    
    gameboard.blit(chessimg, (0,0))
    #white pieces temp
    gameboard.blit(pieces['white']['king']['scale'], pieces['white']['king']['startpos'])
    gameboard.blit(pieces['white']['queen']['scale'], pieces['white']['queen']['startpos'])
    gameboard.blit(pieces['white']['bishop']['scale'], pieces['white']['bishop']['startpos1'])
    gameboard.blit(pieces['white']['bishop']['scale'], pieces['white']['bishop']['startpos2'])
    gameboard.blit(pieces['white']['knight']['scale'], pieces['white']['knight']['startpos1'])
    gameboard.blit(pieces['white']['knight']['scale'], pieces['white']['knight']['startpos2'])
    gameboard.blit(pieces['white']['rook']['scale'], pieces['white']['rook']['startpos1'])
    gameboard.blit(pieces['white']['rook']['scale'], pieces['white']['rook']['startpos2'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos1'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos2'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos3'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos4'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos5'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos6'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos7'])
    gameboard.blit(pieces['white']['pawn']['scale'], pieces['white']['pawn']['startpos8'])
    #black pieces temp
    gameboard.blit(pieces['black']['king']['scale'], pieces['black']['king']['startpos'])
    gameboard.blit(pieces['black']['queen']['scale'], pieces['black']['queen']['startpos'])
    gameboard.blit(pieces['black']['bishop']['scale'], pieces['black']['bishop']['startpos1'])
    gameboard.blit(pieces['black']['bishop']['scale'], pieces['black']['bishop']['startpos2'])
    gameboard.blit(pieces['black']['knight']['scale'], pieces['black']['knight']['startpos1'])
    gameboard.blit(pieces['black']['knight']['scale'], pieces['black']['knight']['startpos2'])
    gameboard.blit(pieces['black']['rook']['scale'], pieces['black']['rook']['startpos1'])
    gameboard.blit(pieces['black']['rook']['scale'], pieces['black']['rook']['startpos2'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos1'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos2'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos3'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos4'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos5'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos6'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos7'])
    gameboard.blit(pieces['black']['pawn']['scale'], pieces['black']['pawn']['startpos8'])
    
    pygame.display.flip()