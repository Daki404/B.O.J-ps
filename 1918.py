import sys
input = sys.stdin.readline

n = input().strip()
prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
ans = ''

stack_operator = []
for i in n:
    if i == '(': stack_operator.append(i)
    elif 'A' <= i <= 'Z': ans += i
    elif i == ')':
        tmp = stack_operator.pop()
        while tmp != '(':
            ans += tmp
            if stack_operator:
                tmp = stack_operator.pop()
            else: break
    else:
        if stack_operator and prior[stack_operator[-1]] < prior[i]:
            stack_operator.append(i)
        elif stack_operator and prior[stack_operator[-1]] >= prior[i]:
            tmp = stack_operator.pop()
            while tmp != '(':
                ans += tmp
                if stack_operator and prior[stack_operator[-1]] >= prior[i]:
                    tmp = stack_operator.pop()
                else:
                    break
            stack_operator.append(i)
        else: stack_operator.append(i)

while stack_operator and stack_operator[-1] != '(':
    tmp = stack_operator.pop()
    ans += tmp
print(ans)

