'''github save if my dumbass cant remember
git add .
git commit -m "Fixing repo and adding latest updates"
git push origin main'''

import pygame, math, time, sys, os
import imgrenderer
from PieceClasses.pawnclass import pawn
from PieceClasses.rookclass import rook
from PieceClasses.queenclass import queen
from PieceClasses.kingclass import king
WIDTH = 1000
HEIGHT = 1000
gameboard = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
imgrenderer.loadimgs()
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

#rects
rect_00 = pygame.Rect((chess_board[0][0]), (100, 100))
rect_01 = pygame.Rect((chess_board[0][1]), (100, 100))
rect_02 = pygame.Rect((chess_board[0][2]), (100, 100))
rect_03 = pygame.Rect((chess_board[0][3]), (100, 100))
rect_04 = pygame.Rect((chess_board[0][4]), (100, 100))
rect_05 = pygame.Rect((chess_board[0][5]), (100, 100))
rect_06 = pygame.Rect((chess_board[0][6]), (100, 100))
rect_07 = pygame.Rect((chess_board[0][7]), (100, 100))
rect_10 = pygame.Rect((chess_board[1][0]), (100, 100))
rect_11 = pygame.Rect((chess_board[1][1]), (100, 100))
rect_12 = pygame.Rect((chess_board[1][2]), (100, 100))
rect_13 = pygame.Rect((chess_board[1][3]), (100, 100))
rect_14 = pygame.Rect((chess_board[1][4]), (100, 100))
rect_15 = pygame.Rect((chess_board[1][5]), (100, 100))
rect_16 = pygame.Rect((chess_board[1][6]), (100, 100))
rect_17 = pygame.Rect((chess_board[1][7]), (100, 100))
rect_20 = pygame.Rect((chess_board[2][0]), (100, 100))
rect_21 = pygame.Rect((chess_board[2][1]), (100, 100))
rect_22 = pygame.Rect((chess_board[2][2]), (100, 100))
rect_23 = pygame.Rect((chess_board[2][3]), (100, 100))
rect_24 = pygame.Rect((chess_board[2][4]), (100, 100))
rect_25 = pygame.Rect((chess_board[2][5]), (100, 100))
rect_26 = pygame.Rect((chess_board[2][6]), (100, 100))
rect_27 = pygame.Rect((chess_board[2][7]), (100, 100))
rect_30 = pygame.Rect((chess_board[3][0]), (100, 100))
rect_31 = pygame.Rect((chess_board[3][1]), (100, 100))
rect_32 = pygame.Rect((chess_board[3][2]), (100, 100))
rect_33 = pygame.Rect((chess_board[3][3]), (100, 100))
rect_34 = pygame.Rect((chess_board[3][4]), (100, 100))
rect_35 = pygame.Rect((chess_board[3][5]), (100, 100))
rect_36 = pygame.Rect((chess_board[3][6]), (100, 100))
rect_37 = pygame.Rect((chess_board[3][7]), (100, 100))
rect_40 = pygame.Rect((chess_board[4][0]), (100, 100))
rect_41 = pygame.Rect((chess_board[4][1]), (100, 100))
rect_42 = pygame.Rect((chess_board[4][2]), (100, 100))
rect_43 = pygame.Rect((chess_board[4][3]), (100, 100))
rect_44 = pygame.Rect((chess_board[4][4]), (100, 100))
rect_45 = pygame.Rect((chess_board[4][5]), (100, 100))
rect_46 = pygame.Rect((chess_board[4][6]), (100, 100))
rect_47 = pygame.Rect((chess_board[4][7]), (100, 100))
rect_50 = pygame.Rect((chess_board[5][0]), (100, 100))
rect_51 = pygame.Rect((chess_board[5][1]), (100, 100))
rect_52 = pygame.Rect((chess_board[5][2]), (100, 100))
rect_53 = pygame.Rect((chess_board[5][3]), (100, 100))
rect_54 = pygame.Rect((chess_board[5][4]), (100, 100))
rect_55 = pygame.Rect((chess_board[5][5]), (100, 100))
rect_56 = pygame.Rect((chess_board[5][6]), (100, 100))
rect_57 = pygame.Rect((chess_board[5][7]), (100, 100))
rect_60 = pygame.Rect((chess_board[6][0]), (100, 100))
rect_61 = pygame.Rect((chess_board[6][1]), (100, 100))
rect_62 = pygame.Rect((chess_board[6][2]), (100, 100))
rect_63 = pygame.Rect((chess_board[6][3]), (100, 100))
rect_64 = pygame.Rect((chess_board[6][4]), (100, 100))
rect_65 = pygame.Rect((chess_board[6][5]), (100, 100))
rect_66 = pygame.Rect((chess_board[6][6]), (100, 100))
rect_67 = pygame.Rect((chess_board[6][7]), (100, 100))
rect_70 = pygame.Rect((chess_board[7][0]), (100, 100))
rect_71 = pygame.Rect((chess_board[7][1]), (100, 100))
rect_72 = pygame.Rect((chess_board[7][2]), (100, 100))
rect_73 = pygame.Rect((chess_board[7][3]), (100, 100))
rect_74 = pygame.Rect((chess_board[7][4]), (100, 100))
rect_75 = pygame.Rect((chess_board[1][5]), (100, 100))
rect_76 = pygame.Rect((chess_board[7][6]), (100, 100))
rect_77 = pygame.Rect((chess_board[7][7]), (100, 100))
pieces = {
    'white': {
        'king': {
            'img': imgrenderer.wkingimg,
            'startpos': chess_board[7][4]
        },
        'queen': {
            'img': imgrenderer.wqueenimg,
            'startpos': chess_board[7][3]
        },
        'bishop': {
            'img': imgrenderer.wbishopimg,
            'startpos1': chess_board[7][2],
            'startpos2': chess_board[7][5]
        },
        'knight': {
            'img': imgrenderer.wknightimg,
            'startpos1': chess_board[7][1],
            'startpos2': chess_board[7][6]
        },
        'rook': {
            'img': imgrenderer.wrookimg,
            'startpos1': chess_board[7][0],
            'startpos2': chess_board[7][7]
        },
        'pawn': {
            'img': imgrenderer.wpawnimg,
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
            'img': imgrenderer.bkingimg,
            'startpos': chess_board[0][4],
        },
        'queen': {
            'img': imgrenderer.bqueenimg,
            'startpos':chess_board[0][3]
        },
        'bishop': {
            'img': imgrenderer.bbishopimg,
            'startpos1': chess_board[0][2],
            'startpos2': chess_board[0][5]
        },
        'knight': {
            'img': imgrenderer.bknightimg,
            'startpos1': chess_board[0][1],
            'startpos2': chess_board[0][6]
        },
        'rook': {
            'img': imgrenderer.brookimg,
            'startpos1': chess_board[0][0],
            'startpos2': chess_board[0][7]
        },
        'pawn': {
            'img': imgrenderer.bpawnimg,
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

#bpawn1
bpawn1 = pawn()
bpawn1.pos = chess_board[1][0]
bpawn1.color = 0
#bpawn2
bpawn2 = pawn()
bpawn2.pos = chess_board[1][1]
bpawn2.color = 0
#bpawn3
bpawn3 = pawn()
bpawn3.pos = chess_board[1][2]
bpawn3.color = 0
#bpawn4
bpawn4 = pawn()
bpawn4.pos = chess_board[1][3]
bpawn4.color = 0
#bpawn5
bpawn5 = pawn()
bpawn5.pos = chess_board[1][4]
bpawn5.color = 0
#bpawn6
bpawn6 = pawn()
bpawn6.pos = chess_board[1][5]
bpawn6.color = 0
#bpawn7
bpawn7 = pawn()
bpawn7.pos = chess_board[1][6]
bpawn7.color = 0
#bpawn8
bpawn8 = pawn()
bpawn8.pos = chess_board[1][7]
bpawn8.color = 0
if bpawn1.color == 0:
    bpawn1.img = imgrenderer.bpawnimg
if bpawn2.color == 0:
    bpawn2.img = imgrenderer.bpawnimg
if bpawn3.color == 0:
    bpawn3.img = imgrenderer.bpawnimg
if bpawn4.color == 0:
    bpawn4.img = imgrenderer.bpawnimg
if bpawn5.color == 0:
    bpawn5.img = imgrenderer.bpawnimg
if bpawn6.color == 0:
    bpawn6.img = imgrenderer.bpawnimg
if bpawn7.color == 0:
    bpawn7.img = imgrenderer.bpawnimg
if bpawn8.color == 0:
    bpawn8.img = imgrenderer.bpawnimg
#wpawn1
wpawn1 = pawn()
wpawn1.pos = chess_board[1][0]
wpawn1.color = 0
#wpawn2
wpawn2 = pawn()
wpawn2.pos = chess_board[1][1]
wpawn2.color = 0
#wpawn3
wpawn3 = pawn()
wpawn3.pos = chess_board[1][2]
wpawn3.color = 0
#wpawn4
wpawn4 = pawn()
wpawn4.pos = chess_board[1][3]
wpawn4.color = 0
#wpawn5
wpawn5 = pawn()
wpawn5.pos = chess_board[1][4]
wpawn5.color = 0
#wpawn6
wpawn6 = pawn()
wpawn6.pos = chess_board[1][5]
wpawn6.color = 0
#wpawn7
wpawn7 = pawn()
wpawn7.pos = chess_board[1][6]
wpawn7.color = 0
#wpawn8
wpawn8 = pawn()
wpawn8.pos = chess_board[1][7]
wpawn8.color = 0
if wpawn1.color == 0:
    wpawn1.img = imgrenderer.wpawnimg
if wpawn2.color == 0:
    wpawn2.img = imgrenderer.wpawnimg
if wpawn3.color == 0:
    wpawn3.img = imgrenderer.wpawnimg
if wpawn4.color == 0:
    wpawn4.img = imgrenderer.wpawnimg
if wpawn5.color == 0:
    wpawn5.img = imgrenderer.wpawnimg
if wpawn6.color == 0:
    wpawn6.img = imgrenderer.wpawnimg
if wpawn7.color == 0:
    wpawn7.img = imgrenderer.wpawnimg
if wpawn8.color == 0:
    wpawn8.img = imgrenderer.wpawnimg
def sendtopos():
    gameboard.blit(imgrenderer.chessimg, (0,0))
    gameboard.blit(pieces['white']['king']['img'], pieces['white']['king']['startpos'])
    gameboard.blit(pieces['white']['queen']['img'], pieces['white']['queen']['startpos'])
    gameboard.blit(pieces['white']['bishop']['img'], pieces['white']['bishop']['startpos1'])
    gameboard.blit(pieces['white']['bishop']['img'], pieces['white']['bishop']['startpos2'])
    gameboard.blit(pieces['white']['knight']['img'], pieces['white']['knight']['startpos1'])
    gameboard.blit(pieces['white']['knight']['img'], pieces['white']['knight']['startpos2'])
    gameboard.blit(pieces['white']['rook']['img'], pieces['white']['rook']['startpos1'])
    gameboard.blit(pieces['white']['rook']['img'], pieces['white']['rook']['startpos2'])
    gameboard.blit(wpawn1.img, wpawn1.pos)
    gameboard.blit(wpawn2.img, wpawn2.pos)
    gameboard.blit(wpawn3.img, wpawn3.pos)
    gameboard.blit(wpawn4.img, wpawn4.pos)
    gameboard.blit(wpawn5.img, wpawn5.pos)
    gameboard.blit(wpawn6.img, wpawn6.pos)
    gameboard.blit(wpawn7.img, wpawn7.pos)
    gameboard.blit(wpawn8.img, wpawn8.pos)
    #black pieces temp
    gameboard.blit(pieces['black']['king']['img'], pieces['black']['king']['startpos'])
    gameboard.blit(pieces['black']['queen']['img'], pieces['black']['queen']['startpos'])
    gameboard.blit(pieces['black']['bishop']['img'], pieces['black']['bishop']['startpos1'])
    gameboard.blit(pieces['black']['bishop']['img'], pieces['black']['bishop']['startpos2'])
    gameboard.blit(pieces['black']['knight']['img'], pieces['black']['knight']['startpos1'])
    gameboard.blit(pieces['black']['knight']['img'], pieces['black']['knight']['startpos2'])
    gameboard.blit(pieces['black']['rook']['img'], pieces['black']['rook']['startpos1'])
    gameboard.blit(pieces['black']['rook']['img'], pieces['black']['rook']['startpos2'])
    gameboard.blit(bpawn1.img, bpawn1.pos)
    gameboard.blit(bpawn2.img, bpawn2.pos)
    gameboard.blit(bpawn3.img, bpawn3.pos)
    gameboard.blit(bpawn4.img, bpawn4.pos)
    gameboard.blit(bpawn5.img, bpawn5.pos)
    gameboard.blit(bpawn6.img, bpawn6.pos)
    gameboard.blit(bpawn7.img, bpawn7.pos)
    gameboard.blit(bpawn8.img, bpawn8.pos)
    #test rects
    pygame.draw.rect(gameboard, (0,0,255), rect_34)
    print(chess_board)
sendtopos()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    pygame.display.flip()