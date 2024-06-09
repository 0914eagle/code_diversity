
def get_unique_jokes(jokes, supervisors):
    # Initialize a set to store the unique jokes
    unique_jokes = set()
    
    # Iterate over the jokes and supervisors
    for joke, supervisor in zip(jokes, supervisors):
        # If the joke is not already in the set, add it
        if joke not in unique_jokes:
            unique_jokes.add(joke)
        # If the supervisor is not in the set, add it
        if supervisor not in unique_jokes:
            unique_jokes.add(supervisor)
    
    # Return the number of unique jokes
    return len(unique_jokes)

def get_consecutive_jokes(jokes, supervisors):
    # Initialize a set to store the consecutive jokes
    consecutive_jokes = set()
    
    # Iterate over the jokes and supervisors
    for joke, supervisor in zip(jokes, supervisors):
        # If the joke is not already in the set, add it
        if joke not in consecutive_jokes:
            consecutive_jokes.add(joke)
        # If the supervisor is not in the set, add it
        if supervisor not in consecutive_jokes:
            consecutive_jokes.add(supervisor)
    
    # Return the number of consecutive jokes
    return len(consecutive_jokes)

def get_party_jokes(jokes, supervisors):
    # Get the number of unique jokes
    unique_jokes = get_unique_jokes(jokes, supervisors)
    
    # Get the number of consecutive jokes
    consecutive_jokes = get_consecutive_jokes(jokes, supervisors)
    
    # Return the number of party jokes
    return unique_jokes * consecutive_jokes

if __name__ == '__main__':
    # Read the number of employees
    n = int(input())
    
    # Read the jokes and supervisors
    jokes = list(map(int, input().split()))
    supervisors = list(map(int, input().split()))
    
    # Get the number of party jokes
    party_jokes = get_party_jokes(jokes, supervisors)
    
    # Print the number of party jokes
    print(party_jokes)

