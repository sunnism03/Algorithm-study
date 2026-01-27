#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())

no_hear = set()
no_see = set()

for i in range(n):
    no_hear.add(input())
for j in range(m):
    no_see.add(input())
    
no_hear_see = no_hear.intersection(no_see)
no_hear_see = list(no_hear_see)

print(len(no_hear_see))
no_hear_see.sort()
for i in range(len(no_hear_see)):
    print(no_hear_see[i])