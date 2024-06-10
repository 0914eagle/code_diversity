
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0
    
    horror_index = 1
    for similar_movie in similarities[movie_id]:
        if similar_movie in horror_list:
            horror_index = max(horror_index, get_horror_index(similar_movie, horror_list, similarities) + 1)
    
    return horror_index

def get_best_movie(movie_ids, horror_list, similarities):
    best_movie = None
    best_horror_index = 0
    
    for movie_id in movie_ids:
        horror_index = get_horror_index(movie_id, horror_list, similarities)
        if horror_index > best_horror_index:
            best_movie = movie_id
            best_horror_index = horror_index
        elif horror_index == best_horror_index and movie_id < best_movie:
            best_movie = movie_id
    
    return best_movie

def main():
    movie_ids = list(range(int(input())))
    horror_list = set(map(int, input().split()))
    similarities = {}
    
    for _ in range(int(input())):
        movie1, movie2 = map(int, input().split())
        if movie1 not in similarities:
            similarities[movie1] = []
        if movie2 not in similarities:
            similarities[movie2] = []
        similarities[movie1].append(movie2)
        similarities[movie2].append(movie1)
    
    print(get_best_movie(movie_ids, horror_list, similarities))

if __name__ == '__main__':
    main()

