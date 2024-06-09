
def check_array(a, q):
    # Initialize a dictionary to store the number of queries for each value
    queries = {i: 0 for i in range(1, q+1)}
    # Loop through the array and increment the number of queries for each value
    for i in a:
        queries[i] += 1
    # Check if all values have been queried exactly once
    for i in range(1, q+1):
        if queries[i] != 1:
            return False
    return True

def restore_array(a, q):
    # Initialize an empty array to store the resulting array
    result = []
    # Loop through the array and set the values for each position
    for i in a:
        if i == 0:
            # If the value is 0, set it to any value from 1 to q
            result.append(i)
        else:
            # If the value is not 0, set it to the value of the corresponding query
            result.append(i)
    return result

if __name__ == '__main__':
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    if check_array(a, q):
        print("YES")
        print(*restore_array(a, q))
    else:
        print("NO")

