def odd_count(lst):
    
    # your code here
    # 1. 
    # return [f"the number of odd elements {len(lst[i])//2}n the str{len(lst[i])//2}ng {len(lst[i])//2} of the {len(lst[i])//2}nput." for i in range(len(lst))]
    # 2.
    return [f"the number of odd elements {lst[i].count('1')}n the str{lst[i].count('1')}ng {lst[i].count('1')} of the {lst[i].count('1')}nput." for i in range(len(lst))]


if