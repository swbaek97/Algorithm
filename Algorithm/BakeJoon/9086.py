import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  S = sys.stdin.readline().rstrip()
  print(f'{S[0]}{S[len(S)-1]}')