
def get_min_clicks(n, k, video_types):
    # Initialize variables
    curr_type = video_types[0]
    num_clicks = 1
    types_seen = set()
    types_seen.add(curr_type)

    # Iterate through the video types
    for i in range(1, n):
        # If the current video type is the same as the previous one, increment the number of clicks
        if video_types[i] == curr_type:
            num_clicks += 1
        # If the current video type is different from the previous one, add it to the set of seen types and increment the number of clicks
        else:
            types_seen.add(video_types[i])
            num_clicks += 1
        # If all types have been seen, return the number of clicks
        if len(types_seen) == k:
            return num_clicks
        # Update the current video type
        curr_type = video_types[i]

    # If not all types have been seen, return -1
    return -1

def main():
    n, k = map(int, input().split())
    video_types = input()
    print(get_min_clicks(n, k, video_types))

if __name__ == '__main__':
    main()

