
def get_horror_index(movie_id, horror_list, similarities):
    # Initialize the Horror Index with 0
    horror_index = 0
    
    # Check if the movie is on the horror list
    if movie_id in horror_list:
        horror_index = 0
    
    # Check if the movie is similar to a horrible movie
    for similar_movie in similarities:
        if movie_id == similar_movie[0] and similar_movie[1] in horror_list:
            horror_index = max(horror_index, similar_movie[2] + 1)
    
    return horror_index

def get_best_movie(movie_ids, horror_list, similarities):
    # Initialize the best movie with the first movie in the list
    best_movie = movie_ids[0]
    
    # Iterate over the movies in the list
    for movie in movie_ids[1:]:
        # Get the Horror Index for the current movie
        horror_index = get_horror_index(movie, horror_list, similarities)
        
        # Check if the current movie has a higher Horror Index than the current best movie
        if horror_index > get_horror_index(best_movie, horror_list, similarities):
            best_movie = movie
    
    return best_movie

def main():
    # Read the input
    num_movies, num_horror_movies, num_similarities = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = []
    for _ in range(num_similarities):
        a, b = map(int, input().split())
        similarities.append((a, b, 1))
    
    # Get the best movie
    best_movie = get_best_movie(list(range(num_movies)), horror_list, similarities)
    
    # Print the result
    print(best_movie)

if __name__ == '__main__':
    main()

