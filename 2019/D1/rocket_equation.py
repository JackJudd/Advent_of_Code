with open('input.txt') as text:
    file = text.readlines()

masses = [int(n) for n in file]
total = 0

for mass in masses:
    total += mass//3 - 2


print(total)


#P2

masses = [int(n) for n in file]
total = 0

for mass in masses:
        while mass > 0:
            mass = (mass//3 - 2)
            if mass > 0:
                total += mass
                print(total)
                if mass <= 0:
                    break

print(total)



# for mass in masses:
#     inter_sum = mass//3 - 2
#     if inter_sum > 0:
#         inter_sum2 += inter_sum//3 - 2
#         if inter_sum2 >0:
#             inter_sum3 += inter_sum2//3 - 2
#             total += inter_sum3
#         elif inter_sum2 <= 0:
#             total += inter_sum
#             exit()
#     elif inter_sum <= 0:
#         total += inter_sum2
#         exit()