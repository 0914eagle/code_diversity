
def f1(n, e):
    # convert n to a string
    n_str = str(n)
    # convert 2^e to a string
    e_str = str(2**e)
    # initialize a counter for the number of occurrences of e_str in n_str
    count = 0
    # loop through each substring of n_str that is the same length as e_str
    for i in range(len(n_str) - len(e_str) + 1):
        # check if the substring is equal to e_str
        if n_str[i:i+len(e_str)] == e_str:
            # if it is, increment the counter
            count += 1
    # return the number of occurrences of e_str in n_str
    return count

def f2(n, e):
    # convert n to a string
    n_str = str(n)
    # convert 2^e to a string
    e_str = str(2**e)
    # initialize a set to store the indices of the occurrences of e_str in n_str
    indices = set()
    # loop through each substring of n_str that is the same length as e_str
    for i in range(len(n_str) - len(e_str) + 1):
        # check if the substring is equal to e_str
        if n_str[i:i+len(e_str)] == e_str:
            # if it is, add its index to the set
            indices.add(i)
    # return the number of unique indices in the set
    return len(indices)

if __name__ == '__main__':
    n = int(input())
    e = int(input())
    print(f1(n, e))
    print(f2(n, e))

