
def get_horror_index(movie_ids, horror_list, similarities):
    horror_index = {}
    for movie_id in movie_ids:
        if movie_id in horror_list:
            horror_index[movie_id] = 0
        else:
            worst_similar_movie = None
            for similar_movie in similarities[movie_id]:
                if similar_movie in horror_list and (worst_similar_movie is None or horror_index[similar_movie] < horror_index[worst_similar_movie]):
                    worst_similar_movie = similar_movie
            if worst_similar_movie is None:
                horror_index[movie_id] = float('inf')
            else:
                horror_index[movie_id] = horror_index[worst_similar_movie] + 1
    return max(horror_index, key=horror_index.get)

