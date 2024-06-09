
def is_possible(area, perimeter):
    area_sum = 0
    for i in range(perimeter):
        for j in range(i, perimeter):
            if area_sum + i * j <= area:
                area_sum += i * j
            else:
                return False
    return area_sum == area

def main():
    area, perimeter = map(float, input().split())
    if is_possible(area, perimeter):
        print("Diablo is happy!")
    else:
        print("Need more materials!")

if __name__ == "__main__":
    main()

