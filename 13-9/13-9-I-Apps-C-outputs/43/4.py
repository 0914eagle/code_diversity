
def get_min_clicks(n, k, watch_list):
    # Initialize variables
    clicks = 0
    current_type = watch_list[0]
    watch_list = watch_list[1:]

    # Loop through the list of videos
    while watch_list:
        # If the current video is of the same type as the previous video, play it
        if watch_list[0] == current_type:
            clicks += 1
            watch_list = watch_list[1:]
        # If the current video is of a different type, find the next video of the same type
        else:
            for i in range(len(watch_list)):
                if watch_list[i] == current_type:
                    clicks += 1
                    watch_list = watch_list[i+1:]
                    break
            # If there are no more videos of the same type, play the next video
            else:
                clicks += 1
                watch_list = watch_list[1:]

        # Update the current type
        current_type = watch_list[0]

    return clicks

def main():
    n, k = map(int, input().split())
    watch_list = input()
    print(get_min_clicks(n, k, watch_list))

if __name__ == '__main__':
    main()

