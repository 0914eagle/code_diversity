def odd_count(lst):
    
    # your code here
    lst2 = []
    for i in lst:
        odd = 0
        for j in i:
            if int(j) % 2 == 1:
                odd += 1
        lst2.append("the number of odd elements " + str(odd) + "n the str" + str(odd) + "ng " + str(odd) + " of the " + str(odd) + "nput.")
    return lst2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
