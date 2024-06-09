
def get_horror_index(movie_list, horror_list, similarities):
    horror_index = {}
    for movie in movie_list:
        if movie in horror_list:
            horror_index[movie] = 0
        else:
            similar_movies = [movie for movie in movie_list if movie in similarities[movie]]
            if len(similar_movies) == 0:
                horror_index[movie] = float('inf')
            else:
                worst_similar_movie = max(similar_movies, key=lambda x: horror_index[x])
                horror_index[movie] = horror_index[worst_similar_movie] + 1
    return max(horror_index, key=horror_index.get)

