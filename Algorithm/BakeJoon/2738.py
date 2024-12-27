import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

A = list()
B = list()
for _ in range(N):
  A.append(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(N):
  B.append(list(map(int, sys.stdin.readline().rstrip().split())))

for r in range(N):
  for c in range(M):
    print(f'{A[r][c] + B[r][c]}', end=' ')
  print()