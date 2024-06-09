
def get_horror_index(movie_list, horror_list, similarity_list):
    horror_index = {}
    for movie in movie_list:
        if movie in horror_list:
            horror_index[movie] = 0
        else:
            similar_movies = [movie for movie in movie_list if movie in similarity_list[movie]]
            if len(similar_movies) == 0:
                horror_index[movie] = float('inf')
            else:
                horror_index[movie] = max([horror_index[similar_movie] for similar_movie in similar_movies]) + 1
    return horror_index

def get_movie_with_highest_horror_index(movie_list, horror_list, similarity_list):
    horror_index = get_horror_index(movie_list, horror_list, similarity_list)
    return max(horror_index, key=horror_index.get)

