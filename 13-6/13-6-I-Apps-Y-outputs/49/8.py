
def solve(my_list):
    # sort the list in descending order
    my_list.sort(reverse=True)
    # initialize a sum variable
    sum = 0
    # loop through the list and calculate the sum
    for i in range(len(my_list)):
        sum += my_list[i]
    # return the sum
    return sum

