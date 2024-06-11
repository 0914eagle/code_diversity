def order_by_points(nums):
    
    # My solution
    # return sorted(nums, key=lambda x: sum(int(i) for i in str(x)), reverse=True)

    # Best way
    return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), x), reverse=True)


if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))
