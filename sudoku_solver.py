import time
start_time = time.time()
'''
Input: 
0 1 2 3 4 5 6 7 8 9 10 --> j
                         
3 0 6 | 5 0 8 | 4 0 0  0 
5 2 0 | 0 0 0 | 0 0 0  1 
0 8 7 | 0 0 0 | 0 3 1  2 
------|-------|-------
0 0 3 | 0 1 0 | 0 8 0  3
9 0 0 | 8 6 3 | 0 0 5  4
0 5 0 | 0 9 0 | 6 0 0  5
------|-------|-------
1 3 0 | 0 0 0 | 2 5 0  6
0 0 0 | 0 0 0 | 0 7 4  7
0 0 5 | 2 0 6 | 3 0 0  8

Output:
3 1 6 5 7 8 4 9 2 
5 2 9 1 3 4 7 6 8 
4 8 7 6 2 9 5 3 1 
2 6 3 4 1 5 9 8 7 
9 7 4 8 6 3 1 2 5 
8 5 1 7 9 2 6 4 3 
1 3 8 9 4 7 2 5 6 
6 9 2 3 5 1 8 7 4 
7 4 5 2 8 6 3 1 9

'''

'''
Following are the rules of Sudoku for a player. 

In all 9 sub matrices 3×3 the elements should be 1-9, without repetition.
In all rows there should be elements between 1-9 , without repetition.
In all columns there should be elements between 1-9 , without repetition.


'''
# easy board
board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# hard board
board1 =[[9, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 1, 7, 0, 0, 2],
        [6, 0, 0, 0, 8, 5, 0, 9, 0],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 7, 0, 6, 8, 0, 0, 1]]


def getZero(board): # returns a zero points that have to be filled 
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i,j
    return None
  

def print_ans(board):
    for i in range(len(board)):
        if i in [3,6]:
            print('------|-------|-------')        
        for j in range(len(board)):
            if j in [3,6]:
                print('| ',end = "")
            
            print(board[i][j],end=' ')
        print(end = '\n')
        

def isvalid(board,r,c,num):
    for i in range(len(board)):
        #check Horizontal
        if board[r][i] == num and i != c :
            return False
            
        #check vertical
        if board[i][c] == num and i != r :
            return False
              
        #check box
        x = r//3
        y = c//3
        
        for j in range(x*3,x*3+3):
            for k in range(y*3,y*3+3):
                if board[j][k] == num:
                    return False
    return True

def TimeCheck(func):
    def wrapper(*args, **kwargs):
    
        start_time = time.time()
        func(*args,**kwargs)
        print (f"My program took {time.time() - start_time} to run")
    return wrapper





def sudoku(board):
    find = getZero(board)
    
    if not find: # break out of the function
        return True
    else:
        r,c = find
        
    for i in range(1,10):
        if isvalid(board,r,c,i):
            board[r][c] = i
            
            
            if sudoku(board):
                return True
            board[r][c] = 0
    
    return False


@TimeCheck
def main():
    print_ans(board1)
    
    sudoku(board1)
    print('\n')
    print_ans(board1)

main()

# 0.056932687759399414s for board (easy problem)
# 20.779505491256714s for board1 (hard problem)
