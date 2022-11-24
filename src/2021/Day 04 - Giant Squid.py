#Reading file
with open(r"advent_of_code\src\2021\Inputs\day4.txt") as f:
    data = [line.strip() for line in f.readlines()]
f.close()

#Clean the data and prepare
draw_nums = data[0].split(",")

#Necessary Functions 
def create_boards(lines):
    big_tmp_board = []
    
    for i in range(1,len(lines),6):
        tmp_board = []
        for row in lines[i+1:i+6]:
            tmp_board.append(row.split())
        big_tmp_board.append(tmp_board)
    
    return big_tmp_board
 
def remove_drawn(n, board):
    for row in range(len(board)):
        for num in range(len(board[0])):
            if board[row][num] == n:
                board[row][num]  = '-'
                return True
            
    return False
    
def bingo_check(board):
    for row in board:
        if row == ['-', '-', '-', '-', '-']:
            return True
    
    for column in range(len(board)):
        checker = 0
        for row in range(len(board[0])):
            if board[row][column] == '-':
                checker += 1
                
        if checker == 5:
            return True
        
    return False

def calculate_result(winner_num, board):
    board_sum = 0
    for row in board:
        for num in row:
            try:
                board_sum += int(num)
            except ValueError:
                continue
        
    print(winner_num * board_sum)
   
#Part 1 Solution
winner_num, winner_board= 0, []
boards = create_boards(data)
loop_breaker = 1

for num in draw_nums:
    for board in boards:
        if remove_drawn(num, board):
            if bingo_check(board):
                winner_board = board.copy()
                winner_num = int(num)
                loop_breaker = 0
                break
    
    #To stop the numbers loop when we find the first bingo table
    if loop_breaker == 0:
        break

calculate_result(winner_num, winner_board)
#46920

#Part 2 Solution
winner_num, winner_boards = 0, []
boards = create_boards(data)

for num in draw_nums:
    for i in range(len((boards))):
        if i not in winner_boards:
            remove_drawn(num, boards[i])
        
            if bingo_check(boards[i]):
                winner_boards.append(i)
                winner_num = int(num)
                
calculate_result(winner_num, boards[winner_boards[-1]])
#12635