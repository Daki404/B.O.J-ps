import sys

input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    arr = input().split()
    if arr[0] == 'add':
        s.add(int(arr[1]))
    elif arr[0] == 'remove':
        if int(arr[1]) in s:
            s.remove(int(arr[1]))
    elif arr[0] == 'check':
        if int(arr[1]) in s:
            print(1)
        else:
            print(0)
    elif arr[0] == 'toggle':
        if int(arr[1]) in s:
            s.remove(int(arr[1]))
        else:
            s.add(int(arr[1]))
    elif arr[0] == 'all':
        s = set(range(1, 21))
    else:
        s = set()
