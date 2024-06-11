def odd_count(lst):
    
    # return [f"the number of odd elements {len(lst)//2}n the str{len(lst)//2}ng {len(lst)//2} of the {len(lst)//2}nput."]
    return [f"the number of odd elements {lst[i].count('1')}n the str{i}ng {i} of the {i}nput." for i in range(len(lst))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
