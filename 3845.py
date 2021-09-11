import sys

input = sys.stdin.readline


def sol(w, x_cut, y_cut):
    x, y = 100, 75
    if x_cut[0] > w / 2 or y_cut[0] > w / 2 or x_cut[-1] < y - (w/2) or y_cut[-1] < x - (w/2):
        return 'NO'

    for i in range(1, len(x_cut)):
        if x_cut[i] - x_cut[i - 1] > w:
            return 'NO'

    for i in range(1, len(y_cut)):
        if y_cut[i] - y_cut[i - 1] > w:
            return 'NO'
    return 'YES'


while True:
    x, y, w = map(float, input().split())
    if x == 0: break
    x_cut = sorted(list(map(float, input().split())))
    y_cut = sorted(list(map(float, input().split())))

    print(sol(w, x_cut, y_cut))