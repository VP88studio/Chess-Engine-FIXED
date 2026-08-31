import math
from optparse import BadOptionError
from sys import exception, exec_prefix

class chess:
    def __init__(self):
        
        # Positive: White
        # Negative: Black
        
        # 0: Nothing
        # 1: Pawn
        # 2: Knight
        # 3: Bishop
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
        
    def _intState(x):
        return (-1 if x < 0 else (1 if x > 0 else 0))
        
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
                    if sorted((abs(px-mx), abs(py-my))) == (1, 2): # If knight is moving 1 square in one direction and 2 in the other
                        if 0 <= mx <= 7 and 0 <= my <= 7: # Destination in Bounds
                            if self.board[mx][my] <= 0: # No piece in way/Takeable piece in way
                                self.board[mx][my] = self.board[px][py] # Place piece at that point
                                self.board[px][py] = 0
                            else:
                                raise BadOptionError(" Piece in way")
                        else:
                            raise BadOptionError(" Out of bounds")
                    else:
                        raise BadOptionError("Illigal move")
                    
                case -2:
                    if sorted((abs(px-mx), abs(py-my))) == (1, 2):
                        if 0 <= mx <= 7 and 0 <= my <= 7:
                            if self.board[mx][my] >= 0:
                                self.board[mx][my] = self.board[px][py]
                                self.board[px][py] = 0
                            else:
                                raise BadOptionError(" Piece in way")
                        else:
                            raise BadOptionError(" Out of bounds")
                    else:
                        raise BadOptionError("Illigal move")
                    
                case 4:
                    if 0 <= mx <= 7 and 0 <= my <= 7: # Destination in Bounds
                        match (self._intState(mx-px), self._intState(my-py)):
                            case (1, 0): # Going left
                                if [self.board[px+1+i][py] for i in range ((px-mx)-2)] == [0 for _ in range ((px-mx)-2)]: # Any pieces in way
                                    if self.board[mx][my] <= 0: # Is it taking the correct piece
                                        self.board[mx][my] = self.board[px][py] # Place piece at that point
                                        self.board[px][py] = 0
                                    else:
                                        raise BadOptionError(" Piece in way")
                                else:
                                    raise BadOptionError("Illigal move")
                            case (-1, 0):
                                self.board.reverse()
                                if [self.board[px+1+i][py] for i in range ((px-mx)-2)] == [0 for _ in range ((px-mx)-2)]:
                                    if self.board[mx][my] <= 0:
                                        self.board[mx][my] = self.board[px][py]
                                        self.board[px][py] = 0
                                    else:
                                        self.board.reverse()
                                        raise BadOptionError(" Piece in way")
                                else:
                                    self.board.reverse()
                                    raise BadOptionError("Illigal move")
                                self.board.reverse()
                            
                            case (0, 1):
                                if [self.board[px][py+1+i] for i in range ((py-my)-2)] == [0 for _ in range ((py-my)-2)]:
                                    if self.board[mx][my] <= 0:
                                        self.board[mx][my] = self.board[px][py]
                                        self.board[px][py] = 0
                                    else:
                                        raise BadOptionError(" Piece in way")
                                else:
                                    raise BadOptionError("Illigal move")
                            case (0, -1): # Going Up
                                self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                if [self.board[px][py+1+i] for i in range ((py-my)-2)] == [0 for _ in range ((py-my)-2)]:
                                    if self.board[mx][my] <= 0:
                                        self.board[mx][my] = self.board[px][py]
                                        self.board[px][py] = 0
                                    else:
                                        self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                        raise BadOptionError(" Piece in way")
                                else:
                                    self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                    raise BadOptionError("Illigal move")
                            case _:
                                raise BadOptionError("Illigal move")
                            
                case -4:
                    if 0 <= mx <= 7 and 0 <= my <= 7: # Destination in Bounds
                        match (self._intState(mx-px), self._intState(my-py)):
                            case (1, 0): # Going left
                                if [self.board[px+1+i][py] for i in range ((px-mx)-2)] == [0 for _ in range ((px-mx)-2)]: # Any pieces in way
                                    if self.board[mx][my] >= 0: # Is it taking the correct piece
                                        self.board[mx][my] = self.board[px][py] # Place piece at that point
                                        self.board[px][py] = 0
                                    else:
                                        raise BadOptionError(" Piece in way")
                                else:
                                    raise BadOptionError("Illigal move")
                            case (-1, 0): # Going Right
                                self.board.reverse()
                                if [self.board[px+1+i][py] for i in range ((px-mx)-2)] == [0 for _ in range ((px-mx)-2)]:
                                    if self.board[mx][my] >= 0:
                                        self.board[mx][my] = self.board[px][py]
                                        self.board[px][py] = 0
                                    else:
                                        self.board.reverse()
                                        raise BadOptionError(" Piece in way")
                                else:
                                    self.board.reverse()
                                    raise BadOptionError("Illigal move")
                                self.board.reverse()
                            
                            case (0, 1): # Going Down
                                if [self.board[px][py+1+i] for i in range ((py-my)-2)] == [0 for _ in range ((py-my)-2)]:
                                    if self.board[mx][my] >= 0:
                                        self.board[mx][my] = self.board[px][py]
                                        self.board[px][py] = 0
                                    else:
                                        raise BadOptionError(" Piece in way")
                                else:
                                    raise BadOptionError("Illigal move")
                            case (0, -1): # Going Up
                                my = 7-my
                                py = 7-py
                                self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                if [self.board[px][py+1+i] for i in range ((py-my)-2)] == [0 for _ in range ((py-my)-2)]:
                                    if self.board[mx][my] >= 0:
                                        self.board[mx][my] = self.board[px][py]
                                        self.board[px][py] = 0
                                    else:
                                        self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                        raise BadOptionError(" Piece in way")
                                else:
                                    self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                    raise BadOptionError("Illigal move")
                                self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                            case _:
                                raise BadOptionError("Illigal move")
                            
                case 3:
                    if 0 <= mx <= 7 and 0 <= my <= 7:
                        dx = mx-px
                        dy = my-py
                        if abs(dx) == abs(dy): # Going diagonally                            
                            match (self._intState(dx), self._intState(dy)):
                                case (1, 1): # Going Down left
                                    if [self.board[px+1+i][py+1+i] for i in range ((px-mx)-2)] == [0 for _ in range ((px-mx)-2)]: # Any pieces in way
                                        if self.board[mx][my] <= 0: # Is it taking the correct piece
                                            self.board[mx][my] = self.board[px][py] # Place piece at that point
                                            self.board[px][py] = 0
                                        else:
                                            raise BadOptionError(" Piece in way")
                                    else:
                                        raise BadOptionError("Illigal move")
                                case (1, -1): # Going Up Right
                                    self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                    my = 7-my
                                    py = 7-py
                                    
                                    if [self.board[px+1+i][py+1+i] for i in range ((px-mx)-2)] == [0 for _ in range ((px-mx)-2)]: # Any pieces in way
                                        self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                        if self.board[mx][my] <= 0: # Is it taking the correct piece
                                            self.board[mx][my] = self.board[px][py] # Place piece at that point
                                            self.board[px][py] = 0
                                        else:
                                            raise BadOptionError(" Piece in way")
                                    else:
                                        self.board = [[self.board[7-x] for x in range (7)] for _ in range (7)]
                                        raise BadOptionError("Illigal move")