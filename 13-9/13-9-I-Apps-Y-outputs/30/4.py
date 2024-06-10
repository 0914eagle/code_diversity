
def get_aggressive_dog(time, a, b):
    if time <= a:
        return 1
    elif time <= a + b:
        return 0
    else:
        return 1

def get_attacked_dogs(postman_time, milkman_time, garbage_man_time, a, b, c, d):
    postman_dog = get_aggressive_dog(postman_time, a, b)
    milkman_dog = get_aggressive_dog(milkman_time, c, d)
    garbage_man_dog = get_aggressive_dog(garbage_man_time, a, b) + get_aggressive_dog(garbage_man_time, c, d)
    return postman_dog, milkman_dog, garbage_man_dog

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    postman_dog, milkman_dog, garbage_man_dog = get_attacked_dogs(p, m, g, a, b, c, d)
    if postman_dog == 1 and milkman_dog == 1 and garbage_man_dog == 2:
        print("both")
    elif postman_dog == 1 and milkman_dog == 1 and garbage_man_dog == 1:
        print("one")
    else:
        print("none")

if __name__ == '__main__':
    main()

