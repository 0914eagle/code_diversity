
def get_operation_type(operation):
    if operation[0] == 'a':
        return 1
    elif operation[0] == 'b':
        return 2
    else:
        return 3

def get_stack_labels(operation):
    if operation[0] == 'a':
        return [int(operation[1])]
    elif operation[0] == 'b':
        return [int(operation[1])]
    else:
        return [int(operation[1]), int(operation[2])]

def perform_operation(operation, stacks):
    operation_type = get_operation_type(operation)
    stack_labels = get_stack_labels(operation)
    if operation_type == 1:
        stacks[stack_labels[0]].append(len(stacks))
    elif operation_type == 2:
        return stacks[stack_labels[0]].pop()
    else:
        return len(set(stacks[stack_labels[0]] + stacks[stack_labels[1]]))

def main():
    num_operations = int(input())
    stacks = [[] for _ in range(num_operations)]
    for _ in range(num_operations):
        operation = input()
        result = perform_operation(operation, stacks)
        if result is not None:
            print(result)

if __name__ == '__main__':
    main()

