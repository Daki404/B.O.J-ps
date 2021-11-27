import sys, math
input = sys.stdin.readline


def star_print(n):
    star = ['*', '* *', '*****']
    for i in star:
        print(i)
    for i in range(1, int(math.log(n // 3, 2)) + 1):
        tmp_star = []
        for j in range(len(star)):
            tmp_star.append(f'{star[j]}' + ' ' * len(star[-(j + 1)]) + f'{star[j]}')
        star += tmp_star
    return star


n = int(input())
star = star_print(n)


for i in range(n):
    print(' ' * (n - (i + 1)) + star[i] + ' ' * (n - (i + 1)))