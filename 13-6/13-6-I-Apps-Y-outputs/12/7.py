
def is_triangle(sticks):
    
    sticks.sort()
    return sticks[0] + sticks[1] > sticks[2]

def main():
    num_sticks = int(input())
    sticks = [int(input()) for _ in range(num_sticks)]
    if is_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

