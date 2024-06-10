
def get_earliest_day_for_party(tree_growth_days):
    # Sort the tree growth days in ascending order
    tree_growth_days.sort()
    # The earliest day for the party is the sum of the growth days plus 1
    return sum(tree_growth_days) + 1

def main():
    num_trees = int(input())
    tree_growth_days = list(map(int, input().split()))
    print(get_earliest_day_for_party(tree_growth_days))

if __name__ == '__main__':
    main()

