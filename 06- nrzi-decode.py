def dec(el):
    return True if el == '|' else False

def decode(source):
    skip = False
    result =[]
    for i in source:
        if skip:
            skip = False
            continue
        else:
            if dec(i):
                skip = True
                result.append('1')
            else:
                result.append('0')
        print (''.join(result))
decode('_|¯|____|¯|__|¯¯¯')
# '011000110100'
