#import time

#start_time = time.time()  # 측정 시작
################################################################
# 내가 푼 풀이
A, B = map(int, input().split())

if A > B:
  print('>')
elif A < B:
  print('<')
else:
  print('==')

# 답지 풀이

################################################################
#end_time = time.time()  # 측정 종료
#print("time:", end_time - start_time)  # 수행 시간 출력
