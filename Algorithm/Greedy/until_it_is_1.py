# 내가 푼 풀이
import time

start_time = time.time()  # 측정 시작

n, k = map(int, input().split())

count = 0

while n != 1:
  if n % k == 0:
    n /= k
  else:
    n -= 1
  count += 1
print(count)

# 답지 풀이
# n, k = map(int, input().split())

# result = 0

# while True:
#   # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#   target = (n // k) * k
#   result += (n - target)
#   n = target

#   # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#   if n < k:
#     break

#   # K로 나누기
#   result += 1
#   n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)

end_time = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력
