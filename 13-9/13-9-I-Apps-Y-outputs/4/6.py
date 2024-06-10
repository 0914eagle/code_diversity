
def get_earliest_party_day(number_of_trees, tree_growth_days):
    # Sort the tree growth days in ascending order
    tree_growth_days.sort()
    # The earliest day the party can be organized is the sum of the growth days of all the trees
    earliest_party_day = sum(tree_growth_days)
    return earliest_party_day

def main():
    number_of_trees = int(input())
    tree_growth_days = list(map(int, input().split()))
    earliest_party_day = get_earliest_party_day(number_of_trees, tree_growth_days)
    print(earliest_party_day)

if __name__ == '__main__':
    main()

