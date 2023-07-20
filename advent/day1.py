import file_utils
import array as arr

path = './data/day1.txt'

def part1():

    lines = file_utils.get_lines(path)

    increases_count = 0
    previous = None

    for line in lines:
        
        number = int(line)

        if previous is not None:
            if number > previous:
                increases_count += 1

        previous = number

    print(increases_count)
    
def part2():

    lines = file_utils.get_lines(path)

    increases_count = 0
    previous = None
    window = arr.array('i', [0,0,0])



    for i in range(0,len(lines)):
        
        line = lines[i]

        window[i % 3] = int(line)

        if i >= 2:
            number = 0
            for n in window:
                number +=n
                
            if previous is not None:
                
                if number > previous:
                    increases_count += 1

            previous = number

    print(increases_count)

if __name__ == "__main__":
    part1()
    part2()