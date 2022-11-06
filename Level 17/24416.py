from html.entities import codepoint2name
import sys

from matplotlib.colors import cnames

n = int(sys.stdin.readline())

def fibo1(n):
    global cnt1
    cnt1 += 1

    if(n == 1 or n == 2):
        cnt1 -= 1
        return 1

    else:
        return fibo1(n-1) + fibo1(n-2)

def fibo2(n):
    cnt2 = 0
    arr = [0, 1, 1]

    for i in range(3, n+1):
        arr.append(arr[i-1] + arr[i-2])
        cnt2 += 1

    return cnt2

cnt1 = 0
print(fibo1(n), fibo2(n))


