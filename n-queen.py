def row_checker(board, row):
    for i in range(N):
        if board[row][i] == 1:
            return False
    return True


def col_checker(board, col):
    for i in range(N):
        if board[i][col] == 1:
            return False
    return True


def diagonal_checker(board, row, col):

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if(board[i][j] == 1):
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if(board[i][j] == 1):
            return False
    return True
def isvalid(board, row, col):
    
    if row_checker(board, row) == True and col_checker(board, col) == True and diagonal_checker(board, row, col) == True:
        return True
    return False

def N_Queen(board, col):
    
    if N == 2 and N == 3:
        return False
    if col >= N:
        printer(board)
        return True
    
    for row in range(N):
        if(isvalid(board, row, col)):
            board[row][col] = 1
            N_Queen(board, col + 1)
            board[row][col] = 0
    
    
    return False

# check two queens in the same row
def printer(res):
    for i in range(N):
        for j  in range(N):
            print(res[i][j],end=" ")
        print()
    print('*'*10)
    
if __name__=='__main__':
    
    N = 8
    board = [[0 for i in range(N)] for j in range(N)]
    N_Queen(board, 0)


