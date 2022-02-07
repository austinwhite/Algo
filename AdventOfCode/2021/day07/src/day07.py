from statistics import median

infile = "../input/data.in"
positions = []

with open(infile) as f:
    positions = [int(x) for x in f.readline().strip().split(',')]

def part1():
    med = int(median(positions))

    total_fuel = 0
    for num in positions:
        total_fuel += abs(med - num)
    
    return total_fuel

print("Part 1:", part1())