#!/usr/bin/env python3


def hamming_weight(digit):
    ''' 
        This function return Hemming's weight of  dec digit
        It's mean quantity of 1 in bin value of this digit 
    '''
    val = bin(digit)[2:]
    q=0
    for i in val:
        if i == "1":
            q+=1
    return q


def main():
    print (hamming_weight(7))


if __name__=="__main__":
    main()