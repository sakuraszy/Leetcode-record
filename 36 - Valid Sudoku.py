class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                boxindex = (i//3)*3+j//3
                if v!='.':
                    if v not in rows[i]:
                        rows[i].append(v)
                    else:
                        return False
                    if v not in col[j]:
                        col[j].append(v)
                    else:
                        return False
                    if v not in box[boxindex]:
                        box[boxindex].append(v)
                    else:
                        return False
        return True