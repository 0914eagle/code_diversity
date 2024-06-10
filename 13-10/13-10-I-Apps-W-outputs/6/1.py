
def read_input():
    N = int(input())
    photos = []
    for i in range(5):
        P = int(input())
        pairs = []
        for j in range(P):
            K, L = map(int, input().split())
            pairs.append((K, L))
        photos.append(pairs)
    return N, photos

def get_party(N, photos):
    # Initialize an array to store the party of each MP
    party = [''] * (N + 1)

    # Iterate through each photograph and count the number of times each MP argues with another MP
    for photo in photos:
        for K, L in photo:
            if party[K] == '':
                party[K] = 'A'
            elif party[L] == '':
                party[L] = 'B'
            else:
                if party[K] == party[L]:
                    party[L] = 'A' if party[L] == 'B' else 'B'

    return party

def main():
    N, photos = read_input()
    party = get_party(N, photos)
    print(''.join(party[1:]))

if __name__ == '__main__':
    main()

