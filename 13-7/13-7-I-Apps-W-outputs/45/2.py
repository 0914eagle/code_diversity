
def get_final_weight(weight, height, stone1_weight, stone1_height, stone2_weight, stone2_height):
    while height > 0:
        weight += height
        if height == stone1_height or height == stone2_height:
            weight -= min(stone1_weight, stone2_weight)
        height -= 1
    return max(weight, 0)

def main():
    weight, height = map(int, input().split())
    stone1_weight, stone1_height = map(int, input().split())
    stone2_weight, stone2_height = map(int, input().split())
    final_weight = get_final_weight(weight, height, stone1_weight, stone1_height, stone2_weight, stone2_height)
    print(final_weight)

if __name__ == '__main__':
    main()

