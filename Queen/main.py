from random import randint

class Queen:
    def __init__(self,x,y):
        #board coords are from 0 to n-1
        self.x = x
        self.y = y
    def can_take(self,queen):
        if self.x == queen.x or self.y == queen.y or abs(self.x-queen.x) == abs(self.y-queen.y):
            return True
        else:
            return False
        # check if this queen can be taken
        # return true if it can

class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
    def create(self):
        for i in range(self.size):
            self.board.append([])
            for n in range(self.size):
                self.board[i].append(Tiles().value)
                #print(self.board)
        return(self.board)


class Tiles:
    def __init__(self):
        self.value=0


queens = [] # global queens variable
n = 4 # board size

def print_board(): #Ascii way of showing board
    board = [[0]*n for _ in range(n)]
    for queen in queens:
        board[queen.y][queen.x] = 1
    for line in board:
        print(line)

def main():
    queens = []
    spots_tried = 0
    while len(queens) < 4:
        x = randint(0,n-1)
        y = randint(0,n-1)
        q = Queen(x,y)
        queen_is_safe = True
        for queen in queens:
            if queen.can_take(q):
                queen_is_safe = False
        if queen_is_safe:
            queens.append(q)
        spots_tried += 1
        if spots_tried == 16:
            print("FAILURE")
            #queens = []
            main()
board = Board(4)
board.create()
main()
#print_board()

for line in board.board:
    print(line)
#print(board.create())
