def skjkasdkd(lst):
    
    lst = [int(i) for i in lst]
    lst = [i for i in lst if i > 1]
    for i in lst:
        for j in range(2, i):
            if i % j == 0:
                lst.remove(i)
                break
    return sum([int(i) for i in str(max(lst))])


if __name__ == '__main__':
    print(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
