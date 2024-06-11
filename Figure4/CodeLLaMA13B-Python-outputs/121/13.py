def solution(lst):
    
    if len(lst) == 0:
        return 0
    else:
        return lst[::2][1::2].sum()


if __name__ ==