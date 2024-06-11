def odd_count(lst):
    
    # your code here
    # odd_count = []
    # for i in lst:
    #     count = 0
    #     for j in i:
    #         if int(j) % 2 != 0:
    #             count += 1
    #     odd_count.append("the number of odd elements " + str(count) + "n the str" + str(count) + "ng " + str(count) + " of the " + str(count) + "nput.")
    # return odd_count
    return ["the number of odd elements " + str(len([i for i in lst[j] if int(i) % 2 != 0])) + "n the str" + str(len([i for i in lst[j] if int(i) % 2 != 0])) + "ng " + str(len([i for i in lst[j] if int(i) % 2 != 0])) + " of the " + str(len([i for i in lst[j] if int(i) % 2 != 0])) + "nput." for j in range(len(lst))]


if