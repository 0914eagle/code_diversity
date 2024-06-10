
def get_dog_attacks(a, b, c, d, p, m, g):
    # Calculate the number of minutes until the first dog attack
    minutes_until_first_attack = (p + m + g) % (a + b + c + d)
    
    # Calculate the number of minutes until the second dog attack
    minutes_until_second_attack = (minutes_until_first_attack + a) % (a + b + c + d)
    
    # Determine which dog attacks each person
    if minutes_until_first_attack < a:
        postman_attack = "one"
    else:
        postman_attack = "none"
    
    if minutes_until_second_attack < c:
        milkman_attack = "one"
    else:
        milkman_attack = "none"
    
    if (minutes_until_first_attack + minutes_until_second_attack) < (a + c):
        garbage_man_attack = "both"
    elif minutes_until_first_attack < a:
        garbage_man_attack = "one"
    else:
        garbage_man_attack = "none"
    
    return postman_attack, milkman_attack, garbage_man_attack

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    postman_attack, milkman_attack, garbage_man_attack = get_dog_attacks(a, b, c, d, p, m, g)
    print(postman_attack)
    print(milkman_attack)
    print(garbage_man_attack)

if __name__ == '__main__':
    main()

