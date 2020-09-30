def get_median(lst):
    lst.sort()
    lst_len = len(lst)
    if lst_len % 2 == 0:
        pos2 = int(lst_len / 2)
        pos1 = pos2 - 1
        return int((lst[pos1] + lst[pos2]) / 2)
    else:
        pos1 = int(lst_len / 2)
        return lst[pos1]


print(get_median([5, 2, 1, 3, 4]))
print(get_median([3, 3, 7, 9]))
print(get_median([9, 7]))
print(get_median([7]))
