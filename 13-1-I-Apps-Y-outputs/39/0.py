
def get_horror_index(movie_list, horror_list, similarities):
    horror_index = {}
    for movie in movie_list:
        if movie in horror_list:
            horror_index[movie] = 0
        else:
            worst_similar_movie = find_worst_similar_movie(movie, similarities)
            if worst_similar_movie is not None:
                horror_index[movie] = horror_index[worst_similar_movie] + 1
            else:
                horror_index[movie] = float('inf')
    return max(horror_index, key=horror_index.get)

def find_worst_similar_movie(movie, similarities):
    worst_similar_movie = None
    for similar_movie in similarities[movie]:
        if worst_similar_movie is None or horror_index[similar_movie] > horror_index[worst_similar_movie]:
            worst_similar_movie = similar_movie
    return worst_similar_movie

horror_list = set(map(int, input().split()))
movie_list = set(range(int(input())))
similarities = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    similarities.setdefault(a, set()).add(b)
    similarities.setdefault(b, set()).add(a)

print(get_horror_index(movie_list, horror_list, similarities))

