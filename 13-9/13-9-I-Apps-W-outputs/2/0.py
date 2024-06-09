
def solve(names, A, B):
    # Find the closest boy to each name in the range [A, B]
    closest_boy = {}
    for i in range(A, B+1):
        if i % 2 == 1:
            continue
        closest_boy[i] = min(abs(i - name) for name in names)
    
    # Return the name with the maximum distance to the closest boy
    return max(closest_boy, key=closest_boy.get)

