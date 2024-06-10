
def get_party_estimation(mp_count, photos):
    # Initialize an array to store the estimation of each MP's party
    party_estimation = [' '] * mp_count

    # Iterate over each photo
    for photo in photos:
        # Iterate over each pair in the photo
        for pair in photo:
            # If the first MP in the pair is not yet estimated, estimate it to be in the opposite party of the second MP
            if party_estimation[pair[0]] == ' ':
                party_estimation[pair[0]] = 'A' if party_estimation[pair[1]] == 'B' else 'B'
            # If the second MP in the pair is not yet estimated, estimate it to be in the opposite party of the first MP
            elif party_estimation[pair[1]] == ' ':
                party_estimation[pair[1]] = 'A' if party_estimation[pair[0]] == 'B' else 'B'
            # If both MPs in the pair are already estimated, check if they are in the same party
            elif party_estimation[pair[0]] != party_estimation[pair[1]]:
                # If they are in different parties, return an empty array as the solution is not unique
                return []

    # If all MPs are estimated, return the estimation array
    return party_estimation

def main():
    mp_count = int(input())
    photos = []
    for _ in range(5):
        photo = input().split()
        photos.append([tuple(map(int, pair.split())) for pair in photo[1:]])
    estimation = get_party_estimation(mp_count, photos)
    print(''.join(estimation))

if __name__ == '__main__':
    main()

