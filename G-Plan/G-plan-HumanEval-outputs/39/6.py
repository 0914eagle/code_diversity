
from typing import List

def sum_of_digits(num: int) -> int:
    return sum(int(d) for d in str(abs(num)))

def count_nums(arr: List[int]) -> int:
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(count_nums(arr))
