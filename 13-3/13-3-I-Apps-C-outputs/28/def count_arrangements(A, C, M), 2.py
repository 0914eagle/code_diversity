
import math

def count_arrangements(A, C, M):
    modulo = 1000000007
    total_boxes = A + C + M
    arrangements = 1
    for i in range(total_boxes - 1):
        arrangements *= (A + C + M - i)
        arrangements %= modulo
    return arrangements

