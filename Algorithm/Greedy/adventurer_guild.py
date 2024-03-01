import time

start_time = time.time()  # 측정 시작
################################################################
# 내가 푼 풀이
# 실패: (시간내에 풀이 실패) 접근 자체를 반대로 했음. 큰쪽부터 채울게 아니라 작은쪽부터 그룹을 지어 나가야 최대로 그룹을 만들 수 있음.
# 반대로 하다보니 공포도와 그룹수 체킹하는게 복잡해져서 꼬였음.
# n = int(input())
# adventurer = list(map(int, input().split()))
# adventurer.sort(reverse=True)

# group = 0
# fear = adventurer[0]
# count = 0
# num = len(adventurer)

# for i in range(len(adventurer)):
#   count += 1
#   if fear == count:
#     count = 0
#     fear = adventurer[i + 1]

# print(adventurer)

# 답지 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의
count = 0  # 현재 그룹에 포함된 모험가의

for i in data:  # 공포도를 낮은 것부터 하나 확인하며
  count += 1  # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
    result += 1  # 총 그룹의 수 증가시키기
    count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력
################################################################
end_time = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력
