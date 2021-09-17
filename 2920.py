import sys
input = sys.stdin.readline

line = list(map(int, input().split()))

if line[0] < line[1]:
    for i in range(2, 8):
        if line[i-1] > line[i]:
            print('mixed')
            break
    else: print('ascending')
else:
    for i in range(2, 8):
        if line[i - 1] < line[i]:
            print('mixed')
            break
    else:
        print('descending')