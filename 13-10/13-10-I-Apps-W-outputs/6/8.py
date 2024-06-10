
def get_party(n, photos):
    # Initialize an array to store the party of each MP
    party = [''] * (n + 1)

    # Iterate through the photos
    for photo in photos:
        # Iterate through the pairs in the photo
        for pair in photo:
            # If the party of the first MP in the pair is not set, set it to 'A'
            if party[pair[0]] == '':
                party[pair[0]] = 'A'
            # If the party of the second MP in the pair is not set, set it to the opposite of the first MP's party
            if party[pair[1]] == '':
                party[pair[1]] = 'B' if party[pair[0]] == 'A' else 'A'
    
    return ''.join(party[1:])

def main():
    n = int(input())
    photos = [input().split() for _ in range(5)]
    print(get_party(n, photos))

if __name__ == '__main__':
    main()

