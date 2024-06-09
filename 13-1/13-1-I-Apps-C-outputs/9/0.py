
def f1(n, k, watch_later_list):
    # Initialize variables
    types = set(watch_later_list)
    type_counts = {type: watch_later_list.count(type) for type in types}
    min_clicks = 0

    # Iterate through the watch later list
    for i in range(n):
        # If the current video is the last video of its type, play it
        if type_counts[watch_later_list[i]] == 1:
            min_clicks += 1
        # If the current video is not the last video of its type, skip it
        else:
            min_clicks += 2
            type_counts[watch_later_list[i]] -= 1

    return min_clicks

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    watch_later_list = input()
    print(f1(n, k, watch_later_list))

