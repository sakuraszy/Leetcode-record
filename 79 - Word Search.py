class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0:
            return word==''
        m=len(board)
        n=len(board[0])
        def recur(i,j,word):
            if (i,j) in path:
                return False
            if word=='':
                return True
            elif board[i][j]==word[0]:
                path.append((i,j))
                if j!=0:
                    if recur(i,j-1,word[1:]):
                        return True
                if j!=n-1:
                    if recur(i,j+1,word[1:]):
                        return True
                if i !=0:
                    if recur(i-1,j,word[1:]):
                        return True
                if i != m-1:
                    if recur(i+1,j,word[1:]):
                        return True
                if word[1:]=='':
                    return True
                path.remove((i,j))
                return False
            else:
                return False
        for i in range(m):
            for j in range(n):
                path=[]
                r=recur(i,j,word)
                if r:
                    return True
        return False


#2021 Oct 7
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW=len(board)
        if ROW==0:
            return False
        COL=len(board[0])
        def move(i,j,path,w):
            if w=="":
                return True
            if i<0 or i ==ROW or j<0 or j==COL or board[i][j]!=w[0]:
                return False
            if board[i][j]==w[0]:
                path= path+[(i,j)]
                for choice in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (i+choice[0],j+choice[1]) not in path:
                        if move(i+choice[0],j+choice[1],path,w[1:]):
                            return True
                return False
        for i in range(ROW):
            for j in range(COL):
                if move(i,j,[],word):
                    return True
        return False