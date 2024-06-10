
def get_min_clicks(video_types):
    # Initialize variables
    num_clicks = 0
    current_type = video_types[0]

    # Iterate through the video types
    for i in range(len(video_types)):
        # If the current type is different from the previous type, increment the number of clicks
        if video_types[i] != current_type:
            num_clicks += 1
            current_type = video_types[i]

    # Return the minimum number of clicks
    return num_clicks

def main():
    # Read the number of videos and video types
    n, k = map(int, input().split())

    # Read the video types
    video_types = list(input())

    # Call the get_min_clicks function and print the result
    print(get_min_clicks(video_types))

if __name__ == '__main__':
    main()

