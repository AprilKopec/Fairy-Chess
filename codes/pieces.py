WHITE = "W"
BLACK = "B"


class Piece:

    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.color = color

    def is_valid(self, startpos, endpos, color, gameboard):
        if endpos in self.available_moves(startpos[0], startpos[1], gameboard):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def available_moves(self, x, y, gameboard):
        print("ERROR: no movement for base class")

    

    def rider(self, x, y, gameboard, color, intervals, n=100):
        """repeats the given interval until another piece is run into. 
        if that piece is not of the same color, that square is added and
         then the list is returned"""
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x+xint, y+yint
            i = 0
            while self.isInBounds(xtemp, ytemp) and i < n:
                #print(str((xtemp,ytemp))+"is in bounds")

                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.color != color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
                i += 1
        return answers

    def isInBounds(self, x, y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def noConflict(self, gameboard, initialColor, x, y):
        "checks if a single position poses no conflict to the rules of chess"
        if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].color != initialColor):
            return True
        return False

def leaper(int1, int2, x = 0, y = 0):
        return [(x+int1, y+int2), (x-int1, y+int2), (x+int1, y-int2), (x-int1, y-int2), (x+int2, y+int1), (x-int2, y+int1), (x+int2, y-int1), (x-int2, y-int1)]

W = leaper(1, 0)
F = leaper(1, 1)
N = leaper(2, 1)
C = leaper(3, 1)
Z = leaper(3, 2)
J = leaper(4, 1)
L = leaper(4, 3)

K = W + F


class Knight(Piece):
    abbr = 'N'
    
    def value():
        return 315

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, N, 1)


class Rook(Piece):
    abbr = 'R'
    
    def value():
        return 500

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, W)


class Bishop(Piece):
    abbr = 'B'
    
    def value():
        return 315

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, F)


class Queen(Piece):
    abbr = 'Q'
    
    def value():
        return 975

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K)


class King(Piece):
    abbr = 'K'
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K, 1)


class Pawn(Piece):
    abbr = 'P'

    def __init__(self, color, name, direction):
        self.name = name
        self.color = color
        # of course, the smallest piece is the hardest to code. direction should be either 1 or -1, should be -1 if the pawn is traveling "backwards"
        self.direction = direction

    def available_moves(self, x, y, gameboard):
        answers = []
        if (x+1, y+self.direction) in gameboard and self.noConflict(gameboard, self.color, x+1, y+self.direction):
            answers.append((x+1, y+self.direction))
        if (x-1, y+self.direction) in gameboard and self.noConflict(gameboard, self.color, x-1, y+self.direction):
            answers.append((x-1, y+self.direction))
        if (x, y+self.direction) not in gameboard:
            # the condition after the and is to make sure the non-capturing movement (the only fucking one in the game) is not used in the calculation of checkmate
            answers.append((x, y+self.direction))
        if (((self.color == WHITE and y == 1)
             or (self.color == BLACK and y == 6))
                and (x, y + 1 * self.direction) not in gameboard
                and (x, y + 2 * self.direction) not in gameboard):
            answers.append((x, y + 2 * self.direction))
        return answers


class Nightrider(Piece):
    abbr = 'NR'
    
    def value():
        return 475

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, N)


class Mann(Piece):
    abbr = 'M'
    
    def value():
        return 375

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K, 1)
        

class Ferz(Piece):
    abbr = 'F'
    
    def value():
        return 150

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, F, 1)

        
class Wazir(Piece):
    abbr = 'W'

    def value():
        return 170
    
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, W, 1)


class Amazon(Piece):
    abbr = 'A'

    def value():
        return 1250
        
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K) + self.rider(x, y, gameboard, self.color, N, 1)
       

class Chancellor(Piece):
    abbr = 'CH'

    def value():
        return 800

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, W) + self.rider(x, y, gameboard, self.color, N, 1)
        
        
class Archbishop(Piece):
    abbr = 'AB'

    def value():
        return 770
        
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, F) + self.rider(x, y, gameboard, self.color, N, 1)


class ShortRook4(Piece):
    abbr = 'R4'
    
    def value():
        return 380

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, W, 4)


class ShortRook2(Piece):
    abbr = 'R2'
    
    def value():
        return 270

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, W, 2)

    
class ShortBishop2(Piece):
    abbr = 'B2'
    
    def value():
        return 220

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, F, 2)
        
        
class ShortBishop4(Piece):
    abbr = 'B4'
    
    def value():
        return 250

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, F, 4)


class Unicorn(Piece):
    abbr = 'U'
    
    def value():
        return 900

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, N+F)


class Camel(Piece):
    abbr = 'C'
    
    def value():
        return 220

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, C, 1)


class Zebra(Piece):
    abbr = 'Z'
    
    def value():
        return 180

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, Z, 1)


class ZebraCamel(Piece):
    abbr = 'ZC'
    
    def value():
        return 400

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, Z+C, 1)


class Centaur(Piece):
    abbr = 'CN'
    
    def value():
        return 600

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K+N, 1)


class CentaurRider(Piece):
    abbr = 'CNR'
    
    def value():
        return 900

    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K, 1) + self.rider(x, y, gameboard, self.color, N)
        
        
class BishopCamel(Piece):
    abbr = "BC"
    
    def value():
        return 750
        
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, C, 1) + self.rider(x, y, gameboard, self.color, F)


class KnightZebra(Piece):
    abbr = "NZ"
    
    def value():
        return 600
        
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, N+Z, 1)


class DoubleMann(Piece):
    abbr = "M2"
    
    def value():
        return 500
        
    def available_moves(self, x, y, gameboard):
        return self.rider(x, y, gameboard, self.color, K, 2)

piece_names = Piece.__subclasses__()
bishops = [Bishop, ShortBishop4, ShortBishop2, Ferz]
colorbounded = bishops + [Camel, BishopCamel]



# 画像IDの割り当て
piece_ID = {}
for i, piece in enumerate(piece_names):
    piece_ID['W' + piece.abbr] = i + 1
    piece_ID['B' + piece.abbr] = -(i + 1)
