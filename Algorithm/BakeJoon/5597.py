num = set()
for _ in range(28):
  num.add(int(input()))
for i in range(1,31,1):
  if i not in num:
    print(i)