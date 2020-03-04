class State:
    def __init__(self, board):
        self.board = board

    @staticmethod
    def initialState(n):
        board = []
        for i in range(n):
            board.append([0] * n)
        return board
