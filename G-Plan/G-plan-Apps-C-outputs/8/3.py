ess_events_dreams_scenarios(n, lines):
    events = {}
    dreams = 0
    result = []

    for line in lines:
        if line[0] == 'E':
            event = line.split()[1]
            events[event] = True
        elif line[0] == 'D':
            dreams = int(line.split()[1])
        elif line[0] == 'S':
            scenario = line.split()[2:]
            valid = True
            for event in scenario:
                if event.startswith('!'):
                    if event[1:] in events or dreams > 0:
                        valid = False
                else:
                    if event not in events or dreams > 0:
                        valid = False
            if valid:
                result.append("Yes")
            elif dreams > 0:
                result.append(f"{dreams} Just A Dream")
            else:
                result.append("Plot Error")

    return result


if __name__ == "__main__":
    n = int(input())
    lines = [input() for _ in range(n)]
    results = process_events_dreams_scenarios(n, lines)
    for res in results:
        print(res)
