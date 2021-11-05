import sys
input = sys.stdin.readline

string = input().strip()
explo = list(input().strip())
stack = []

for i in string:
    stack.append(i)
    if len(stack) >= len(explo) and explo == (stack[-len(explo):]):
        del stack[-len(explo):]

if stack: print(''.join(stack))
else: print('FRULA')