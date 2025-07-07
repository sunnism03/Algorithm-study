import sys

input = sys.stdin.readline

n = int(input())

scores = list(map(int, input().split()))
scores.sort()

max = scores[-1]

for i in range(n):
    scores[i] = scores[i] / max * 100

print(sum(scores)/n)