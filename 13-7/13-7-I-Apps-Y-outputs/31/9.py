
def get_balloon_capacity(n):
    return list(range(1, n+1))

def get_canister_capacity(n, canisters):
    return [canisters[i] for i in range(n)]

def get_balloon_filling(balloon_capacity, canister_capacity):
    balloon_filling = [0] * len(balloon_capacity)
    for i in range(len(balloon_capacity)):
        balloon_filling[i] = min(balloon_capacity[i], canister_capacity[i])
    return balloon_filling

def get_maximum_fraction(balloon_filling):
    maximum_fraction = 0
    for i in range(len(balloon_filling)):
        maximum_fraction = max(maximum_fraction, balloon_filling[i] / balloon_capacity[i])
    return maximum_fraction

def main():
    n = int(input())
    canisters = list(map(int, input().split()))
    balloon_capacity = get_balloon_capacity(n)
    canister_capacity = get_canister_capacity(n, canisters)
    balloon_filling = get_balloon_filling(balloon_capacity, canister_capacity)
    maximum_fraction = get_maximum_fraction(balloon_filling)
    print(maximum_fraction)

if __name__ == '__main__':
    main()

