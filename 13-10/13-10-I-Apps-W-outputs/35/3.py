
def get_detachments(soldiers, days):
    detachments = []
    for day in range(days):
        detachment = []
        for soldier in soldiers:
            if soldier not in detachment:
                detachment.append(soldier)
                if len(detachment) == day + 1:
                    break
        detachments.append(detachment)
    return detachments

def get_output(detachments):
    output = []
    for detachment in detachments:
        output.append(str(len(detachment)) + " " + " ".join(map(str, detachment)))
    return "\n".join(output)

def main():
    soldiers, days = map(int, input().split())
    soldiers = list(map(int, input().split()))
    detachments = get_detachments(soldiers, days)
    print(get_output(detachments))

if __name__ == '__main__':
    main()

