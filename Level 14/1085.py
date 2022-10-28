import sys

x, y, w ,h = map(int, sys.stdin.readline().split())

x_w = max(x, w) - min(x, w)

y_h = max(y, h) - min(y, h)

print(min(x_w, y_h, x, y))