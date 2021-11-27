def solution(gems):
    gem_check = {i: False for i in set(gems)}
    gem_cnt = 0
    st, ed = 0, len(gems)

    if len(gem_check) == 1: return [1, 1]

    for i in range(len(gems)):
        if gem_check[gems[i]] == False:
            gem_check[gems[i]] = True
            gem_cnt += 1

        if gem_cnt == len(gem_check):
            pos = i
            gem_check = {i: False for i in set(gems)}
            gem_cnt = 0
            break

    for k in range(pos, -1, -1):
        if gem_check[gems[k]] == False:
            gem_check[gems[k]] = True
            gem_cnt += 1

        if gem_cnt == len(gem_check):
            st, ed = k, pos
            break

    j = ed
    while j < len(gems) and j < ed + ed - st:
        j += 1
        gem_check = {k: False for k in set(gems)}
        gem_cnt = 0

        for k in range(j, -1, -1):
            if gem_check[gems[k]] == False:
                gem_check[gems[k]] = True
                gem_cnt += 1

            if gem_cnt == len(gem_check):
                if j - k < ed - st: st, ed = k, j
                break
    return st + 1, ed + 1

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))