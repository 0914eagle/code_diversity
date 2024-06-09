
import sys

def get_purchased_houses(L, R):
    purchased_houses = 0
    for house_number in range(L, R+1):
        house_number_str = str(house_number)
        if '4' in house_number_str:
            continue
        sixes = house_number_str.count('6')
        eights = house_number_str.count('8')
        if sixes == eights:
            purchased_houses += 1
    return purchased_houses

L, R = map(int, sys.stdin.readline().split())
print((get_purchased_houses(L, R) % 1000000007))

