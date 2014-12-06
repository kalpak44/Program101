HEIGHT = 3
WIDTH = 3

class Board:
    def __init__(self):
        self.board = {}
        self.initBoard()

    def initBoard(self):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                self.board[i,j] = '*'

    def isEditable(self, x, y):
        if x > WIDTH or x <= 0 or y > HEIGHT or y <= 0:
            return False
        else:
            return self.board[x-1,y-1] == '*'

    def edit0(self, x, y):
        if self.isEditable(x ,y):
            self.board[x-1,y-1] = 'o'
            return True
        else:
            return False

    def editX(self, x, y):
        if self.isEditable(x ,y):
            self.board[x-1,y-1] = 'x'
            return True
        else:
            return False

    def isFull(self):
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if self.board[i,j] == '*':
                    return False
        return True

    def wins(self):
        rows = []
        for i in range(WIDTH):
            row = ''
            for j in range(HEIGHT):
                row += self.board[i,j]
            rows.append(row)

        cols = []
        for i in range(WIDTH):
            col = ''
            for j in range(HEIGHT):
                col += self.board[j,i]
            cols.append(col)

        digs = []
        dig1 = ''
        dig2 = ''

        for i in range(WIDTH):
            for j in range(HEIGHT):
                if i == j:
                    dig1 += self.board[i,j]
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if WIDTH - i == HEIGHT - j:
                    dig2 += self.board[HEIGHT-i-1,j]

        digs.append(dig1)
        digs.append(dig2)

        return any(all(cell is 'x' for cell in row) or
                   all(cell is 'o' for cell in row)
                   for row in rows + cols + digs)


    def __str__(self):
        result = ''
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if j != WIDTH - 1:
                    result += self.board[i,j] + ' '
                else:
                    result += self.board[i,j]
            if i != HEIGHT - 1:
                result += '\n'

        return result