
def solve(N, di):
    # Calculate the number of ways to connect the parts
    num_ways = 1
    for i in range(N):
        num_ways *= di[i]
    
    # Calculate the number of ways to connect the parts in each way
    num_ways_each_way = 1
    for i in range(N):
        num_ways_each_way *= 2
    
    # Calculate the final answer
    answer = num_ways * num_ways_each_way
    
    # Return the answer modulo 998244353
    return answer % 998244353

