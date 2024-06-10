
def get_min_clicks(n, k, video_types):
    # Initialize variables
    clicks = 0
    current_type = ""
    video_counts = [0] * k

    # Loop through each video in the list
    for i in range(n):
        # Get the type of the current video
        type_index = ord(video_types[i]) - ord("a")

        # If the current video is of a new type, play it
        if type_index != current_type:
            clicks += 1
            current_type = type_index

        # Increment the count of videos of the current type
        video_counts[current_type] += 1

    # Return the minimum number of clicks needed to watch all videos
    return clicks + sum(video_counts)

def main():
    n, k = map(int, input().split())
    video_types = input()
    print(get_min_clicks(n, k, video_types))

if __name__ == '__main__':
    main()

