
def get_max_amount(n, m, coupons):
    # Initialize a dictionary to store the count of each number
    count = {}
    for i in range(1, n+1):
        count[i] = 0
    
    # Iterate over the coupons and increment the count of each number
    for coupon in coupons:
        count[coupon[0]] += 1
    
    # Initialize a variable to store the maximum amount
    max_amount = 0
    
    # Iterate over the numbers and check if they are beautiful
    for i in range(1, n+1):
        if count[i] > 0:
            # Check if the number is beautiful
            if is_beautiful(i, count):
                # If it is, add its cost to the maximum amount
                max_amount += i * count[i]
    
    return max_amount

def is_beautiful(x, count):
    # Check if x occurs in the array
    if count[x] == 0:
        return False
    
    # Iterate over the numbers and check if they have a pair
    for i in range(1, x):
        if count[i] > 0:
            # Check if the pair is beautiful
            if is_pair_beautiful(x, i, count):
                return True
    
    return False

def is_pair_beautiful(x, y, count):
    # Check if the pair is beautiful
    if count[x] == 0 or count[y] == 0:
        return False
    
    # Iterate over the numbers and check if they have a position j
    for j in range(1, x):
        # Check if the position j is a beautiful pair
        if is_beautiful_pair(x, y, j, count):
            return True
    
    return False

def is_beautiful_pair(x, y, j, count):
    # Check if the position j is a beautiful pair
    if count[x] == 0 or count[y] == 0:
        return False
    
    if j == x or j == y:
        return False
    
    # Check if the pair is adjacent to each other
    if abs(x - y) == 1:
        return True
    
    return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_max_amount(n, m, coupons))

