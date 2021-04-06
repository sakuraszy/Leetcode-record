class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solved=False
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
        def ava_option(i,j):
            result= []
            ind =(i//3)*3+j//3
            for x in range(1,10):
                x = str(x)
                if x not in row[i] and x not in col[j] and x not in box[ind]:
                    result.append(str(x))
            return result
        def addall(i,j,v):
            ind =(i//3)*3+j//3
            row[i].append(v)
            col[j].append(v)
            box[ind].append(v) 
            
        def removeall(i,j,v):
            ind =(i//3)*3+j//3
            row[i].remove(v)
            col[j].remove(v)
            box[ind].remove(v)
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    addall(i,j,board[i][j])
        def recur(i,j):
            #print(board)
            if i == 8 and j ==9:
                #print(board)
                return True
            if j==9:
                i = i+1
                j=0
            if board[i][j]==".":
                t = ava_option(i,j)
                for v in t:
                    board[i][j]=str(v)
                    addall(i,j,v)
                    if recur(i,j+1):
                        return True
                    else:
                        board[i][j]='.'
                        removeall(i,j,v)
                return False
            else:
                return recur(i,j+1)
        recur(0,0)