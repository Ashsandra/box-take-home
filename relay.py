import piece


class Relay(piece.Piece):
    """
    Class that represents a Relay piece.
    """

    def __init__(self, lowerSide):
        self.ID = id(Relay)
        self.origin = Relay
        self.lowerSide = lowerSide
        self.canPromote = True

    def getCaptureRepr(self):
        if self.lowerSide:
            return "r"
        else:
            return "R"

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " r"
        else:
            return " R"

    def generatePossibleMoves(self, board, start):
        """
        :param board: the chess board
        :param start: the starting position
        :return: all valid moves of drive starting from index position.
        """
        i, j = start.getX(), start.getY()
        if self.lowerSide:
            candidate = [(i-1, j+1), (i-1,j), (i-1, j-1),
                     (i+1, j-1), (i+1, j+1)]
        else:
            candidate = [(i+1, j+1), (i+1,j), (i+1, j-1),
                     (i-1, j-1), (i-1, j+1)]

        res = []
        for x, y in candidate:
            if 0 <= x <= 4 and 0 <= y <= 4 \
                    and (not board[x][y].getPiece() or board[x][y].getPiece().isLower() != start.getPiece().isLower()):
                res.append(board[x][y])
        return res

    def canMove(self, player, board, start, end, changeCapture = True):
        """
        :param player: the current player
        :param board: the chess board
        :param start: the starting position
        :param end: the ending position
        :param changeCapture: boolean indicating whether the captureList needs to be changed
        :return: whether the player could move from start to end in the given board
        """
        if not self.checkMoveBasics(start, end):
            return False
        allMoves = self.generatePossibleMoves(board, start)
        if end not in allMoves:
            return False
        if end.getPiece():
            if changeCapture:
                player.setCapture(end.getPiece().origin(player.lowerSide))
        end.setPiece(start.getPiece())
        start.setPiece(None)
        return True