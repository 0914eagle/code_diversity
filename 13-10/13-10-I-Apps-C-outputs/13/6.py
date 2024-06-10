
def get_average_number_of_visitors(n, a, p):
    # calculate the sum of the sizes of all guests
    total_size = sum(a)
    
    # initialize a list to store the number of visitors for each order
    num_visitors = []
    
    # iterate over all possible orders of the guests
    for order in itertools.permutations(range(1, n + 1)):
        # initialize the number of visitors for this order to 0
        num_visitors.append(0)
        
        # iterate over the guests in the order
        for i in order:
            # if the sum of the sizes of the guests in the restaurant plus the size of the current guest is less than or equal to the table length, add the current guest to the restaurant
            if total_size + a[i - 1] <= p:
                total_size += a[i - 1]
                num_visitors[-1] += 1
            # otherwise, break the loop and move on to the next order
            else:
                break
    
    # calculate the average number of visitors over all orders
    return sum(num_visitors) / len(num_visitors)

