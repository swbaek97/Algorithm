import sys
S = sys.stdin.readline().rstrip()
converted = ''

for i in S:
  if i.isupper():
    converted += i.lower()
  else:
    converted += i.upper()
print(converted)