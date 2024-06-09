
def get_girl_name(names, a, b):
    # Find the closest boy to each name in the range [a, b]
    closest_boys = {}
    for i in range(a, b+1):
        if i % 2 == 1:
            closest_boys[i] = min(abs(i - int(name)) for name in names)
    
    # Return the name with the maximum distance to the closest boy
    return max(closest_boys, key=closest_boys.get)

