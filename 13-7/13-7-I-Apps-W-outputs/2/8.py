
def get_status(n, statuses):
    # Initialize a counter for the number of cows that can show their hands
    can_show_hands = 0
    
    # Iterate through the statuses of each cow
    for i in range(n):
        # If the current cow's status is not "FOLDED" and all other cows have a status of "ALLIN" or "FOLDED", increment the counter
        if statuses[i] != "F" and all(statuses[j] in ["A", "F"] for j in range(n) if j != i):
            can_show_hands += 1
    
    # Return the number of cows that can show their hands
    return can_show_hands

def main():
    # Read the number of cows and their statuses from stdin
    n = int(input())
    statuses = input()
    
    # Call the get_status function and print the result
    print(get_status(n, statuses))

if __name__ == '__main__':
    main()

