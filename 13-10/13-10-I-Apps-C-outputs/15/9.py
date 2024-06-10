
def get_maximum_amount(n, m, coupon_info):
    # Initialize a dictionary to store the counts of each number
    count = {}
    for i in range(m):
        q, w = coupon_info[i]
        count[q] = count.get(q, 0) + 1
    
    # Initialize a variable to store the maximum amount
    maximum = 0
    
    # Iterate over the dictionary and check if we can find a beautiful array
    for key, value in count.items():
        if value % 2 == 0:
            continue
        else:
            # If we can find a beautiful array, calculate the maximum amount
            maximum += key * value
    
    return maximum

def main():
    n, m = map(int, input().split())
    coupon_info = []
    for i in range(m):
        q, w = map(int, input().split())
        coupon_info.append((q, w))
    print(get_maximum_amount(n, m, coupon_info))

if __name__ == '__main__':
    main()

