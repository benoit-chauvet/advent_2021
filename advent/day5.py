import file_utils
import array as arr

path = "./data/day5_test.txt"

width = 0
height = 0

def parse_line(line):
    points = line.strip().split(' -> ')
    p1 = parse_point(points[0])
    p2 = parse_point(points[1])
    start = p1
    end = p2
    if p1[0] > p2[0]:
        start = p2
        end = p1
    if p1[0] == p2[0] and p1[1] > p2[1]:
        start = p2
        end = p1
    return [start, end]

def parse_point(value):
    global width
    global height
    coords = value.split(',')
    point = (int(coords[0]), int(coords[1]))
    if point[0] > width:
        width = point[0]
    if point[1] > height:
        height = point[1]
    return point

def draw_board(board):
    for line in board:
        for cell in line:
            print(cell, end='')
        print('')

def part1():
    lines = file_utils.get_lines(path)
    vectors = list()

    for line in lines:
        points = parse_line(line)
        vectors.append(points)
        #print(f'{points[0]} - {points[1]}') 

    board = [ [0] * height for i in range(width)]
    draw_board(board)
    print(f'w{width} - h{height}')

    # draw the lines:


def part2():
    print('p2')

if __name__ == "__main__":
    part1()
    part2()
