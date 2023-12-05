import math

with open("inputs/day04.txt", "r") as file:
    lines = file.read().splitlines()

test = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def parse(card):
    name, rest = card.split(": ")
    winners, mine = rest.split(" | ")
    winners = set([int(num) for num in winners.split(" ") if num != ""])
    mine = set([int(num) for num in mine.split(" ") if num != ""])
    return winners, mine


def eval(card):
    a, b = card
    overlap = len(a & b)
    return math.floor(2 ** (overlap - 1))


cards = [eval(parse(line)) for line in lines]
print(sum(cards))

test = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def eval(card):
    winners, mine = card
    return len(winners & mine)


cards = [(i, eval(parse(line))) for i, line in enumerate(lines)]
nums = [1 for _ in range(len(cards))]
for i, card in cards:
    for j in range(i + 1, i + 1 + card):
        nums[j] += nums[i]
print(sum(nums))
