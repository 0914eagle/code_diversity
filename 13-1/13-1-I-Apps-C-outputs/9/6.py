
def get_min_clicks(n, k, watch_later_list):
    # Initialize variables
    clicks = 0
    current_type = watch_later_list[0]
    types_watched = set()
    types_watched.add(current_type)

    # Iterate through the watch later list
    for i in range(1, n):
        # If the current video is of the same type as the previous video, play it
        if watch_later_list[i] == current_type:
            clicks += 1
        # If the current video is of a different type, play the next video of the same type
        else:
            clicks += 1
            current_type = watch_later_list[i]
            types_watched.add(current_type)

    # If all videos have been watched, return the minimum number of clicks
    if len(types_watched) == k:
        return clicks

    # If not all videos have been watched, return -1
    return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    watch_later_list = list(input())
    print(get_min_clicks(n, k, watch_later_list))

