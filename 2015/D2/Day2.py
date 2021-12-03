with open('input.txt') as text:
    file = text.read().splitlines()

real_sum = 0

for line in file:
    l,w,h = map(int, line.split('x'))
    sf_area1 = 2*l*w
    sf_area2 = 2*w*h
    sf_area3 = 2*h*l
    sf_sum = sf_area1 + sf_area2 +sf_area3
    
    surface_areas = [sf_area1, sf_area2, sf_area3]

    sf_sum2 = sf_sum + min(surface_areas)/2
    real_sum += sf_sum2

print(real_sum)