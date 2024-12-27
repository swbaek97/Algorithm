#import time

#start_time = time.time()  # 측정 시작
################################################################
# 내가 푼 풀이
import sys
    
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  S = sys.stdin.readline().rstrip()
  print(f'{S[0]}{S[len(S)-1]}')

# 답지 풀이

################################################################
#end_time = time.time()  # 측정 종료
#print("time:", end_time - start_time)  # 수행 시간 출력
