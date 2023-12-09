import math

with open("inputs/day08.txt", "r") as file:
    contents = file.read()


def parse_graph(graph_lines):
    graph = {}
    for line in graph_lines.splitlines():
        curr, rest = line.split(" = ")
        left, right = rest[1:-1].split(", ")
        graph[curr] = (left, right)
    return graph


instructions, graph_lines = contents.split("\n\n")
graph = parse_graph(graph_lines)
N = len(instructions)
curr = "AAA"
count = 0
i = 0
while curr != "ZZZ":
    instruction = 1 if instructions[i] == "R" else 0
    curr = graph[curr][instruction]
    count += 1
    i = (i + 1) % N
print(count)

paths = [(n, 0) for n in graph if n[-1] == "A"]
cycles = []
end_nodes = [n for n in graph if n[-1] == "Z"]
count = 0
i = 0
stop = False
while paths != []:
    instruction = 1 if instructions[i] == "R" else 0
    new_paths = []
    for curr_node, count_since_end in paths:
        next_node = graph[curr_node][instruction]
        if count_since_end > 0 and next_node in end_nodes:
            cycles.append((count - count_since_end, count_since_end))
        elif count_since_end > 0 or next_node in end_nodes:
            count_since_end += 1
            new_paths.append((next_node, count_since_end))
        else:
            new_paths.append((next_node, count_since_end))
    paths = new_paths
    count += 1
    i = (i + 1) % N
# print(count, paths)
cycles = [(s + 1, l) for s, l in cycles]

starts = [start - length for start, length in cycles]
cycle_lengths = [length for _, length in cycles]
print(max(starts) + math.lcm(*cycle_lengths))
