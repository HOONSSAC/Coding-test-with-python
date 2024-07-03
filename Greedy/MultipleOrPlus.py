# 나의 풀이
num = input()

num_list = [int(i) for i in num]

i = 0
result = 0

while i < len(num_list) - 1:
    result = max(num_list[i] + num_list[i+1], num_list[i] * num_list[i+1])
    num_list[i+1] = result
    i += 1

print(result)

# # 모범 답안
# data = input()

# print(len(data))
# print(data[4])

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
        
# print(result)