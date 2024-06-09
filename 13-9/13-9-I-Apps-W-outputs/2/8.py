
def solve(N, names, A, B):
    # Find the closest boy to each name in the range [A, B]
    closest_names = []
    for i in range(A, B+1):
        if i % 2 == 1:
            closest_names.append(i)
        else:
            closest_names.append(i+1)
    
    # Find the name that maximizes the distance to the closest boy
    max_distance = 0
    best_name = None
    for i in range(A, B+1):
        if i % 2 == 1:
            distance = min([abs(i - name) for name in names])
            if distance > max_distance:
                max_distance = distance
                best_name = i
    
    return best_name

