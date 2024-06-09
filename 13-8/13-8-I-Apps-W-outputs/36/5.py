
def get_min_m(n, k):
    # Initialize m to 1
    m = 1
    # Initialize a list to store the sets
    sets = []
    # Loop until we have n sets
    while len(sets) < n:
        # Generate a set of four integers from 1 to m
        set_ = set(range(1, m + 1))
        # Check if the set is valid
        if is_valid_set(set_, k):
            # Add the set to the list of sets
            sets.append(set_)
        # Increment m
        m += 1
    # Return the minimum m and the sets
    return m, sets

def is_valid_set(set_, k):
    # Check if the set has four elements
    if len(set_) != 4:
        return False
    # Check if the set has no duplicates
    if len(set_) != len(set(set_)):
        return False
    # Check if the set is of rank k
    for i in range(len(set_)):
        for j in range(i + 1, len(set_)):
            if gcd(set_[i], set_[j]) != k:
                return False
    # If all checks pass, return True
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, k = map(int, input().split())
m, sets = get_min_m(n, k)
print(m)
for set_ in sets:
    print(*set_)

