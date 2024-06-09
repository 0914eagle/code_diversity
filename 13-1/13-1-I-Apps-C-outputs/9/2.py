
def f1(n, k, watch_later_list):
    # Initialize variables
    types = set(watch_later_list)
    type_counts = {type: watch_later_list.count(type) for type in types}
    min_clicks = 0

    # Iterate through the list of videos
    for i in range(n):
        # If the current video is of a new type, increment the minimum number of clicks
        if watch_later_list[i] not in types:
            types.add(watch_later_list[i])
            type_counts[watch_later_list[i]] = 1
            min_clicks += 1

        # If the current video is of a known type, decrement the count for that type
        else:
            type_counts[watch_later_list[i]] -= 1

            # If the count for the current type is 0, remove it from the set of types
            if type_counts[watch_later_list[i]] == 0:
                types.remove(watch_later_list[i])

    return min_clicks

def f2(n, k, watch_later_list):
    # Initialize variables
    types = set(watch_later_list)
    type_counts = {type: watch_later_list.count(type) for type in types}
    min_clicks = 0

    # Iterate through the list of videos
    for i in range(n):
        # If the current video is of a new type, increment the minimum number of clicks
        if watch_later_list[i] not in types:
            types.add(watch_later_list[i])
            type_counts[watch_later_list[i]] = 1
            min_clicks += 1

        # If the current video is of a known type, decrement the count for that type
        else:
            type_counts[watch_later_list[i]] -= 1

            # If the count for the current type is 0, remove it from the set of types
            if type_counts[watch_later_list[i]] == 0:
                types.remove(watch_later_list[i])

    return min_clicks

if __name__ == '__main__':
    n, k = map(int, input().split())
    watch_later_list = input()
    print(f1(n, k, watch_later_list))
    print(f2(n, k, watch_later_list))

