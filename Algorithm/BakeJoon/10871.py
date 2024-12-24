N, X = map(int, input().split())
A = list(map(int, input().split()))

L = [a for a in A if a < X]
for x in L:
  print(x, end=' ')
