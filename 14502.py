from itertools import combinations
import sys
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]


def solve(lab, blank):
    ans = 0
    for walls in combinations(blank, 3):
        for wall in walls:
            lab[wall[0]][wall[1]] = 1
        addict = 0
        visit = [[False] * col for _ in range(row)]
        stack = []
        for i in virus:
            stack.append(i)
            visit[i[0]][i[1]] = True

        while stack:
            y, x = stack.pop()
            for i in range(4):
                v_x, v_y = x + dx[i], y + dy[i]
                if 0 <= v_x < col and 0 <= v_y < row and not visit[v_y][v_x] and not lab[v_y][v_x]:
                    visit[v_y][v_x] = True
                    addict += 1
                    stack.append((v_y, v_x))
        ans = max(ans, len(blank) - addict - 3)
        for wall in walls:
            lab[wall[0]][wall[1]] = 0
    return ans


row, col = map(int, input().split())
blank, virus, lab = [], [], []

for i in range(row):
    line = list(map(int, input().split()))
    for j in range(col):
        if line[j] == 0: blank.append((i, j))
        elif line[j] == 2: virus.append((i, j))
    lab.append(line)

print(solve(lab, blank))
