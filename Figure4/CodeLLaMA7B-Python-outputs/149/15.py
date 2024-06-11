def sorted_list_sum(lst):
    
    lst = sorted(lst, key=len)
    return lst


if __name__ == '__main__':
    print(sorted_list_sum(["aa", "a",