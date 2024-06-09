
def get_max_fruits(lemons, apples, pears):
    if lemons == 0 and apples == 0 and pears == 0:
        return 0
    if lemons < 0 or apples < 0 or pears < 0:
        return -1
    max_lemons = min(lemons, apples // 2, pears // 4)
    max_apples = min(apples, lemons * 2, pears // 4)
    max_pears = min(pears, lemons * 4, apples // 2)
    return max_lemons + max_apples + max_pears

def main():
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    print(get_max_fruits(lemons, apples, pears))

if __name__ == '__main__':
    main()

