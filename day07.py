import functools
import itertools

with open("inputs/day07.txt", "r") as file:
    contents = file.read()


def parse(line):
    hand, bid = line.split(" ")
    return hand, int(bid)


def type_strength(hand):
    hand = [list(g) for _, g in itertools.groupby(sorted(hand))]
    hand_type = list(sorted(map(len, hand)))
    if hand_type == [5]:
        return 10
    elif hand_type == [1, 4]:
        return 9
    elif hand_type == [2, 3]:
        return 8
    elif hand_type == [1, 1, 3]:
        return 7
    elif hand_type == [1, 2, 2]:
        return 6
    elif hand_type == [1, 1, 1, 2]:
        return 5
    else:
        return 4


def card_strength(card):
    return "23456789TJQKA".find(card)


def stronger_than(line1, line2):
    hand1, _ = line1
    hand2, _ = line2
    if type_strength(hand1) == type_strength(hand2):
        for c1, c2 in zip(hand1, hand2):
            if c1 != c2:
                return card_strength(c1) - card_strength(c2)
    return type_strength(hand1) - type_strength(hand2)


# contents = "\n".join(
#     [
#         "32T3K 765",
#         "T55J5 684",
#         "KK677 28",
#         "KTJJT 220",
#         "QQQJA 483",
#     ]
# )


hands = [parse(line) for line in contents.splitlines()]
ranked_hands = sorted(hands, key=functools.cmp_to_key(stronger_than))
print(sum([(i + 1) * bid for i, (_, bid) in enumerate(ranked_hands)]))


def card_strength(card):
    return "J23456789TQKA".find(card)


def type_strength(hand):
    hand = [c for c in hand if c != "J"]
    if hand == []:
        return 10
    hand = [list(g) for _, g in itertools.groupby(sorted(hand))]
    hand_type = list(sorted(map(len, hand)))
    hand_type[-1] += 5 - sum(hand_type)
    if hand_type == [5]:
        return 10
    elif hand_type == [1, 4]:
        return 9
    elif hand_type == [2, 3]:
        return 8
    elif hand_type == [1, 1, 3]:
        return 7
    elif hand_type == [1, 2, 2]:
        return 6
    elif hand_type == [1, 1, 1, 2]:
        return 5
    else:
        return 4


# def type_strength(hand):
#     hand = [c for c in hand if c != "J"]
#     hand = [list(g) for _, g in itertools.groupby(sorted(hand))]
#     hand_type = list(sorted(map(len, hand)))
#     if len(hand_type) == 1:
#         return 10
#     elif len(hand_type) == 2 and hand_type[0] == 1:
#         return 9
#     elif len(hand_type) == 2 and hand_type[0] == 2:
#         return 8
#     elif len(hand_type) == 3 and hand_type[0:2] == [1, 1]:
#         return 7
#     elif len(hand_type) == 3 and hand_type[0:2] == [1, 2]:
#         return 6
#     elif len(hand_type) == 4:
#         return 5
#     else:
#         return 4


def stronger_than(line1, line2):
    hand1, _ = line1
    hand2, _ = line2
    if type_strength(hand1) == type_strength(hand2):
        for c1, c2 in zip(hand1, hand2):
            if c1 != c2:
                return card_strength(c1) - card_strength(c2)
    return type_strength(hand1) - type_strength(hand2)


hands = [parse(line) for line in contents.splitlines()]
ranked_hands = sorted(hands, key=functools.cmp_to_key(stronger_than))
print(sum([(i + 1) * bid for i, (_, bid) in enumerate(ranked_hands)]))
