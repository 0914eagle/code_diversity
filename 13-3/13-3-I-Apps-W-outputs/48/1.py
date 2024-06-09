
def get_permutation(b):
    # Sort the input array
    b.sort()
    
    # Create a dictionary to store the counts of each element
    counts = {}
    for i in range(len(b)):
        if b[i] in counts:
            counts[b[i]] += 1
        else:
            counts[b[i]] = 1
    
    # Create a list to store the permutation
    permutation = []
    
    # Iterate through the dictionary and add elements to the permutation
    for key in sorted(counts):
        for i in range(counts[key]):
            permutation.append(key)
    
    return permutation

def is_increasing(a):
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            return False
    return True

def get_answer(b):
    permutation = get_permutation(b)
    a = [permutation[0]]
    for i in range(1, len(permutation)):
        a.append(a[i - 1] ^ permutation[i])
    return a

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = get_answer(b)
    if is_increasing(a):
        print("Yes")
        print(" ".join(map(str, permutation)))
    else:
        print("No")

if __name__ == '__main__':
    main()

