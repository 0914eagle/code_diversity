def odd_count(lst):
    
    # return ["the number of odd elements " + str(len(lst[i]) - lst[i].count('0')) + "n the str" + str(i) + "ng " + str(i) + " of the " + str(i) + "nput." for i in range(len(lst))]
    return ["the number of odd elements " + str(len(lst[i]) - lst[i].count('0')) + "n the str" + str(i) + "ng " + str(i) + " of the " + str(i) + "nput." for i in range(len(lst))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
