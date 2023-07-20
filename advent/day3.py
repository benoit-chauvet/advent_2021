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
    nb_bits = len(ones)

    for i in range(1, nb_bits + 1):
        value = ones[i - 1]
        if value > nb_lines - value:
            gamma += pow(2,nb_bits - i)
        else:
            epsilon += pow(2,nb_bits - i)

    print(gamma*epsilon)

def get_remaining_number_oxygen(lines, column):
     
    remain = list()
    nb_lines = len(lines)
    nb_ones = 0
    nb_zeros = 0

    for line in lines:
        if line[column] == '1':
            nb_ones += 1
        else:
            nb_zeros += 1 

    for line in lines:
        value = line[column]
        if value == '1' and nb_ones >= nb_zeros:
            remain.append(line)
        if value == '0' and nb_ones < nb_zeros:
            remain.append(line)

    if len(remain) == 1:
        return remain[0]
    else:
        return get_remaining_number_oxygen(remain, column + 1)

def get_remaining_number_co2(lines, column):
     
    remain = list()
    nb_lines = len(lines)
    nb_ones = 0
    nb_zeros = 0

    for line in lines:
        if line[column] == '1':
            nb_ones += 1
        else:
            nb_zeros += 1 

    for line in lines:
        value = line[column]
        if value == '1' and nb_ones < nb_zeros:
            remain.append(line)
        if value == '0' and nb_ones >= nb_zeros:
            remain.append(line)

    if len(remain) == 1:
        return remain[0]
    else:
        return get_remaining_number_co2(remain, column + 1)

def binary_to_int(value):
    
    result = 0
    nb_bits = len(value)

    for i in range(1, nb_bits + 1):
        bit = value[i - 1]
        if bit == '1':
            result += pow(2,nb_bits - i)

    return result

def part2():

    lines = file_utils.get_lines(path)

    nb_bytes = len(lines[0])
   
    oxygen = get_remaining_number_oxygen(lines, 0)
    co2 = get_remaining_number_co2(lines, 0)

    # print(oxygen)
    # print(binary_to_int(oxygen))
    # print(co2)
    # print(binary_to_int(co2))

    print(binary_to_int(oxygen) * binary_to_int(co2))

if __name__ == "__main__":
    part1()
    part2()
