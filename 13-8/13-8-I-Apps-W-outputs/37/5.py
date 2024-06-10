
def get_max_lit_time(a, M):
    # Initialize variables
    n = len(a)
    max_lit_time = 0
    curr_lit_time = 0
    curr_state = "on"
    prev_state = "off"
    
    # Iterate through the array
    for i in range(n):
        # If the current state is "on", turn it off
        if curr_state == "on":
            curr_state = "off"
            curr_lit_time += a[i] - prev_state
            prev_state = a[i]
        # If the current state is "off", turn it on
        else:
            curr_state = "on"
            prev_state = a[i]
    
    # Add the time when the lamp is turned off
    curr_lit_time += M - prev_state
    
    # Return the maximum lit time
    return curr_lit_time

def main():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_lit_time(a, M))

if __name__ == '__main__':
    main()

