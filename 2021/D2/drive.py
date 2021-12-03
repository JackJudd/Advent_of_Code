with open('input.txt') as text:
    file = text.read().splitlines()

horz = 0
depth = 0


for line in file:
    parts = line.split(" ")
    direction,factor = parts[0], int(parts[1])
    if direction == 'forward':
        horz += factor
    if direction == 'up':
        depth -= factor
    if direction == 'down':
        depth += factor

total = depth * horz
print(total)


#P2

total = 0
horz = 0
depth = 0
aim = 0


for line in file:
    parts = line.split(" ")
    direction,factor = parts[0], int(parts[1])
    if direction == 'forward':
        horz += factor
        depth += (aim * factor)
    if direction == 'up':
        aim -= factor
    if direction == 'down':
        aim += factor
    print(depth)
    print(aim)
    

print(depth)
print(horz)
total = depth * horz
print(total)