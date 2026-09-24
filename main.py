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
from PieceClasses.bishopclass import bishop
from PieceClasses.knightclass import knight
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
#bking1
bking1 = king()
bking1.pos = chess_board[0][4]
bking1.color = 0
if bking1.color == 0:
    bking1.img = imgrenderer.bkingimg
#bqueen1
bqueen1 = queen()
bqueen1.pos = chess_board[0][3]
bqueen1.color = 0
if bqueen1.color == 0:
    bqueen1.img = imgrenderer.bqueenimg
#bbishop1
bbishop1 = bishop()
bbishop1.pos = chess_board[0][2]
bbishop1.color = 0
if bbishop1.color == 0:
    bbishop1.img = imgrenderer.bbishopimg
#bbishop2
bbishop2 = bishop()
bbishop2.pos = chess_board[0][5]
bbishop2.color = 0
if bbishop2.color == 0:
    bbishop2.img = imgrenderer.bbishopimg
#knight1
bknight1 = knight()
bknight1.pos = chess_board[0][1]
bknight1.color = 0
if bknight1.color == 0:
    bknight1.img = imgrenderer.bknightimg
#knight2
bknight2 = knight()
bknight2.pos = chess_board[0][6]
bknight2.color = 0
if bknight2.color == 0:
    bknight2.img = imgrenderer.bknightimg
#rook1
brook1 = rook()
brook1.pos = chess_board[0][7]
brook1.color = 0
if brook1.color == 0:
    brook1.img = imgrenderer.brookimg
#rook2
brook2 = rook()
brook2.pos = chess_board[0][0]
brook2.color = 0
if brook2.color == 0:
    brook2.img = imgrenderer.brookimg
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




#White
#bking1
wking1 = king()
wking1.pos = chess_board[7][4]
wking1.color = 1
if wking1.color == 1:
    wking1.img = imgrenderer.wkingimg  
#bqueen1
wqueen1 = queen()
wqueen1.pos = chess_board[7][3]
wqueen1.color = 1
if wqueen1.color == 1:
    wqueen1.img = imgrenderer.wqueenimg
#bbishop1
wbishop1 = bishop()
wbishop1.pos = chess_board[7][2]
wbishop1.color = 1
if wbishop1.color == 1:
    wbishop1.img = imgrenderer.wbishopimg
#bbishop2
wbishop2 = bishop()
wbishop2.pos = chess_board[7][5]
wbishop2.color = 1
if wbishop2.color == 1:
    wbishop2.img = imgrenderer.wbishopimg
#knight1
wknight1 = knight()
wknight1.pos = chess_board[7][1]
wknight1.color = 1
if wknight1.color == 1:
    wknight1.img = imgrenderer.wknightimg
#knight2
wknight2 = knight()
wknight2.pos = chess_board[7][6]
wknight2.color = 1
if wknight2.color == 1:
    wknight2.img = imgrenderer.wknightimg
#rook1
wrook1 = rook()
wrook1.pos = chess_board[7][7]
wrook1.color = 1
if wrook1.color == 1:
    wrook1.img = imgrenderer.wrookimg
#rook2
wrook2 = rook()
wrook2.pos = chess_board[7][0]
wrook2.color = 1
if wrook2.color == 1:
    wrook2.img = imgrenderer.wrookimg
#wpawn1
wpawn1 = pawn()
wpawn1.pos = chess_board[6][0]
wpawn1.color = 0
#wpawn2
wpawn2 = pawn()
wpawn2.pos = chess_board[6][1]
wpawn2.color = 0
#wpawn3
wpawn3 = pawn()
wpawn3.pos = chess_board[6][2]
wpawn3.color = 0
#wpawn4
wpawn4 = pawn()
wpawn4.pos = chess_board[6][3]
wpawn4.color = 0
#wpawn5
wpawn5 = pawn()
wpawn5.pos = chess_board[6][4]
wpawn5.color = 0
#wpawn6
wpawn6 = pawn()
wpawn6.pos = chess_board[6][5]
wpawn6.color = 0
#wpawn7
wpawn7 = pawn()
wpawn7.pos = chess_board[6][6]
wpawn7.color = 0
#wpawn8
wpawn8 = pawn()
wpawn8.pos = chess_board[6][7]
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
    gameboard.blit(wking1.img, wking1.pos)
    gameboard.blit(wqueen1.img, wqueen1.pos)
    gameboard.blit(wbishop1.img, wbishop1.pos)
    gameboard.blit(wbishop2.img, wbishop2.pos)
    gameboard.blit(wknight1.img, wknight1.pos)
    gameboard.blit(wknight2.img, wknight2.pos)
    gameboard.blit(wrook1.img, wrook1.pos)
    gameboard.blit(wrook2.img, wrook2.pos)
    gameboard.blit(wpawn1.img, wpawn1.pos)
    gameboard.blit(wpawn2.img, wpawn2.pos)
    gameboard.blit(wpawn3.img, wpawn3.pos)
    gameboard.blit(wpawn4.img, wpawn4.pos)
    gameboard.blit(wpawn5.img, wpawn5.pos)
    gameboard.blit(wpawn6.img, wpawn6.pos)
    gameboard.blit(wpawn7.img, wpawn7.pos)
    gameboard.blit(wpawn8.img, wpawn8.pos)
    #black pieces temp
    gameboard.blit(bking1.img, bking1.pos)
    gameboard.blit(bqueen1.img, bqueen1.pos)
    gameboard.blit(bbishop1.img, bbishop1.pos)
    gameboard.blit(bbishop2.img, bbishop2.pos)
    gameboard.blit(bknight1.img, bknight1.pos)
    gameboard.blit(bknight2.img, bknight2.pos)
    gameboard.blit(brook1.img, brook1.pos)
    gameboard.blit(brook2.img, brook2.pos)
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
    print(bpawn1.pos)
sendtopos()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    pygame.display.flip()