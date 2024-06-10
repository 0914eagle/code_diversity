
def get_status(n, statuses):
    # Initialize a count for the number of cows that can show their hands
    can_show_hand = 0

    # Iterate through the statuses of each cow
    for i in range(n):
        # If the current cow's status is not "FOLDED" and all other cows have a status of either "ALLIN" or "FOLDED"
        if statuses[i] != "F" and all(statuses[j] in ["A", "F"] for j in range(n) if j != i):
            # Increment the count of cows that can show their hands
            can_show_hand += 1

    return can_show_hand

def main():
    n = int(input())
    statuses = input()
    print(get_status(n, statuses))

if __name__ == '__main__':
    main()

