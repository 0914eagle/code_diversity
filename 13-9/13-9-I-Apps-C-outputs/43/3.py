
def get_minimum_clicks(n, k, watch_later_list):
    # Initialize variables
    current_type = watch_later_list[0]
    num_types = 1
    num_clicks = 0
    
    # Iterate through the watch later list
    for i in range(1, n):
        # If the current type is the same as the previous type, increment the number of types
        if watch_later_list[i] == current_type:
            num_types += 1
        # If the current type is different from the previous type, increment the number of clicks
        else:
            num_clicks += 1
            current_type = watch_later_list[i]
    
    # Add the final click if there are more than one type
    if num_types > 1:
        num_clicks += 1
    
    return num_clicks

def main():
    n, k = map(int, input().split())
    watch_later_list = list(input())
    print(get_minimum_clicks(n, k, watch_later_list))

if __name__ == '__main__':
    main()

