def order_by_points(nums):
    
    # your code here
    # return sorted(nums, key=lambda x: sum(int(i) for i in str(x)), reverse=True)
    return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), x), reverse=True)


if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))
