
def get_maximum_fruits(lemons, apples, pears):
    if lemons == 0 and apples == 0 and pears == 0:
        return 0
    
    max_lemons = min(lemons, apples // 2, pears // 4)
    max_apples = max_lemons * 2
    max_pears = max_lemons * 4
    
    return max_lemons + max_apples + max_pears

def main():
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    
    print(get_maximum_fruits(lemons, apples, pears))

if __name__ == '__main__':
    main()

