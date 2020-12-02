import re

data = []
with open('2.in', 'r') as f:
    for l in f:
        g = re.match(r"(\d+)-(\d+) (\w): (.+)", l.strip()).groups()
        data.append((int(g[0]), int(g[1]), g[2], g[3]))


# Part 1
def part1():
    count = 0
    for min_, max_, char, pwd in data:
        if min_ <= pwd.count(char) <= max_:
            count += 1
    print(count)

part1()


# Part 2
def part2():
    count = 0
    for p1, p2, char, pwd in data:
        if (pwd[p1-1] == char) ^ (pwd[p2-1] == char):
            count += 1
    print(count)

part2()
