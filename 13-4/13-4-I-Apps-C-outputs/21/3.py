
def solve(numbers):
    n = int(input())
    numbers = list(map(float, input().split()))
    diff = 0
    for i in range(n):
        for j in range(i+1, n):
            a_i = round(numbers[i])
            a_j = round(numbers[j])
            diff += abs(a_i + a_j - numbers[i] - numbers[j])
    return diff

