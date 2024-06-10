
def get_min_clicks(n, k, watch_later_list):
    # Initialize variables
    clicks = 0
    types_watched = set()
    current_type = watch_later_list[0]
    types_watched.add(current_type)

    # Loop through the watch later list
    for i in range(1, n):
        # If the current video is of a different type, click on it
        if watch_later_list[i] != current_type:
            clicks += 1
            current_type = watch_later_list[i]
            types_watched.add(current_type)

    # Return the minimum number of clicks
    return clicks + (k - len(types_watched))

def main():
    n, k = map(int, input().split())
    watch_later_list = list(input())
    print(get_min_clicks(n, k, watch_later_list))

if __name__ == '__main__':
    main()

