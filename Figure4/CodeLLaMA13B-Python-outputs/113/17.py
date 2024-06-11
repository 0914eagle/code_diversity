def odd_count(lst):
    
    return [
        "the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            str(lst[i].count("1") + lst[i].count("3") + lst[i].count("5") + lst[i].count("7")),
            str(i),
            str(i),
            str(i)
        )
        for i in range(len(lst))
    ]


