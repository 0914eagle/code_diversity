ess_event(event, events, dreams):
    if event[0] == 'E':
        events.add(event[1])
    elif event[0] == 'D':
        for _ in range(event[1]):
            last_event = events.pop()
            dreams.add(last_event)

def check_scenario(scenario, events, dreams):
    for event in scenario[2:]:
        if event[0] == '!':
            if event[1:] in events or event[1:] not in dreams:
                return "Plot Error"
        else:
            if event not in events and event not in dreams:
                return "Plot Error"
    return "Yes"

def solve_problem(n, lines):
    events = set()
    dreams = set()
    output = []

    for line in lines:
        if line[0] == 'E' or line[0] == 'D':
            process_event(line, events, dreams)
        elif line[0] == 'S':
            output.append(check_scenario(line, events, dreams))

    return output

if __name__ == "__main__":
    n = int(input())
    lines = [input().split() for _ in range(n)]
    result = solve_problem(n, lines)
    for res in result:
        print(res)
