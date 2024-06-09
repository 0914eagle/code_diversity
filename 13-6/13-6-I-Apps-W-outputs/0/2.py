
def execute_program(program):
    x = 0
    for statement in program:
        if statement == "++X":
            x += 1
        elif statement == "--X":
            x -= 1
    return x

def main():
    n = int(input())
    program = []
    for _ in range(n):
        program.append(input())
    print(execute_program(program))

if __name__ == '__main__':
    main()

