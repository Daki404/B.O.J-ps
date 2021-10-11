from collections import deque
import sys
input = sys.stdin.readline

ladder, snake = {}, {}
n, m = map(int, input().split())

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b


def bfs_game():
    visit = [True] + [False] * 100
    board = [0] * 101
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for move in range(1, 7):
            new_move = now + move
            if 0 < new_move <= 100 and not visit[new_move]:
                if new_move in ladder: new_move = ladder[new_move]
                if new_move in snake: new_move = snake[new_move]
                if not visit[new_move]:
                    queue.append(new_move)
                    visit[new_move] = True
                    board[new_move] = board[now] + 1
    return board[100]


print(bfs_game())

