
def f1(n, k, watch_later_list):
    # Initialize variables
    types = set(watch_later_list)
    type_counts = {type: watch_later_list.count(type) for type in types}
    min_clicks = 0

    # Iterate through the watch later list
    for i, type in enumerate(watch_later_list):
        # If the current type is the same as the previous type, skip this iteration
        if i > 0 and type == watch_later_list[i - 1]:
            continue

        # If the current type is not the same as the previous type, increment the minimum number of clicks
        min_clicks += 1

        # If the current type is the last type in the list, break the loop
        if type == watch_later_list[-1]:
            break

    return min_clicks

def f2(n, k, watch_later_list):
    # Initialize variables
    types = set(watch_later_list)
    type_counts = {type: watch_later_list.count(type) for type in types}
    min_clicks = 0

    # Iterate through the watch later list
    for i, type in enumerate(watch_later_list):
        # If the current type is the same as the previous type, skip this iteration
        if i > 0 and type == watch_later_list[i - 1]:
            continue

        # If the current type is not the same as the previous type, increment the minimum number of clicks
        min_clicks += 1

        # If the current type is the last type in the list, break the loop
        if type == watch_later_list[-1]:
            break

    return min_clicks

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    watch_later_list = input()
    print(f1(n, k, watch_later_list))
    print(f2(n, k, watch_later_list))

