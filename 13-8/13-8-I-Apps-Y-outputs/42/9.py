
def get_horror_index(movie_id, horror_list, similarities):
    if movie_id in horror_list:
        return 0
    
    horror_index = 1
    for similar_movie in similarities[movie_id]:
        if similar_movie in horror_list:
            horror_index = max(horror_index, get_horror_index(similar_movie, horror_list, similarities) + 1)
    
    return horror_index

def get_highest_horror_index(movie_ids, horror_list, similarities):
    highest_horror_index = 0
    highest_horror_index_movie = 0
    
    for movie_id in movie_ids:
        horror_index = get_horror_index(movie_id, horror_list, similarities)
        if horror_index > highest_horror_index:
            highest_horror_index = horror_index
            highest_horror_index_movie = movie_id
    
    return highest_horror_index_movie

def main():
    movie_ids = list(range(int(input())))
    horror_list = set(map(int, input().split()))
    similarities = {}
    for _ in range(int(input())):
        movie_id1, movie_id2 = map(int, input().split())
        if movie_id1 not in similarities:
            similarities[movie_id1] = set()
        similarities[movie_id1].add(movie_id2)
        if movie_id2 not in similarities:
            similarities[movie_id2] = set()
        similarities[movie_id2].add(movie_id1)
    
    print(get_highest_horror_index(movie_ids, horror_list, similarities))

if __name__ == '__main__':
    main()

