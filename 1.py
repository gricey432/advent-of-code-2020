with open('1.in', 'r') as f:
    data = list(map(int, f))


# Part 1
def part1():
    for n in data:
        remainder = 2020 - n
        if remainder in data:
            print(remainder * n)
            return

part1()


# Part 2
def part2():
    for n in data:
        for j in data:
            remainder = 2020 - n - j
            if remainder in data:
                print(remainder * n * j)
                return

part2()
