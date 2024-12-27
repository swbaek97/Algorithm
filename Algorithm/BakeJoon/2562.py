L = list()
for _ in range(9):
  n = int(input())
  L.append(n)

max = max(L)
print(max)
for i in range(len(L)):
  if L[i] == max:
    print(i + 1)
