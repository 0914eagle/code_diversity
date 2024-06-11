def odd_count(lst):
    
    # return [f"the number of odd elements {len(lst[i])//2}n the str{len(lst[i])//2}ng {len(lst[i])//2} of the {len(lst[i])//2}nput." for i in range(len(lst))]
    return [f"the number of odd elements {lst[i].count('1')}n the str{lst[i].count('1')}ng {lst[i].count('1')} of the {lst[i].count('1')}nput." for i in range(len(lst))]


if __name__ == "__main__":
    import doctest
    doct