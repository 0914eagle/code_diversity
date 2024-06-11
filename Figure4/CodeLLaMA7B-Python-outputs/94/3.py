def skjkasdkd(lst):
    
    lst = [int(i) for i in lst]
    for i in lst:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                return i


lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
print(skjkasdkd(lst))
