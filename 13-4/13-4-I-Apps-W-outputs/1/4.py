
def get_absurdity_segments(n, k, absurdity):
    # Sort the absurdity list in descending order
    absurdity.sort(reverse=True)
    # Initialize the segments with the first k laws
    segment_1 = absurdity[:k]
    segment_2 = absurdity[k:2*k]
    # Initialize the total absurdity of the signed laws
    total_absurdity = sum(segment_1) + sum(segment_2)
    # Loop through the remaining laws
    for i in range(2*k, n):
        # Check if the current law is more absurd than the current total absurdity
        if absurdity[i] > total_absurdity:
            # Add the current law to the first segment
            segment_1.append(absurdity[i])
            # Remove the least absurd law from the first segment
            segment_1.pop(0)
            # Add the current law to the second segment
            segment_2.append(absurdity[i])
            # Remove the least absurd law from the second segment
            segment_2.pop(0)
            # Update the total absurdity
            total_absurdity = sum(segment_1) + sum(segment_2)
    return segment_1, segment_2

def get_segments(n, k, absurdity):
    # Get the absurdity segments
    segment_1, segment_2 = get_absurdity_segments(n, k, absurdity)
    # Get the indices of the segments
    index_1 = absurdity.index(segment_1[0]) + 1
    index_2 = absurdity.index(segment_2[0]) + 1
    return index_1, index_2

if __name__ == '__main__':
    n, k = map(int, input().split())
    absurdity = list(map(int, input().split()))
    index_1, index_2 = get_segments(n, k, absurdity)
    print(index_1, index_2)

