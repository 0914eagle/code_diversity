
def get_min_clicks(n, k, video_types):
    # Initialize variables
    click_count = 0
    current_type = video_types[0]
    video_counts = [0] * k
    for i in range(n):
        # Check if the current video is of the same type as the previous video
        if video_types[i] == current_type:
            # If it is, play the next video in the list
            click_count += 1
            current_type = video_types[(i + 1) % n]
        # If it is not, find the next video of the same type
        else:
            # Find the next video of the same type
            for j in range(i + 1, n):
                if video_types[j] == current_type:
                    click_count += 1
                    current_type = video_types[(j + 1) % n]
                    break
    return click_count

def main():
    n, k = map(int, input().split())
    video_types = input()
    print(get_min_clicks(n, k, video_types))

if __name__ == '__main__':
    main()

