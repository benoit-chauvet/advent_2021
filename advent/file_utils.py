def get_lines(path):
    lines = list()
    f = open(path, "r")

    line = f.readline()
    while line != "":
        lines.append(line.strip())
        line = f.readline()
        
    f.close()
    return lines

