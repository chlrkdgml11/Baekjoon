import sys
import math

n, m = map(int, sys.stdin.readline().split())

def count_number(n, k):
    cnt = 0
    while(n):
        n = n // k
        cnt += n
    return cnt

count_two = count_number(n, 2) - count_number(m, 2) - count_number(n - m, 2)
count_five = count_number(n, 5) - count_number(m, 5) - count_number(n - m, 5)

print(min(count_five, count_two))