
def get_earliest_party_date(n, tree_growth_days):
    # Sort the tree growth days in ascending order
    tree_growth_days.sort()
    # The earliest day the party can be organized is the sum of the growth days of all the trees
    earliest_party_date = sum(tree_growth_days)
    return earliest_party_date

def main():
    n = int(input())
    tree_growth_days = list(map(int, input().split()))
    earliest_party_date = get_earliest_party_date(n, tree_growth_days)
    print(earliest_party_date)

if __name__ == '__main__':
    main()

