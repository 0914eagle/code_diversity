
def get_number_of_unique_cheeses(cheese_list):
    return len(set(cheese_list))

def main():
    num_cheeses = int(input())
    cheese_list = []
    for i in range(num_cheeses):
        cheese_name, cheese_type = input().split()
        cheese_list.append(cheese_name)
    print(get_number_of_unique_cheeses(cheese_list))

if __name__ == '__main__':
    main()

