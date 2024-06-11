def minSubArraySum(nums):
    
    # 1.
    # if not nums:
    #     return 0
    #
    # min_sum = nums[0]
    # cur_sum = nums[0]
    # for i in range(1, len(nums)):
    #     cur_sum += nums[i]
    #     min_sum = min(min_sum, cur_sum)
    #     if cur_sum < 0:
    #         cur_sum = 0
    # return min_sum

    # 2.
    # if not nums:
    #     return 0
    #
    # min_sum = nums[0]
    # cur_sum = nums[0]
    # for i in range(1, len(nums)):
    #     cur_sum = max(cur_sum, nums[i])
    #     min_sum = min(min_sum, cur_sum)
    # return min_sum

    # 3.
    # if not nums:
    #     return 0
    #
    # min_sum = nums[0]
    # cur_sum = nums[0]
    # for i in range(1, len(nums)):
    #     cur_sum = max(cur_sum + nums[i], nums[i])
    #     min_sum = min(min_sum, cur_sum)
    # return min_sum

    # 4.
    # if not nums:
    #     return 0
    #
    # min_sum = nums[0]
    # cur_sum = nums[0]
    # for i in range(1, len(nums)):
    #     cur_sum = max(cur_sum, nums[i])
    #     min_sum = min(min_sum, cur_sum - nums[i])
    # return min_sum

    # 5.
    # if not nums:
    #     return 0
    #
    # min_sum = nums[0]
    # cur_sum = nums[0]
    # for i in