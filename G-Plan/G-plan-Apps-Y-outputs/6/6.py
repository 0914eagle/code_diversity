
def find_good_candies(n, candies):
    prefix_sum_odd = [0] * (n + 1)
    prefix_sum_even = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum_odd[i] = prefix_sum_odd[i - 1] + (candies[i - 1] if i % 2 == 1 else 0)
        prefix_sum_even[i] = prefix_sum_even[i - 1] + (candies[i - 1] if i % 2 == 0 else 0)
    
    good_candies = 0
    for i in range(1, n + 1):
        odd_sum = prefix_sum_odd[i - 1] + prefix_sum_even[n] - prefix_sum_even[i]
        even_sum = prefix_sum_even[i - 1] + prefix_sum_odd[n] - prefix_sum_odd[i]
        
        if odd_sum == even_sum:
            good_candies += 1
    
    return good_candies

if __name__ == "__main__":
    n = int(input())
    candies = list(map(int, input().split()))
    
    result = find_good_candies(n, candies)
    print(result)
