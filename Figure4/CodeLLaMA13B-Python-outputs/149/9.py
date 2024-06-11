def sorted_list_sum(lst):
    
    return sorted(filter(lambda x: len(x) % 2 == 0, lst), key=lambda x: (len(x), x))


if __name__ == '__main__':
    print(sorted_list_sum(["aa", "a", "aaa"]))
