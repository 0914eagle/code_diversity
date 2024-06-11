def sorted_list_sum(lst):
    
    lst = sorted(lst, key=len)
    return [x for x in lst if len(x) % 2 == 0]


if __name__ == '__main__':
    print(