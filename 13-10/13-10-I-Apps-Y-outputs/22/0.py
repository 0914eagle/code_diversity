
def get_attack_count(health, attack_power):
    return (health - 1) // attack_power + 1

def main():
    health, attack_power = map(int, input().split())
    print(get_attack_count(health, attack_power))

if __name__ == '__main__':
    main()

