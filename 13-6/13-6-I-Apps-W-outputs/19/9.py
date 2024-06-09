
def get_maximum_fruits(lemons, apples, pears):
    if lemons == 0 and apples == 0 and pears == 0:
        return 0
    
    max_lemons = lemons
    max_apples = apples // 2
    max_pears = pears // 4
    
    total_fruits = max_lemons + max_apples + max_pears
    
    return total_fruits

def main():
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    
    print(get_maximum_fruits(lemons, apples, pears))

if __name__ == '__main__':
    main()

