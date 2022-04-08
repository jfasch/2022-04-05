def uniq(in_l):
    out_l = []
    for num in in_l:
        if num not in out_l:
            out_l.append(num)
    return out_l

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
uniquified_list = uniq(input_list)
print(uniquified_list)
