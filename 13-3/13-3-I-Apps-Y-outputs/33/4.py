
def get_max_beauty(n, k, x, a):
    # Calculate the maximum sum of beauty values of reposted pictures
    max_beauty = 0
    for i in range(n - k + 1):
        # Calculate the sum of beauty values of the current segment
        segment_beauty = sum(a[i:i+k])
        # Check if the current segment has at least one picture reposted by Vova
        if segment_beauty > 0:
            # Add the current segment to the list of reposted segments
            reposted_segments.append(segment_beauty)
            # Update the maximum sum of beauty values
            max_beauty += segment_beauty
            # Decrement the number of pictures Vova is ready to repost
            x -= 1
            # If Vova has reposted all the pictures, break the loop
            if x == 0:
                break
    # Check if Vova has reposted all the pictures
    if x == 0:
        return max_beauty
    else:
        return -1

