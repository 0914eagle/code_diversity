def sum_squares(lst):
    
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            lst[i] = lst[i] ** 3
        sum += lst[i]
    return sum


if __name__ == "__main__":
    print(sum_squares([1, 2, 3]))
    print(sum_squares([]))
    print(sum_squares([-1, -5, 2, -1, -5]))
