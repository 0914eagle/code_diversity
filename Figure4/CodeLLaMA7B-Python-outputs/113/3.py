def odd_count(lst):
    
    # your code here
    lst2 = []
    for i in lst:
        lst2.append(i.count('1') + i.count('3') + i.count('5') + i.count('7') + i.count('9'))
    lst3 = []
    for i in lst2:
        lst3.append("the number of odd elements " + str(i) + "n the str" + str(i) + "ng " + str(i) + " of the " + str(i) + "nput.")
    return lst3


if __name__ == "__main__":
    import doctest
    doctest.testmod()