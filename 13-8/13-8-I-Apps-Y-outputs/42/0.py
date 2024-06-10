
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0
    
    worst_similar_movie = -1
    for movie_id_1, movie_id_2 in similarities:
        if movie_id_1 == movie_id and movie_id_2 in horror_list:
            worst_similar_movie = movie_id_2
            break
    
    if worst_similar_movie == -1:
        return float('inf')
    else:
        return get_horror_index(worst_similar_movie, horror_list, similarities) + 1

def get_best_movie(movie_ids, horror_list, similarities):
    horror_indices = []
    for movie_id in movie_ids:
        horror_indices.append(get_horror_index(movie_id, horror_list, similarities))
    
    best_movie = movie_ids[0]
    for i in range(1, len(movie_ids)):
        if horror_indices[i] < horror_indices[best_movie]:
            best_movie = i
    
    return best_movie

def main():
    N, H, L = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = []
    for _ in range(L):
        movie_id_1, movie_id_2 = map(int, input().split())
        similarities.append((movie_id_1, movie_id_2))
    
    movie_ids = list(range(N))
    print(get_best_movie(movie_ids, horror_list, similarities))

if __name__ == '__main__':
    main()

