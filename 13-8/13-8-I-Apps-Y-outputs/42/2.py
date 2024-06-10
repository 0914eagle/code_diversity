
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0
    
    worst_similar_movie = None
    for movie_id_2 in similarities[movie_id]:
        if movie_id_2 in horror_list:
            worst_similar_movie = movie_id_2
            break
    
    if worst_similar_movie is not None:
        return similarities[movie_id][worst_similar_movie] + 1
    else:
        return float('inf')

def get_movie_with_highest_horror_index(movie_ids, horror_list, similarities):
    horror_indices = {movie_id: get_horror_index(movie_id, horror_list, similarities) for movie_id in movie_ids}
    return max(horror_indices, key=horror_indices.get)

def main():
    n, h, l = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = {}
    for _ in range(l):
        a, b = map(int, input().split())
        if a not in similarities:
            similarities[a] = {}
        if b not in similarities:
            similarities[b] = {}
        similarities[a][b] = 1
        similarities[b][a] = 1
    
    movie_ids = set(range(n))
    print(get_movie_with_highest_horror_index(movie_ids, horror_list, similarities))

if __name__ == '__main__':
    main()

