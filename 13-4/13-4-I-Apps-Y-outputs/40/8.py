
def get_largest_number_of_battles(n, a, e):
    # Sort the list of ships sent by Finni in descending order
    e.sort(reverse=True)
    # Initialize the number of battles won by Atli to 0
    battles_won = 0
    # Iterate through the list of ships sent by Finni
    for i in range(n):
        # If Atli has more ships than Finni, win the battle and gain control of the solar system
        if a >= e[i]:
            battles_won += 1
            a -= e[i]
        # Otherwise, lose the battle and do not gain control of the solar system
        else:
            break
    # Return the largest number of battles won by Atli
    return battles_won

def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    print(get_largest_number_of_battles(n, a, e))

if __name__ == '__main__':
    main()

