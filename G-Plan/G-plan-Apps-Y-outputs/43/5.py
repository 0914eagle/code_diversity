
def input_data():
    return map(int, input().split())

def calculate_sum(a, b):
    return a + b

if __name__ == '__main__':
    a, b = input_data()
    total = calculate_sum(a, b)
    if total < 10:
        print(total)
    else:
        print("error")
