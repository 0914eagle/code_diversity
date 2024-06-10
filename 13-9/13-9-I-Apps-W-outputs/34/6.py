
def find_teammate(strengths):
    # Initialize a dictionary to store the teammate information
    teammates = {}
    
    # Iterate through the strengths of each possible combination of two people
    for i in range(1, len(strengths) + 1):
        for combination in combinations(range(1, len(strengths) + 1), i):
            # Get the strength of the current combination
            strength = strengths[combination[0] - 1][combination[1] - 1]
            
            # If the current combination is the strongest, update the teammate information
            if strength not in teammates or teammates[strength] > combination[0]:
                teammates[strength] = combination[0]
    
    # Return the teammate information
    return teammates

def get_teammates(strengths):
    # Find the teammate information
    teammates = find_teammate(strengths)
    
    # Initialize the teammate list
    teammate_list = [0] * len(strengths)
    
    # Iterate through the strengths and find the teammate for each person
    for i in range(len(strengths)):
        for strength, teammate in teammates.items():
            if teammate == i + 1:
                teammate_list[i] = strength
                break
    
    # Return the teammate list
    return teammate_list

if __name__ == '__main__':
    num_teams = int(input())
    strengths = []
    for i in range(num_teams):
        strengths.append(list(map(int, input().split())))
    print(*get_teammates(strengths), sep='\n')

