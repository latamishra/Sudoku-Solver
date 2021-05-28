# Algorithim for code
# 1. pick empty square
# 2. try all numbers
# 3. final one that works
# 4. repeat
# 5. backtrack
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False
#to check the number is valid or not.
#the numbers in row,column and box.
def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column #bo->board
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

# to print the board
def print_board(bo):
    for i in range(len(bo)):
        # here i is index of board=[[],[],[]..9]
                                #   0   1 2   8
        if i % 3 == 0 and i != 0:
            print("--------------------")
        for j in range(len(bo[0])):
         # here j is index of board[0] =     [7,8,0,4,0,0,1,2,0]
         #                                  0 1 2 3 4 5 6 7 8
            if j % 3 == 0 and j != 0:
                print("|", end = "")
            if j == 8:
                print(bo[i][j]) # print the value
                # when j == 8 which means last value in every array
            else:
                print(str(bo[i][j]) + " ", end = "")
                #print the every element in array except j==8
                #because next value can start from newline.

#to find the empty square
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return(i, j) #row,col
    return None

print(print_board(board))
solve(board)
print("_____________________")
print_board(board)
