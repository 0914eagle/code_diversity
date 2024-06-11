def sorted_list_sum(lst):
    
    return sorted(lst, key=lambda x: (len(x), x))


if __name__ == "__main__":
    print(sorted_list_sum(["aa",