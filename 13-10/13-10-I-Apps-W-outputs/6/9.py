
def get_party_estimation(n, photos):
    # Initialize an array to store the estimation of each MP's party
    estimation = [''] * (n + 1)

    # Iterate over the photos
    for photo in photos:
        # Split the photo into pairs
        pairs = photo.split()

        # Iterate over the pairs
        for pair in pairs:
            # Split the pair into the two MPs
            mp1, mp2 = pair.split(',')

            # Check if the MPs are already estimated to be in the same party
            if estimation[int(mp1)] == estimation[int(mp2)]:
                # If they are, continue to the next pair
                continue

            # Check if either MP is already estimated to be in a party
            if estimation[int(mp1)] == '' or estimation[int(mp2)] == '':
                # If neither MP is estimated, assign them to the same party
                estimation[int(mp1)] = 'A' if estimation[int(mp1)] == '' else 'B'
                estimation[int(mp2)] = estimation[int(mp1)]
            else:
                # If one MP is already estimated, assign the other MP to the opposite party
                estimation[int(mp1)] = 'B' if estimation[int(mp1)] == 'A' else 'A'
                estimation[int(mp2)] = estimation[int(mp1)]

    # Return the estimation array
    return estimation

def main():
    # Read the input
    n = int(input())
    photos = [input() for _ in range(5)]

    # Estimate the parties of the MPs
    estimation = get_party_estimation(n, photos)

    # Print the estimation
    print(''.join(estimation[1:]))

if __name__ == '__main__':
    main()

