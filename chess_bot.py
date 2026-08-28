import math
from optparse import BadOptionError
from sys import exception, exec_prefix

class chess:
    def __init__(self):
        
        # Positive: White
        # Negative: Black
        
        # 1: Pawn
        # 0: Nothing
        # 2: Knight
        # 3: Bishopit 
        # 4: Rook
        # 5: Queen
        # 6: King
        
        
        self.board = [[0 for _ in range (8)] for _ in range (8)]
        
        # Pawns
        self.board[1] = [1 for _ in range (8)]
        self.board[7] = [-1 for _ in range (8)]
        
        # Rooks
        self.board[0][0] = 4
        self.board[0][7] = 4
        self.board[7][0] = -4
        self.board[7][7] = -4
        
        #Knights
        self.board[0][1] = 2
        self.board[0][6] = 2
        self.board[7][1] = -2
        self.board[7][6] = -2
        
        # Bishops
        self.board[0][2] = 3
        self.board[0][5] = 3
        self.board[7][2] = -3
        self.board[7][5] = -3
        
        # Kings
        self.board[0][4] = 6
        self.board[8][4] = -6
        
        # Queens
        self.board[0][3] = 5
        self.board[7][3] = -5
        
        # 0: White
        # 1: Black
        self.turn = 0
        
    def move(self, move):
        
        # Piece pos
        px = math.floor(move/1000)
        move -= px*1000
        py = math.floor(move/100)
        move -= py*1000
        
        # Piece move
        mx = math.floor(move/10)
        move -= mx*10
        my = move
        
        piece = self.board[px][py]


        
        if math.ceil(piece/6) == self.turn:
            match piece:
                case 0: raise ValueError("No piece at start point")
                case 1: # White Pawn
                    if my == py+1: # Pawn moves forward 1
                        match abs(mx-px): # Check if taking piece
                            case 1: # Is taking piece
                                if self.board[mx][my] < 0: # Is there a black piece at the point its going to
                                    self.board[mx][my] = self.board[px][py] # Place piece at that point
                                    self.board[px][py] = 0
                                else: # No piece at taking point
                                    raise BadOptionError("Illigal move")
                            case 0: # Not taking piece
                                if self.board[mx][my] == 0: # Is there a piece in the way
                                    self.board[mx][my] = self.board[px][py] # Place piece at that point
                                    self.board[px][py] = 0
                                else: # Piece in the way
                                    raise BadOptionError(" Piece in way")
                    elif my == py+2 and py == 1: # Pawn is moving 2 spaces
                        if self.board[mx][my] == 0:
                            self.board[mx][my] = self.board[px][py]
                            self.board[px][py] = 0
                        else:
                            raise BadOptionError(" Piece in way")
                    else:
                        raise BadOptionError("Illigal move")
                        
                case -1:
                    if my == py-1:
                        match abs(mx-px):
                            case 1:
                                if self.board[mx][my] > 0:
                                    self.board[mx][my] = self.board[px][py]
                                    self.board[px][py] = 0
                                else:
                                    raise BadOptionError("Illigal move")
                            case 0:
                                if self.board[mx][my] == 0:
                                    self.board[mx][my] = self.board[px][py]
                                    self.board[px][py] = 0
                                else:
                                    raise BadOptionError(" Piece in way")
                    elif my == py-2 and py == 6:
                        if self.board[mx][my] == 0:
                            self.board[mx][my] = self.board[px][py]
                            self.board[px][py] = 0
                        else:
                            raise BadOptionError(" Piece in way")
                    else:
                        raise BadOptionError("Illigal move")
                    
                case 2:
                    if sorted((abs(px-mx), abs(py-my))) == (1, 2):
                        if 0 <= mx <= 7 and 0 <= my <= 7:
                            if self.board[mx][my] >= 0:
                                self.board[mx][my] = self.board[px][py]
                                self.board[px][py] = 0
                            else:
                                raise BadOptionError(" Piece in way")
                        else:
                            raise BadOptionError(" Piece in way")
                    else:
                        raise BadOptionError("Illigal move")
                        
                case -1:
                    if my == py-1:
                        match abs(mx-px):
                            case 1:
                                if self.board[mx][my] > 0:
                                    self.board[mx][my] = self.board[px][py]
                                    self.board[px][py] = 0
                                else:
                                    raise BadOptionError("Illigal move")
                            case 0:
                                if self.board[mx][my] == 0:
                                    self.board[mx][my] = self.board[px][py]
                                    self.board[px][py] = 0
                                else:
                                    raise BadOptionError(" Piece in way")
                    elif my == py-2 and py == 6:
                        if self.board[mx][my] == 0:
                            self.board[mx][my] = self.board[px][py]
                            self.board[px][py] = 0
                        else:
                            raise BadOptionError(" Piece in way")
                    else:
                        raise BadOptionError("Illigal move")
                    
                case 2:
                    if sorted((abs(px-mx), abs(py-my))) == (1, 2):
                        if 0 <= mx <= 7 and 0 <= my <= 7:
                            if self.board[mx][my] >= 0:
                                self.board[mx][my] = self.board[px][py]
                                self.board[px][py] = 0
                            else:
                                raise BadOptionError("Illigal move")
                        else:
                            raise BadOptionError("Illigal move")
                    else:
                        raise BadOptionError("Illigal move")