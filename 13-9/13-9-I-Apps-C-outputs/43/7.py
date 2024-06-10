
def get_min_clicks(n, k, list_str):
    # Initialize variables
    clicks = 0
    types = []
    current_type = list_str[0]
    types.append(current_type)

    # Iterate through the list
    for i in range(1, n):
        # If the current video is of a different type, play the next video
        if list_str[i] != current_type:
            clicks += 1
            current_type = list_str[i]
            types.append(current_type)
        # If the current video is of the same type, play the next video of the same type
        else:
            clicks += 1
            current_type = list_str[i]

    # Return the minimum number of clicks
    return clicks

def main():
    n, k = map(int, input().split())
    list_str = input()
    print(get_min_clicks(n, k, list_str))

if __name__ == '__main__':
    main()

