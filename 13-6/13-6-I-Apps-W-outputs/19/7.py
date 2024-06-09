
def get_max_fruits(lemons, apples, pears):
    # Calculate the maximum number of fruits that can be used to make a compote
    max_fruits = min(lemons, apples // 2, pears // 4)
    return max_fruits

def main():
    lemons, apples, pears = map(int, input().split())
    print(get_max_fruits(lemons, apples, pears))

if __name__ == '__main__':
    main()

