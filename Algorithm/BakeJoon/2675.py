n = int(input())
for _ in range(n):
  r, s = input().split()
  r = int(r)
  str = ''
  for i in s:
    str += i * r
  print(str)
