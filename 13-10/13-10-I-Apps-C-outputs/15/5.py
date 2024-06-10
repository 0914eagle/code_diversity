
def get_maximum_cost(n, m, coupons):
    # Initialize a dictionary to store the count of each number
    count = {}
    for q, w in coupons:
        count[q] = count.get(q, 0) + 1
    
    # Initialize a list to store the numbers that occur in the array
    numbers = []
    
    # Iterate through the dictionary and add the numbers to the list
    for q, cnt in count.items():
        for i in range(cnt):
            numbers.append(q)
    
    # Sort the list in non-decreasing order
    numbers.sort()
    
    # Initialize a variable to store the maximum cost
    max_cost = 0
    
    # Iterate through the list and calculate the maximum cost
    for i in range(n):
        q = numbers[i]
        w = count[q]
        max_cost += w
    
    return max_cost

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_cost(n, m, coupons))

if __name__ == '__main__':
    main()

