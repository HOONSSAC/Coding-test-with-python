# num1, num2을 공백을 기준으로 구분하여 깁력 받기
num1, num2 = map(int, input().split())

result = 0

while True:
    # num1이 num2로 나누어 떨어지는 수가 될 때까지 빼기
    target = (num1 // num2) * num2
    result = result + (num1 - target)
    num1 = target
    
    # num1이 num2보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if num1 < num2:
        break
    
    # num2로 나누기
    result += 1
    num1 //= num2

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (num1 - 1)
print(result)