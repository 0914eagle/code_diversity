
def will_turn_on_ac(temperature):
    if temperature >= 30:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    temperature = int(input())
    print(will_turn_on_ac(temperature))

