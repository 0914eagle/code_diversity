
def f1(n, m, coupons):
    # Initialize the maximum amount of money that can be paid
    max_money = 0
    
    # Iterate over all possible arrays
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # Check if the current array is beautiful
                if is_beautiful(i, j, k, n):
                    # Calculate the amount of money that can be paid with the current array
                    money = calculate_money(i, j, k, n, coupons)
                    
                    # Update the maximum amount of money if necessary
                    if money > max_money:
                        max_money = money
    
    return max_money

def is_beautiful(a, b, c, n):
    # Check if a, b, and c are distinct
    if a == b or a == c or b == c:
        return False
    
    # Initialize the number of positions where a, b, and c occur
    count_a = 0
    count_b = 0
    count_c = 0
    
    # Iterate over all positions
    for i in range(1, n + 1):
        # Check if a occurs at the current position
        if i == a or i == b or i == c:
            count_a += 1
        
        # Check if b occurs at the current position
        if i == b or i == c or i == a:
            count_b += 1
        
        # Check if c occurs at the current position
        if i == c or i == a or i == b:
            count_c += 1
    
    # Check if at least one of the two conditions is met for a and b
    if count_a >= 1 and count_b >= 1:
        return True
    
    # Check if at least one of the two conditions is met for a and c
    if count_a >= 1 and count_c >= 1:
        return True
    
    # Check if at least one of the two conditions is met for b and c
    if count_b >= 1 and count_c >= 1:
        return True
    
    return False

def calculate_money(a, b, c, n, coupons):
    # Initialize the amount of money that can be paid
    money = 0
    
    # Iterate over all coupons
    for coupon in coupons:
        # Check if the current coupon is valid
        if coupon[0] in [a, b, c] and coupon[1] <= n:
            money += coupon[1]
    
    return money

def f2(n, m, coupons):
    # Initialize the maximum amount of money that can be paid
    max_money = 0
    
    # Iterate over all possible arrays
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # Check if the current array is beautiful
                if is_beautiful(i, j, k, n):
                    # Calculate the amount of money that can be paid with the current array
                    money = calculate_money(i, j, k, n, coupons)
                    
                    # Update the maximum amount of money if necessary
                    if money > max_money:
                        max_money = money
    
    return max_money

if __name__ == '__main__':
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    
    print(f2(n, m, coupons))

