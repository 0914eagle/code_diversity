
def polycarp_problem(s):
    # Initialize variables
    r = 0
    indices = []
    
    # Check if the string contains "one" or "two" as a substring
    if "one" in s or "two" in s:
        # If it does, find the indices of all occurrences of "one" and "two"
        one_indices = [i for i, ltr in enumerate(s) if ltr == "one"]
        two_indices = [i for i, ltr in enumerate(s) if ltr == "two"]
        
        # Find the intersection of the two lists
        indices = list(set(one_indices) & set(two_indices))
        
        # If there are any indices, set the required number of removals to the length of the intersection
        if indices:
            r = len(indices)
    
    # Return the required number of removals and the indices to remove
    return r, indices

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        r, indices = polycarp_problem(s)
        print(r)
        if r != 0:
            print(" ".join(str(i) for i in indices))

if __name__ == '__main__':
    main()

