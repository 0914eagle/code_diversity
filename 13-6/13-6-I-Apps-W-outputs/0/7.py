
def execute_programme(programme):
    x = 0
    for statement in programme:
        if statement == "++X":
            x += 1
        elif statement == "--X":
            x -= 1
    return x

def main():
    n = int(input())
    programme = []
    for _ in range(n):
        programme.append(input())
    print(execute_programme(programme))

if __name__ == '__main__':
    main()

