
def get_required_minutes(hamsters_positions):
    # Calculate the number of standing hamsters
    num_standing = sum(hamsters_positions == "X")
    
    # Calculate the number of minutes required to get the required number of standing hamsters
    required_minutes = (num_standing // 2) + (num_standing % 2)
    
    return required_minutes

def get_optimal_positions(hamsters_positions):
    # Calculate the number of standing hamsters
    num_standing = sum(hamsters_positions == "X")
    
    # Calculate the number of minutes required to get the required number of standing hamsters
    required_minutes = (num_standing // 2) + (num_standing % 2)
    
    # Create a list to store the optimal positions
    optimal_positions = []
    
    # Loop through the hamsters and determine the optimal position for each hamster
    for i in range(len(hamsters_positions)):
        if i < required_minutes:
            optimal_positions.append("X")
        else:
            optimal_positions.append("x")
    
    return "".join(optimal_positions)

if __name__ == '__main__':
    num_hamsters = int(input())
    hamsters_positions = input()
    required_minutes = get_required_minutes(hamsters_positions)
    optimal_positions = get_optimal_positions(hamsters_positions)
    print(required_minutes)
    print(optimal_positions)

