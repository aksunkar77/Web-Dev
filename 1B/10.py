thickness = int(input())
c = 'H'
for i in range(thickness):
    print((c*(2*i+1)).center(2*thickness-1))


for i in range(thickness+1):
    print((c*thickness).ljust(thickness*2) + (c*thickness).rjust(thickness*2))


for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).ljust(thickness*2) + (c*thickness).rjust(thickness*2))


for i in range(thickness):
    print((c*(2*(thickness-i)-1)).center(2*thickness-1))