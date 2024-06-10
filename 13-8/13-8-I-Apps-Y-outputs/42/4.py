
def get_horror_index(movie_id, horror_list, movie_similarity_database):
    # Initialize the Horror Index as 0
    horror_index = 0
    
    # Check if the movie is on the horror list
    if movie_id in horror_list:
        horror_index = 0
    
    # If the movie is not on the horror list, check if it is similar to a horrible movie
    else:
        # Get the list of similar movies
        similar_movies = movie_similarity_database[movie_id]
        
        # Initialize the worst similar movie with the highest Horror Index
        worst_similar_movie = (0, 0)
        
        # Iterate over the similar movies
        for similar_movie in similar_movies:
            # Check if the similar movie is on the horror list
            if similar_movie in horror_list:
                # If it is, set the Horror Index to 1
                horror_index = 1
                break
            # If it is not, check if it has a higher Horror Index than the current worst similar movie
            elif horror_index < get_horror_index(similar_movie, horror_list, movie_similarity_database):
                # If it does, set the worst similar movie to this movie
                worst_similar_movie = (similar_movie, get_horror_index(similar_movie, horror_list, movie_similarity_database))
        
        # If the worst similar movie has a Horror Index of 1, set the Horror Index to 2
        if worst_similar_movie[1] == 1:
            horror_index = 2
        # If the worst similar movie has a Horror Index of > 1, set the Horror Index to infinity
        elif worst_similar_movie[1] > 1:
            horror_index = float('inf')
    
    return horror_index

def get_best_movie(movie_similarity_database, horror_list):
    # Get the number of movies in the collection
    num_movies = len(movie_similarity_database)
    
    # Initialize the best movie with the lowest ID and the lowest Horror Index
    best_movie = (0, 0)
    
    # Iterate over the movies in the collection
    for movie_id in range(num_movies):
        # Get the Horror Index of the current movie
        horror_index = get_horror_index(movie_id, horror_list, movie_similarity_database)
        
        # Check if the current movie has a higher Horror Index than the current best movie
        if horror_index > best_movie[1]:
            # If it does, set the best movie to this movie
            best_movie = (movie_id, horror_index)
    
    return best_movie[0]

def main():
    # Read the input
    num_movies, num_horror_movies, num_similarities = map(int, input().split())
    horror_list = set(map(int, input().split()))
    movie_similarity_database = {}
    for _ in range(num_similarities):
        movie1, movie2 = map(int, input().split())
        if movie1 not in movie_similarity_database:
            movie_similarity_database[movie1] = []
        if movie2 not in movie_similarity_database:
            movie_similarity_database[movie2] = []
        movie_similarity_database[movie1].append(movie2)
        movie_similarity_database[movie2].append(movie1)
    
    # Find the best movie
    best_movie = get_best_movie(movie_similarity_database, horror_list)
    
    # Print the ID of the best movie
    print(best_movie)

if __name__ == '__main__':
    main()

