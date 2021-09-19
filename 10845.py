from collections import deque
import sys
input = sys.stdin.readline

queue =deque([])

for _ in range(int(input())):
    command = list(input().split())
    if (com := command[0]) == 'push':
        queue.append(int(command[1]))
    elif com == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif com == 'size': print(len(queue))
    elif com == 'empty':
        if queue: print(0)
        else: print(1)
    elif com == 'front':
        if queue: print(queue[0])
        else: print(-1)
    else:
        if queue: print(queue[-1])
        else: print(-1)