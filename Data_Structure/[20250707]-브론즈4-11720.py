import sys

input = sys.stdin.readline

n = int(input())
total = 0

num = list(input())

for i in range(n):
    total+=int(num[i])


print(total)