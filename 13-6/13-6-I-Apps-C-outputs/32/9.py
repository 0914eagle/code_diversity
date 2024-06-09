
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    dogs = []
    for _ in range(N):
        dogs.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for dog in dogs for t in dog)
    return N, M, dogs

def f1(N, M, dogs):
    # Initialize the food bowls with the first dog's food preferences
    bowls = [dogs[0]]
    # Remove the first dog's food preferences from the list
    dogs.pop(0)
    # While there are still dogs left to feed
    while dogs:
        # Find the dog with the shortest food preference
        shortest_dog = min(dogs, key=lambda x: x[0])
        # Find the bowl with the shortest time
        shortest_time = min(bowls, key=lambda x: x[0])
        # Assign the dog to the bowl with the shortest time
        shortest_dog[0] = shortest_time[0]
        # Remove the bowl with the shortest time from the list
        bowls.remove(shortest_time)
        # Add the dog to the list of fed dogs
        dogs.remove(shortest_dog)
    # Calculate the total waiting time
    total_time = sum(dog[0] for dog in dogs)
    return total_time

def f2(N, M, dogs):
    # Initialize the food bowls with the first dog's food preferences
    bowls = [dogs[0]]
    # Remove the first dog's food preferences from the list
    dogs.pop(0)
    # While there are still dogs left to feed
    while dogs:
        # Find the dog with the shortest food preference
        shortest_dog = min(dogs, key=lambda x: x[0])
        # Find the bowl with the shortest time
        shortest_time = min(bowls, key=lambda x: x[0])
        # Assign the dog to the bowl with the shortest time
        shortest_dog[0] = shortest_time[0]
        # Remove the bowl with the shortest time from the list
        bowls.remove(shortest_time)
        # Add the dog to the list of fed dogs
        dogs.remove(shortest_dog)
    # Calculate the total waiting time
    total_time = sum(dog[0] for dog in dogs)
    return total_time

if __name__ == '__main__':
    N, M, dogs = get_input()
    print(f1(N, M, dogs))

