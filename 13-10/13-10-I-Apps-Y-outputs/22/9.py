
def get_attacks_needed(health, attack_amount):
    return (health - 1) // attack_amount + 1

def main():
    health, attack_amount = map(int, input().split())
    print(get_attacks_needed(health, attack_amount))

if __name__ == '__main__':
    main()

