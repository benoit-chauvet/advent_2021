import file_utils
import array as arr

board_size = 5

path = "./data/day4_test.txt"

numbers = arr.array('i')
boards = list()

def init_game():
    f = open(path, "r")

    # init numbers:
    line = f.readline()
    line_split = line.strip().split(',')
    
    for item in line_split:
        numbers.append(int(item))

    # init boards
    while line != '':
        line = f.readline()

        board = [[]]
        
        if line.strip() != '':
            for row in range(0,5): 
                line_split = line.replace('  ', ' ').strip().split(' ')
                board.append([])
                for i in range(0, len(line_split)):
                    item = line_split[i]
                    board[row].append(int(item))
                line = f.readline()
            board.pop()
            boards.append(board)

    f.close()

def mark_board(board, number):
    for i in range(0,board_size):
        for j in range(0,board_size):
            if board[i][j] == number:
                board[i][j] = -1
                return

def check_win(board):
    for i in range(0,board_size):
        nb_x = 0
        nb_y = 0
        for j in range(0,board_size):
            if board[i][j] == -1: 
                nb_x +=1
            if board[j][i] == -1: 
                nb_y +=1
        if (nb_x == board_size or nb_y == board_size):
            return True
    return False

def calculate_score(board, last_number):
    score = 0
    for i in range(0, board_size):
        for j in range(0, board_size):
            if board[i][j] > -1:
                score += board[i][j]
    return score * last_number

def part1():
    init_game()
    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if check_win(board):
                print(calculate_score(board, number))
                return

def part2():
    init_game()
    rnd = 0

    for number in numbers:
        rnd += 1
        for i in range(0, len(boards)):
            board = boards[i]
            if board:
                mark_board(board, number)
                if check_win(board):
                    score = calculate_score(board, number)
                    boards[i] = None
                    if(score > 0):
                        print(rnd)
                        print(score * rnd)

if __name__ == "__main__":
    part1()
    part2()
