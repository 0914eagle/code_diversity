def skjkasdkd(lst):
    
    lst = sorted(lst)
    max_prime = lst[-1]
    sum_of_digits = 0
    for i in range(len(lst)):
        if lst[i] > max_prime:
            break
        sum_of_digits += lst[i]
    return sum_of_digits


if __name__ == "__main__":
    lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
    print(skjkasdkd(lst))
