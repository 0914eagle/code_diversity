
def get_detachments(n, k, beauties):
    detachments = []
    for i in range(k):
        detachment = []
        for j in range(n):
            if beauties[j] not in detachment:
                detachment.append(beauties[j])
                if len(detachment) == i + 1:
                    break
        detachments.append(detachment)
    return detachments

def get_output(n, k, beauties, detachments):
    output = []
    for i in range(k):
        output.append(str(len(detachments[i])) + " " + " ".join(str(x) for x in detachments[i]))
    return "\n".join(output)

if __name__ == '__main__':
    n, k = map(int, input().split())
    beauties = list(map(int, input().split()))
    detachments = get_detachments(n, k, beauties)
    print(get_output(n, k, beauties, detachments))

