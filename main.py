class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [["empty" for j in range(0, height)] for i in range(0, width)]
    def change_tile(self, x, y, text):
        self.board[y-1][x-1] = text
    def value_at_tile(self, x, y):
        return self.board[y-1][x-1]
    def is_legal_tile(self, x, y):
        return not (x < 1 or y < 1 or x > self.width or y > self.height)
