
def get_horror_index(movie_id, horror_list, similarities):
    # Initialize the horror index for the given movie
    horror_index = 0
    
    # Check if the movie is on the horror list
    if movie_id in horror_list:
        horror_index = 0
    
    # Check if the movie is similar to any horror movies
    for movie_id2, similarity in similarities:
        if movie_id2 in horror_list:
            horror_index = max(horror_index, similarity + 1)
    
    return horror_index

def get_highest_horror_index(movie_ids, horror_list, similarities):
    # Initialize the highest horror index and the corresponding movie ID
    highest_horror_index = 0
    highest_horror_movie_id = 0
    
    # Iterate over the movies and calculate their horror indices
    for movie_id in movie_ids:
        horror_index = get_horror_index(movie_id, horror_list, similarities)
        if horror_index > highest_horror_index:
            highest_horror_index = horror_index
            highest_horror_movie_id = movie_id
    
    return highest_horror_movie_id

def main():
    # Read the input
    num_movies, num_horror_movies, num_similarities = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = []
    for _ in range(num_similarities):
        movie_id1, movie_id2 = map(int, input().split())
        similarities.append((movie_id1, movie_id2))
    
    # Get the movie ID with the highest horror index
    highest_horror_movie_id = get_highest_horror_index(range(num_movies), horror_list, similarities)
    
    # Print the result
    print(highest_horror_movie_id)

if __name__ == '__main__':
    main()

