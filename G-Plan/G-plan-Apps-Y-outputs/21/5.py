
import math

def match_fits_in_box(match_length, box_width, box_height):
    diagonal_length = math.sqrt(box_width**2 + box_height**2)
    return "DA" if match_length <= diagonal_length else "NE"

def process_matches():
    n, box_width, box_height = map(int, input().split())
    for _ in range(n):
        match_length = int(input())
        print(match_fits_in_box(match_length, box_width, box_height))

if __name__ == "__main__":
    process_matches()
