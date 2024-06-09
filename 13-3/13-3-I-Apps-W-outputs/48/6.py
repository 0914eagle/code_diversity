
def get_permutation(b):
    n = len(b)
    # Create a dictionary to store the counts of each element in b
    counts = {}
    for i in range(n):
        if b[i] in counts:
            counts[b[i]] += 1
        else:
            counts[b[i]] = 1
    
    # Create a list to store the permutation
    permutation = []
    
    # Iterate through the dictionary and add the elements to the permutation list
    for i in range(n):
        for key in counts:
            if counts[key] > 0:
                permutation.append(key)
                counts[key] -= 1
                break
    
    return permutation

def is_increasing(a):
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            return False
    return True

def solve(b):
    n = len(b)
    # Create a list to store the permutation
    permutation = get_permutation(b)
    
    # Create a list to store the sequence a
    a = [permutation[0]]
    for i in range(1, n):
        a.append(a[i - 1] ^ permutation[i])
    
    # Check if the sequence a is strictly increasing
    if is_increasing(a):
        return permutation
    else:
        return []

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    permutation = solve(b)
    if permutation:
        print("Yes")
        print(" ".join(map(str, permutation)))
    else:
        print("No")

