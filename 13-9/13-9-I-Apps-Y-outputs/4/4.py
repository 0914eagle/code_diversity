
def get_party_day(n, growth_times):
    # Sort the growth times in non-decreasing order
    growth_times.sort()
    # The party can be organized on the latest day when all trees have grown
    party_day = sum(growth_times)
    return party_day

def main():
    n = int(input())
    growth_times = list(map(int, input().split()))
    party_day = get_party_day(n, growth_times)
    print(party_day)

if __name__ == '__main__':
    main()

