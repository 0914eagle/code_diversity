def odd_count(lst):
    
    result = []
    for i in lst:
        odd = 0
        for j in i:
            if int(j) % 2 != 0:
                odd += 1
        result.append("the number of odd elements " + str(odd) + "n the str" + str(odd) + "ng " + str(odd) + " of the " + str(odd) + "nput.")
    return result

print(odd_count(['1234567']))
print(odd_count(['3',"11111111"]))