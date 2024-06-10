
def get_ingredients_value(values):
    return sum(values) / len(values)

def get_max_value(values):
    if len(values) == 1:
        return values[0]
    else:
        return max(get_ingredients_value(values), get_max_value(values[1:]))

if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))
    print(get_max_value(values))

