from itertools import combinations as comb
import sys
input = sys.stdin.readline


def word_to_bit(word):
    bit_line = 0b0
    for i in word:
        bit_line |= 1 << (ord(i) - 97)

    for i in 'antic':
        if bit_line & 1 << (ord(i) - 97):
            bit_line -= 1 << (ord(i) - 97)

    return bit_line


n, k = map(int, input().split())

k -= 5
if k < 0: print(0)
else:
    words = []
    choice = set()
    for _ in range(n):
        line = input().strip()
        words.append(word_to_bit(line))
        for i in line:choice.add(i)
    choice -= {'a', 'n', 't', 'i', 'c'}

    ans = 0
    if k > len(choice): k = len(choice)
    for i in comb(choice, k):
        make_word = word_to_bit(i)
        tmp = 0
        for j in words:
            if make_word & j == j: tmp += 1
        ans = max(ans, tmp)

    print(ans)
