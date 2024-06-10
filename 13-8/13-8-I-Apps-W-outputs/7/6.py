
def get_possible_options(n, x, y, z, a):
    # Initialize the number of possible options to 0
    possible_options = 0
    
    # Iterate over each castle and its defenders
    for i in range(n):
        # If the castle has at least one defender, we can attack it
        if a[i] > 0:
            # Check if the castle was not attacked in the previous day
            if i % 2 == 0:
                # The White King can attack the castle with a mixed attack
                possible_options += 1
            # Check if the castle was not attacked in the previous night
            if i % 2 == 1:
                # The Black King can attack the castle with a mixed attack
                possible_options += 1
    
    # Return the number of possible options
    return possible_options

def get_number_of_possible_options(n, x, y, z, a):
    # Initialize the number of possible options to 0
    possible_options = 0
    
    # Iterate over each castle and its defenders
    for i in range(n):
        # If the castle has at least one defender, we can attack it
        if a[i] > 0:
            # Check if the castle was not attacked in the previous day
            if i % 2 == 0:
                # The White King can attack the castle with a mixed attack
                possible_options += 1
            # Check if the castle was not attacked in the previous night
            if i % 2 == 1:
                # The Black King can attack the castle with a mixed attack
                possible_options += 1
    
    # Return the number of possible options
    return possible_options

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_number_of_possible_options(n, x, y, z, a))

