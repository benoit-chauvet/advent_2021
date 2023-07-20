import file_utils
import array as arr

path = "./data/day3.txt"

def part1():

    lines = file_utils.get_lines(path)
    nb_lines = len(lines)

    ones = arr.array('i')
    
    for line in lines:
        for i in range (0, len(line)):
            if len(ones) <= i:
                ones.append(0)
            if line[i] == "1":
                ones[i] += 1
    
    gamma = 0
    epsilon = 0
    bytes_count = len(ones)

    for i in range(1, bytes_count+1):
        value = ones[i-1]
        if value > nb_lines - value:
            gamma += pow(2,bytes_count - i)
        else:
            epsilon += pow(2,bytes_count - i)

    print(gamma*epsilon)
    

def part2():

    lines = file_utils.get_lines(path)
    nb_lines = len(lines)

    ones = compute_ones(lines)

    for i in range(1, bytes_count+1):
        value = ones[i-1]
        if value > nb_lines - value:
            gamma += pow(2,bytes_count - i)
        else:
            epsilon += pow(2,bytes_count - i)

if __name__ == "__main__":
    part1()
    part2()
