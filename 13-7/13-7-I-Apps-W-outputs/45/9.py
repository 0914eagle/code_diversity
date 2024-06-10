
def get_weight_after_fall(weight, height, stone1_weight, stone1_height, stone2_weight, stone2_height):
    while height > 0:
        weight += height
        if height == stone1_height or height == stone2_height:
            weight -= min(stone1_weight, stone2_weight)
        height -= 1
    return weight

def main():
    weight, height = map(int, input().split())
    stone1_weight, stone1_height = map(int, input().split())
    stone2_weight, stone2_height = map(int, input().split())
    print(get_weight_after_fall(weight, height, stone1_weight, stone1_height, stone2_weight, stone2_height))

if __name__ == '__main__':
    main()

