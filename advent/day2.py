import file_utils
import array as arr

path = "./data/day2.txt"

def part1():

    lines = file_utils.get_lines(path)
    horizontal = 0
    depth = 0

    for line in lines:
        words = line.split()
        action = words[0]
        value = int(words[1])

        match(action):
            case "forward":
                horizontal += value
            case "up":
                depth -= value
            case "down":
                depth += value
            
    print(f'{horizontal} - {depth}')
    
    print(horizontal * depth)

def part2():

    lines = file_utils.get_lines(path)
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        words = line.split()
        action = words[0]
        value = int(words[1])

        match(action):
            case "forward":
                horizontal += value
                depth = depth + (aim * value)
            case "up":
                aim -= value
            case "down":
                aim += value
            
    print(f'{horizontal} - {depth}')
    
    print(horizontal * depth)


if __name__ == "__main__":
    part1()
    part2()