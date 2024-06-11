def triples_sum_to_zero(l: list):
    
    # Your code here
    l.sort()
    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1
        while left < right:
            if l[i] + l[left] + l[right] == 0:
                return True
            elif l[i] + l[left] + l[right] < 0:
                left += 1
            else:
                right -= 1
    return False


if __name