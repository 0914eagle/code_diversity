
def find_last_visited_cafe(n, cafes):
    last_visited = cafes[-1]
    for i in range(n-2, -1, -1):
        if cafes[i] == last_visited:
            return cafes[i+1]
    return cafes[0]

