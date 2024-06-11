def odd_count(lst):
    
    # return ["the number of odd elements {}n the str{}ng {} of the {}nput.".format(len(lst[i])-lst[i].count("0")-lst[i].count("2")-lst[i].count("4")-lst[i].count("6"),len(lst[i]),i,len(lst)) for i in range(len(lst))]
    return ["the number of odd elements {}n the str{}ng {} of the {}nput.".format(lst[i].count("1")+lst[i].count("3")+lst[i].count("5")+lst[i].count("7"),len(lst[i]),i,len(lst)) for i in range(len(lst))]


