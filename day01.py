with open("inputs/day01.txt", "r") as file:
    lines = file.read().splitlines()


def parse(line):
    digits = [c for c in line if c in "0123456789"]
    value = "".join([digits[0], digits[-1]])
    return int(value)


values = [parse(line) for line in lines]
print(sum(values))

test_input = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def parse(line):
    string_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for string, digit in string_digits.items():
        line = line.replace(string, string + digit + string)
    digits = [c for c in line if c in "0123456789"]
    value = "".join([digits[0], digits[-1]])
    return int(value)


values = [parse(line) for line in lines]
print(sum(values))
