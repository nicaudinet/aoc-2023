with open("inputs/day02.txt", "r") as file:
    lines = file.read().splitlines()

test = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"


def parse(line):
    id_str, rest = line.split(": ")
    id_num = int(id_str.split(" ")[1])
    rounds = []
    for game_str in rest.split("; "):
        sample = {}
        for color_str in game_str.split(", "):
            num, color = color_str.split(" ")
            sample[color] = int(num)
        rounds.append(sample)
    return id_num, rounds


def sample_is_possible(sample):
    red = "red" not in sample or sample["red"] <= 12
    green = "green" not in sample or sample["green"] <= 13
    blue = "blue" not in sample or sample["blue"] <= 14
    return red and green and blue


def is_possible(rounds):
    return all(sample_is_possible(sample) for sample in rounds)


games = [parse(line) for line in lines]
possible_games = [id_num for id_num, rounds in games if is_possible(rounds)]
print(sum(possible_games))


def minimum_cube_power(rounds):
    reds = []
    greens = []
    blues = []
    for sample in rounds:
        reds.append(0 if "red" not in sample else sample["red"])
        greens.append(0 if "green" not in sample else sample["green"])
        blues.append(0 if "blue" not in sample else sample["blue"])
    return max(reds) * max(greens) * max(blues)


powers = [minimum_cube_power(rounds) for _, rounds in games]
print(sum(powers))
