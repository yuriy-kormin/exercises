#!/usr/bin/env python3


def triangle(num):
    '''
        This function return line of Pascal's triangle
            0:      1
            1:     1 1
            2:    1 2 1
            3:   1 3 3 1
            4:  1 4 6 4 1
    '''
    pre_line = [1]
    count = 0
    line = [1]
    if num:
        while count < num:
            line = [1]
            if len(pre_line) > 1:
                for index, elem in enumerate(pre_line[:-1]):
                    line.append(pre_line[index + 1] + elem)
            line.append(1)
            count += 1
            pre_line = line[:]
    return line


def main():
    print (triangle(7))


if __name__=="__main__":
    main() 
