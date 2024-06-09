
def get_max_fruits(lemons, apples, pears):
    if lemons == 0 and apples == 0 and pears == 0:
        return 0
    
    total_fruits = lemons + apples + pears
    lemon_ratio = 1
    apple_ratio = 2
    pear_ratio = 4
    
    if total_fruits % (lemon_ratio + apple_ratio + pear_ratio) != 0:
        return 0
    
    return total_fruits // (lemon_ratio + apple_ratio + pear_ratio)

def main():
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    
    print(get_max_fruits(lemons, apples, pears))

if __name__ == '__main__':
    main()

