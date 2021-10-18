from collections import defaultdict
import sys
input = sys.stdin.readline


# n번 사람이 영향을 미치는 사람 탐색
def dfs_connect(n):  #
    visit = [False] * (len(person) + 1)
    visit[n] = True
    stack = [n]

    while stack:
        v = stack.pop()
        for i in connect[v]:
            if visit[i]: continue
            stack.append(i)
            visit[i] = True
            person[i] = True


n, m = map(int, input().split())

person = {i: None for i in range(1, n + 1)}  # 사람들은 무지 상태 : None
know = list(map(int, input().split()))

for i in know[1:]:  # 진실을 아는 상태 : True
    person[i] = True

connect = defaultdict(list)  # 파티 연결점
party = []

for _ in range(m):  # 양방향 그래프로, 파티 연결점 생성
    invite = list(map(int, input().split()))[1:]
    party.append(invite)
    for i in range(len(invite)):
        for j in range(len(invite)):
            if i == j: continue
            connect[invite[i]].append(invite[j])

for i, j in person.items():  # 초기 상태가 '진실' 이면 파티 접촉자들 상태를 '진실' 로
    if not j: continue
    dfs_connect(i)

ans = 0
for i in party:  # 해당 파티에, '진실' 상태가 없으면 count
    for j in i:
        if person[j]: break
    else: ans += 1
print(ans)