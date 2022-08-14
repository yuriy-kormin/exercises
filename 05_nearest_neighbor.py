def find_index_of_nearest(digit, list_):
    if not len(list_):
        return
    elif digit in list_:
        return list_.index(digit)
    elif len(list_) == 1:
        return 0
    cur_digit = list_[0]
    for i, v in enumerate(list_):
        if abs(v-digit) < abs(cur_digit - digit):
            cur_i = i
            cur_digit = v
    return cur_i

print (find_index_of_nearest(0, [10,15]))