def pairs_sum_to_zero(l):
    
    # Your code here
    # create a set of the list
    # iterate through the set
    # if the sum of two elements is zero, return True
    # else return False
    # O(n) time complexity
    # O(n) space complexity
    # set = set(l)
    # for i in set:
    #     if (0 - i) in set:
    #         return True
    # return False

    # O(n) time complexity
    # O(1) space complexity
    # create a set of the list
    # iterate through the set
    # if the sum of two elements is zero, return True
    # else return False
    set = set(l)
    for i in set:
        if (0 - i) in set:
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
