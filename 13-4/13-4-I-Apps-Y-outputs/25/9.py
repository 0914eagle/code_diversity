
def get_dog_behavior(a, b, c, d):
    # Define a function to get the dog's behavior at a given time
    def get_dog_behavior_at_time(time):
        # Calculate the number of aggressive minutes that have passed since the last calm minute
        num_aggressive_minutes = (time // b) % 2
        # If the number of aggressive minutes is 0, the dog is calm
        if num_aggressive_minutes == 0:
            return "calm"
        # If the number of aggressive minutes is 1, the dog is aggressive
        else:
            return "aggressive"
    
    # Return a tuple with the behavior of both dogs at the given time
    return (get_dog_behavior_at_time(a), get_dog_behavior_at_time(c))

def get_attacking_dogs(postman_time, milkman_time, garbage_man_time):
    # Get the behavior of the dogs at the given times
    postman_behavior = get_dog_behavior(postman_time, milkman_time, garbage_man_time)[0]
    milkman_behavior = get_dog_behavior(postman_time, milkman_time, garbage_man_time)[1]
    
    # Determine how many dogs attack each hero
    if postman_behavior == "aggressive" and milkman_behavior == "aggressive":
        return "both"
    elif postman_behavior == "aggressive" or milkman_behavior == "aggressive":
        return "one"
    else:
        return "none"

if __name__ == '__main__':
    # Read input
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    
    # Call the function to get the attacking dogs
    postman_attacking_dogs = get_attacking_dogs(p, m, g)
    milkman_attacking_dogs = get_attacking_dogs(m, p, g)
    garbage_man_attacking_dogs = get_attacking_dogs(g, p, m)
    
    # Print output
    print(postman_attacking_dogs)
    print(milkman_attacking_dogs)
    print(garbage_man_attacking_dogs)

