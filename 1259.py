import sys
input = sys.stdin.readline


def palindrome(num):
    arr = []
    while num:
        arr.append(num % 10)
        num //= 10
    for i in range(len(arr) // 2):
        if arr[i] != arr[-(i + 1)]:
            return 'no'
    return 'yes'


while True:
    n = int(input())
    if n == 0: break
    print(palindrome(n))