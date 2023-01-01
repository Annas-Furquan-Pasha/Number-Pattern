# Number pyramid

height = int(input('Enter height : '))

for row in range(1, height+1):
    for i in range(1, row+1):
        print(i, end=' ')
    print()