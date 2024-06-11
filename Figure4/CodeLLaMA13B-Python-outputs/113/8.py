def odd_count(lst):
    
    return [
        "the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            lst[i].count("1") % 2 + lst[i].count("3") % 2 + lst[i].count("5") % 2 + lst[i].count("7") % 2 + lst[i].count("9") % 2,
            lst[i],
            lst[i],
            lst[i]
        )
        for i in range(len(lst))
    ]

print(odd_count(['1234567']))
print(odd_count(['3',"11111111"]))