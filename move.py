import copy

class Move:
    def __init__(self, player, board, start, end, drop = None):
        self.player = player
        self.board = board
        self.start = start
        self.end = end
        self.drop = drop
        self.captures = player.captures
        if not self.start:
            self.piece = drop
        else:
            self.piece = start.getPiece()

    def getOpponentKing(self, board):
        if self.player.isLowerSide():
            target = " D"
        else:
            target = " d"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if repr(board[i][j].getPiece()) == target:
                    return board[i][j]

    def isCheck(self, board):
        kingPosition = self.getOpponentKing()
        candidate = end.getPiece().generatePossibleMoves()
        if kingPosition in candidate:
            return True
        return False

    def isCheckMate(self):
        return False if self.generateCheckMoves() else True

    def generateCheckMoves(self, board):
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].getPiece().isLower == self.player.isLowerSide():
                    start, startPiece = board[i][j], board[i][j].getPiece()
                    endCandidate = startPiece.generatePossibleMoves(startPiece)
                    for end in endCandidate:
                        newboard = copy.deepcopy(self.board)
                        startPiece.canMove(self.player, newboard, start, end)
                        if not self.isCheck(newboard):
                            # to do: fix repr of square to "a5"
                            res.append("move" + repr(start) + repr(end))
        for capture in self.captures:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    newboard = self.canDrop(copy.deepcopy(board), capture, board[i][j], copy.deepcopy(self.captures))
                    if newboard and not self.isCheck(newboard):
                        res.append("move" + repr(capture) + repr(end))
        return res


    def canDrop(self, board, piece, end, captures):
        if not piece:
            return False
        if piece not in captures:
            return False
        if end.getX() < 0 or end.getX() > 4 or end.getY() < 0 or end.getY() > 4:
            return False
        if end.getPiece():
            return False
        if repr(piece) in [" p", " P"]:
            if end.getX == self.player.getPromotionRow():
                return False
            newboard = copy.deepcopy(board)
            newboard[end.getX()][end.getY()] = piece
            if self.isCheck(board):
                return False
        captures.remove(piece)
        board[end.getX()][end.getY()] = piece
        return board


    def canMove(self, player, board, start, end):
        if not start.getPiece():
            return False
        return start.getPiece().canMove(player, board, start, end)



