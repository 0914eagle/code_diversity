def odd_count(lst):
    
    # your code here
    lst2 = []
    for i in lst:
        count = 0
        for j in i:
            if int(j) % 2 != 0:
                count += 1
        lst2.append("the number of odd elements " + str(count) + "n the str" + str(count) + "ng " + str(count) + " of the " + str(count) + "nput.")
    return lst2


if __name__ == "__main__":
    import doctest
    doctest.testmod()