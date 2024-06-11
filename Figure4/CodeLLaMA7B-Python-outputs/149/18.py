def sorted_list_sum(lst):
    
    lst.sort(key=lambda x: (len(x), x))
    return lst


if __name__ == "__main__":
    print(sorted_list_sum(