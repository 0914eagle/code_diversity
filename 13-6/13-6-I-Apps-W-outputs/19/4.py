
def get_max_fruits(lemons, apples, pears):
    if lemons == 0 and apples == 0 and pears == 0:
        return 0
    
    max_lemons = lemons
    max_apples = apples // 2
    max_pears = pears // 4
    
    max_fruits = max_lemons + max_apples + max_pears
    
    return max_fruits

def main():
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    
    max_fruits = get_max_fruits(lemons, apples, pears)
    print(max_fruits)

if __name__ == '__main__':
    main()

