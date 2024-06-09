
def get_girl_name(N, names, A, B):
    # Find the closest boy to each name in the range [A, B]
    closest_names = []
    for i in range(A, B+1):
        if i % 2 == 1:
            closest_names.append(i)
        else:
            closest_names.append(i+1)
    
    # Find the name that maximizes the distance to the closest boy
    max_distance = 0
    girl_name = 0
    for i in range(A, B+1):
        if i % 2 == 1:
            distance = min([abs(i - j) for j in closest_names])
            if distance > max_distance:
                max_distance = distance
                girl_name = i
    
    return girl_name

