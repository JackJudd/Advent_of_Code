with open('input.txt') as text:
    lines = text.read().splitlines()

gamma_rate = [0] * len(lines[0])
epsilon_rate = [0] * len(lines[0])

def counter(binary_strings):
    one_count2 = [0] * len(binary_strings[0])
    for line in binary_strings:
        for i,x in enumerate(line):
            if int(x) == 1:
                one_count2[i] += 1
    return one_count2

one_count = counter(lines)

print(one_count)

for x in one_count:
    for i,x in enumerate(one_count):
        if x < len(lines)//2:
            gamma_rate[i] = 0
            epsilon_rate[i] = 1
        elif x > len(lines)//2:
            gamma_rate[i] = 1
            epsilon_rate[i] = 0

print(gamma_rate)
print(epsilon_rate)

bin1 = int("".join(str(x) for x in gamma_rate), 2)
print(bin1)

bin2 = int("".join(str(x) for x in epsilon_rate), 2)
print(bin2)

bin_final = bin1 * bin2
print(bin_final)

#P2

oxygen_lines = lines.copy()
co2_lines = lines.copy()

for i in range(len(one_count)):
    one_count = counter(oxygen_lines)
    if one_count[i] < len(oxygen_lines) - one_count[i]:
        oxygen_lines = [x for x in oxygen_lines if x[i] == '0']
    elif one_count[i] > len(oxygen_lines) - one_count[i]:
        oxygen_lines = [x for x in oxygen_lines if x[i] == '1']
    elif one_count[i] == len(oxygen_lines) - one_count[i]:
        oxygen_lines = [x for x in oxygen_lines if x[i] == '1']
    if len(oxygen_lines) == 1:
        break

print(oxygen_lines)

for i in range(len(one_count)):
    one_count = counter(co2_lines)
    print(one_count)
    if one_count[i] < len(co2_lines) - one_count[i]:
        co2_lines = [x for x in co2_lines if x[i] == '1']
    elif one_count[i] > len(co2_lines) - one_count[i]:
        co2_lines = [x for x in co2_lines if x[i] == '0']
    elif one_count[i] == len(co2_lines) - one_count[i]:
        co2_lines = [x for x in co2_lines if x[i] == '0']
    print(co2_lines)
    if len(co2_lines) == 1:
        break

print(co2_lines)

bin3 = int(oxygen_lines[0], 2)
print(bin3)

bin4 = int(co2_lines[0], 2)
print(bin4)

bin_final2 = bin3 * bin4
print(bin_final2)