
def get_horror_index(movie_id, horror_list, similarities):
    # Base case: If the movie is on the horror list, return 0
    if movie_id in horror_list:
        return 0
    
    # Initialize the horror index to infinity
    horror_index = float('inf')
    
    # Iterate over the similarities and find the worst horror movie
    for movie_1, movie_2 in similarities:
        if movie_1 == movie_id:
            horror_index = min(horror_index, get_horror_index(movie_2, horror_list, similarities) + 1)
        elif movie_2 == movie_id:
            horror_index = min(horror_index, get_horror_index(movie_1, horror_list, similarities) + 1)
    
    return horror_index

def main():
    # Read the input
    N, H, L = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = []
    for _ in range(L):
        a, b = map(int, input().split())
        similarities.append((a, b))
    
    # Find the movie with the highest horror index
    horror_index = float('-inf')
    movie_id = -1
    for i in range(N):
        if i not in horror_list:
            current_horror_index = get_horror_index(i, horror_list, similarities)
            if current_horror_index > horror_index:
                horror_index = current_horror_index
                movie_id = i
    
    # Print the result
    print(movie_id)

if __name__ == '__main__':
    main()

