
def get_earliest_day(num_trees, tree_growth_days):
    # Sort the tree growth days in ascending order
    tree_growth_days.sort()
    # Find the latest day when all trees are grown
    latest_day = tree_growth_days[-1]
    # Return the earliest day when the party can be organized
    return latest_day + 1

def main():
    num_trees = int(input())
    tree_growth_days = list(map(int, input().split()))
    print(get_earliest_day(num_trees, tree_growth_days))

if __name__ == '__main__':
    main()

