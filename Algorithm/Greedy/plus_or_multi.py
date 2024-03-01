import time

start_time = time.time()  # 측정 시작
################################################################
# 내가 푼 풀이
num = list(map(int, input()))
result = 0

for i in num:
  if i <= 1 or result == 0:
    result += i
  else:
    result *= i
print(result)

# 답지 풀이
# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#   # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수
#   num = int(data[i])
#   if num <= 1 or result <= 1:
#     result += num
#   else:
#     result *= num

# print(result)

################################################################
end_time = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력
