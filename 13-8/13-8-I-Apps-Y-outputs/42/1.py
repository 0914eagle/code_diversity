
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0
    
    worst_similar_movie = None
    for movie_a, movie_b in similarities:
        if movie_a == movie_id:
            worst_similar_movie = movie_b
            break
    
    if worst_similar_movie is not None:
        return get_horror_index(worst_similar_movie, horror_list, similarities) + 1
    else:
        return float('inf')

def solve(n_movies, n_horror_movies, n_similarities):
    horror_list = set()
    similarities = []
    
    for _ in range(n_horror_movies):
        horror_list.add(int(input()))
    
    for _ in range(n_similarities):
        a, b = map(int, input().split())
        similarities.append((a, b))
    
    highest_horror_index = 0
    highest_horror_index_movie = 0
    for movie_id in range(n_movies):
        if movie_id not in horror_list:
            horror_index = get_horror_index(movie_id, horror_list, similarities)
            if horror_index > highest_horror_index:
                highest_horror_index = horror_index
                highest_horror_index_movie = movie_id
    
    return highest_horror_index_movie

if __name__ == '__main__':
    n_movies, n_horror_movies, n_similarities = map(int, input().split())
    print(solve(n_movies, n_horror_movies, n_similarities))

