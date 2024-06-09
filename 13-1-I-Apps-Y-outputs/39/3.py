
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0

    horror_index = 1
    for movie_a, movie_b in similarities:
        if movie_a == movie_id:
            horror_index = max(horror_index, get_horror_index(movie_b, horror_list, similarities) + 1)
        elif movie_b == movie_id:
            horror_index = max(horror_index, get_horror_index(movie_a, horror_list, similarities) + 1)

    return horror_index

def solve(n, h, l):
    horror_list = set(map(int, input().split()))
    similarities = []
    for _ in range(l):
        a, b = map(int, input().split())
        similarities.append((a, b))

    horror_index = [0] * n
    for i in range(n):
        if i not in horror_list:
            horror_index[i] = get_horror_index(i, horror_list, similarities)

    return max(range(n), key=lambda i: (horror_index[i], i))

