
def get_min_clicks(n, k, watch_later_list):
    # Initialize variables
    types = []
    clicks = 0
    current_type = watch_later_list[0]
    types.append(current_type)

    # Iterate through the watch later list
    for i in range(1, n):
        # If the current video is of a different type, add it to the list of types
        if watch_later_list[i] != current_type:
            types.append(watch_later_list[i])
            current_type = watch_later_list[i]
        # If the current video is of the same type, increase the number of clicks
        else:
            clicks += 1

    # Return the minimum number of clicks needed to watch all videos
    return clicks + len(types)

def main():
    n, k = map(int, input().split())
    watch_later_list = list(input())
    print(get_min_clicks(n, k, watch_later_list))

if __name__ == '__main__':
    main()

