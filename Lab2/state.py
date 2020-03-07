class State:
    def __init__(self):
        self.boards = []

    def __add__(self, board):
        self.boards.append(board)
        return self

    def __copy__(self):
        state = State()
        state.boards = self.boards[:]
        return state

    def __str__(self):
        string = ""
        for board in self.boards:
            string += '\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in board])
            string += "\n-------------------------\n"
        return string

    def lastBoard(self):
        return self.boards[-1]