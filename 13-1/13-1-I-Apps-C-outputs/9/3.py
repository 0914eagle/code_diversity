
def f1(n, k, watch_later_list):
    # Initialize variables
    types = []
    count = 0
    current_type = watch_later_list[0]
    types.append(current_type)

    # Iterate through the watch later list
    for i in range(1, n):
        if watch_later_list[i] == current_type:
            count += 1
        else:
            count += 2
            current_type = watch_later_list[i]
            types.append(current_type)

    # Return the minimum number of clicks
    return count

def f2(n, k, watch_later_list):
    # Initialize variables
    types = []
    count = 0
    current_type = watch_later_list[0]
    types.append(current_type)

    # Iterate through the watch later list
    for i in range(1, n):
        if watch_later_list[i] == current_type:
            count += 1
        else:
            count += 2
            current_type = watch_later_list[i]
            types.append(current_type)

    # Return the minimum number of clicks
    return count

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    watch_later_list = input()
    print(f1(n, k, watch_later_list))
    print(f2(n, k, watch_later_list))

