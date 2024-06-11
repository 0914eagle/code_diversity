def odd_count(lst):
    
    # Your code here
    lst_of_odds = []
    for i in lst:
        count = 0
        for j in i:
            if int(j) % 2 == 1:
                count += 1
        lst_of_odds.append("the number of odd elements " + str(count) + "n the str" + str(count) + "ng " + str(count) + " of the " + str(count) + "nput.")
    return lst_of_odds


