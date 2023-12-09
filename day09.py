with open("inputs/day09.txt", "r") as file:
    contents = file.read()

# contents = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45"


def extrapolate(sequence):
    history = [sequence]
    while not all([x == 0 for x in history[-1]]):
        prev = history[-1]
        next = []
        for i in range(len(prev) - 1):
            next.append(prev[i + 1] - prev[i])
        history.append(next)
    for i in range(len(history)):
        idx = len(history) - i - 1
        history[idx - 1].append(history[idx][-1] + history[idx - 1][-1])
    return history[0][-1]


def extrapolate_back(sequence):
    history = [sequence]
    while not all([x == 0 for x in history[-1]]):
        prev = history[-1]
        next = []
        for i in range(len(prev) - 1):
            next.append(prev[i + 1] - prev[i])
        history.append(next)
    for i in range(len(history)):
        idx = len(history) - i - 1
        history[idx - 1].insert(0, history[idx - 1][0] - history[idx][0])
    return history[0][0]


sequences = [[int(n) for n in line.split(" ")] for line in contents.splitlines()]
print(sum([extrapolate(seq) for seq in sequences]))
print(sum([extrapolate_back(seq) for seq in sequences]))
