
def get_party_day(num_trees, tree_growth_days):
    # Sort the tree growth days in ascending order
    sorted_growth_days = sorted(tree_growth_days)
    # Initialize the party day as the last tree growth day
    party_day = sorted_growth_days[-1]
    # Loop through the tree growth days in reverse order
    for i in range(len(tree_growth_days) - 2, -1, -1):
        # Calculate the previous tree growth day
        previous_growth_day = sorted_growth_days[i]
        # Check if the party day is earlier than the previous tree growth day
        if party_day > previous_growth_day:
            # Update the party day to the previous tree growth day
            party_day = previous_growth_day
    return party_day

def main():
    # Read the number of trees and their growth days from stdin
    num_trees = int(input())
    tree_growth_days = list(map(int, input().split()))
    # Call the get_party_day function to get the earliest party day
    party_day = get_party_day(num_trees, tree_growth_days)
    # Print the earliest party day to stdout
    print(party_day)

if __name__ == '__main__':
    main()

