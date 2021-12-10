def checker(word, change_words):
    possible = []
    for change in change_words:
        cnt = 0
        for i, j in zip(word, change):
            if i != j: cnt += 1
            if cnt > 1: break
        else:
            possible.append(change)
    return possible


def solution(begin, target, words):
    visit = {i: False for i in words}
    ans = len(words) + 1

    def sol(n, cnt):
        nonlocal ans
        if n == target:
            ans = min(ans, cnt)
            return

        for i in checker(n, words):
            if visit[i]: continue
            visit[i] = True
            cnt += 1
            sol(i, cnt)
            visit[i] = False
            cnt -= 1

    sol(begin, 0)
    if ans > len(words): return 0
    return ans


solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])