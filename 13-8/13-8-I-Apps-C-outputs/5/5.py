
def get_min_extensions(a, b, h, w, n, a_list):
    # Initialize variables
    min_extensions = 0
    current_h = h
    current_w = w

    # Loop through the list of extensions
    for i in range(n):
        # Check if the current extension can be applied
        if a_list[i] <= current_h or a_list[i] <= current_w:
            # Apply the extension
            if a_list[i] <= current_h:
                current_h *= a_list[i]
            else:
                current_w *= a_list[i]

            # Increment the number of extensions used
            min_extensions += 1

    # Check if the rectangle can be placed on the field
    if current_h < a or current_w < b:
        return -1

    return min_extensions

def main():
    a, b, h, w, n = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, a_list))

if __name__ == '__main__':
    main()

