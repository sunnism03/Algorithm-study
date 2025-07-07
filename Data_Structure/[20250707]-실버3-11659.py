import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))
sum_list = [0]

for i in range(len(num)):
    sum_list.append(sum_list[i]+num[i])

for j in range(m):
    a, b = map(int, input().split())
    print(sum_list[b] - sum_list[a-1])