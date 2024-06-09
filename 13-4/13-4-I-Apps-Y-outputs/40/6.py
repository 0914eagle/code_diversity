
def get_largest_number_of_battles(n, a, e):
    # Sort the list of ships sent by Finni in descending order
    e.sort(reverse=True)
    # Initialize the number of battles won by Atli to 0
    battles_won = 0
    # Iterate through the list of ships sent by Finni
    for i in range(n):
        # If Atli has more ships than Finni in the current battle, win the battle and add it to the number of battles won
        if a >= e[i]:
            battles_won += 1
            a -= e[i]
        # If Atli has fewer ships than Finni in the current battle, break the loop and return the number of battles won
        else:
            break
    return battles_won

def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    print(get_largest_number_of_battles(n, a, e))

if __name__ == '__main__':
    main()

