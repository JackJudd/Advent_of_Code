open('input.txt')
with open('input.txt') as f:
    lines = list(f.read())

count = 0
for x in lines:
    if x == '(':
        count += 1
    elif x == ')':
        count -= 1

print(count)

count = 0
position = 0
for i,x in enumerate(lines):
    if x == '(':
        count += 1
    elif x == ')':
        count -= 1
        if count == -1:
            print(i+1)
            exit()