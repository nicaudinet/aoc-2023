import math
import operator
from functools import reduce

with open("inputs/day06.txt", "r") as file:
    contents = file.read()

times, distances = contents.splitlines()
times = [float(t) for t in times.split(" ") if t != "" and t[0] != "T"]
distances = [float(d) for d in distances.split(" ") if d != "" and d[0] != "D"]

# times = [7, 15, 30]
# distances = [9, 40, 200]

options = []
for time, distance in zip(times, distances):
    z1 = math.ceil((time - math.sqrt(time**2 - 4 * distance)) / 2)
    z2 = math.floor((time + math.sqrt(time**2 - 4 * distance)) / 2)
    if z1 * z2 == distance:
        options.append(z2 - z1 - 1)
    else:
        options.append(z2 - z1 + 1)
print(reduce(operator.mul, options))

times, dists = contents.splitlines()
time = float("".join([t for t in times.split(" ") if t != "" and t[0] != "T"]))
dist = float("".join([d for d in dists.split(" ") if d != "" and d[0] != "D"]))
z1 = math.ceil((time - math.sqrt(time**2 - 4 * dist)) / 2)
z2 = math.floor((time + math.sqrt(time**2 - 4 * dist)) / 2)
if z1 * z2 == dist:
    print(z2 - z1 - 1)
else:
    print(z2 - z1 + 1)
