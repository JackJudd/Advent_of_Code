with open('input.txt') as text:
    file = text.readlines()
    file = [int(n) for n in file]


count = 0
prev_depth = file[0] + file[1] + file[2]
curr_depth = 0

for x in range(len(file)):
    if x + 2 >= len(file):
        break
    curr_depth = file[x] + file[x+1] + file[x+2]
    if curr_depth > prev_depth:
        count += 1
    prev_depth = curr_depth

print(count)