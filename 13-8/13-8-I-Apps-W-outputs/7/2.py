
def get_possible_attacks(n, x, y, z, a):
    # Initialize the number of possible attacks to 0
    possible_attacks = 0
    
    # Iterate over each castle
    for i in range(n):
        # If the castle has at least one defender
        if a[i] > 0:
            # Increment the number of possible attacks by 1
            possible_attacks += 1
    
    # Return the number of possible attacks
    return possible_attacks

def get_last_attack_options(n, x, y, z, a):
    # Initialize the number of last attack options to 0
    last_attack_options = 0
    
    # Iterate over each castle
    for i in range(n):
        # If the castle has at least one defender
        if a[i] > 0:
            # Increment the number of last attack options by 1
            last_attack_options += 1
    
    # Return the number of last attack options
    return last_attack_options

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        possible_attacks = get_possible_attacks(n, x, y, z, a)
        last_attack_options = get_last_attack_options(n, x, y, z, a)
        print(possible_attacks)

