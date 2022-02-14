NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def to_roman(digit):
    '''convert arabic digit to roman format'''
    if digit > 3000 or digit < 0 or int(digit) != digit:
        return False
    elif digit == 0:
        return ''
    else:
        answer = ''
        for num in NUMERALS:
            val = digit // NUMERALS[num]
            if val:
                answer += num * val
                digit = digit % NUMERALS[num]
        return answer


def to_arabic(digit):
    '''convert roman digit to arabic format'''
    answer = 0
    for num, val in NUMERALS.items():
        count = 0
        while digit[:len(num)] == num and count < 3:
            count += 1
            answer += NUMERALS[num]
            digit = digit[len(num):]
    return answer if not digit else False
