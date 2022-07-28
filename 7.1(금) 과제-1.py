# 문제 1-3) "수"를 찾는 코드작성. 단, 빈칸에 들어갈 수는1부터 1씩 증가시키면서 찾아라
# 3 * a / 2 = 63
num = 0       # num의 값이 위 수식의 빈칸에 넣어 볼 값/ num에 저장된 값이 42

num = 0
r= 0
while r != 63:
    num += 1
    r = 3 * num / 2
print(num)

# 문제 2-1) 6과 45의 최소 공배수를 구하는 코드를 while루프 기반으로 작성해라
# 참고로 6으로도 나눠지고 45로도 나눠지는 값들 중에서 제일 작은값이 '최소공배수'이다.
# 따라서 45부터 시작해서 값을 1씩 증가 시켜가면서 6과45로 나누어 떨어지는 첫번째 값을 찾으면 된다.
lcm = 0   # 90이 출력되어야 정답

lcm = 0
n = 45
while True:
    if n % 6==0 and n % 45==0:
        lcm = n
        break
    n += 1
print(lcm)        # 90

# 문제 2-2) 42와 120의 최대공약수를 구하는 코드를 while루프 기반으로 작성해라
# 참고로 42로도 나눌수있고 120도 나눌수 있는 값들 중에서 제일 큰 값이 '최대 공약수'이다
# 따라서 42부터 시작해서 값을 1씩 감소시켜가면서 42와 120을 나눌 수 있는 값을 찾으면 된다.
gcm = 0  # 6이 출력되어야 정답

gcm = 0
n = 42
while True:
    if 42 % n ==0 and 120 % n ==0:
        gcm = n
        break
    n -= 1
gcm                 # 6

# 문제 3-1) 다음은 구구단중에서 7단을 출력하는 예제이다.
for i in range(1, 10):
    print(7*i, end='')           # 7 14 21 28 35 42 49 56 63
# 위의 예제에 continue관련 코드를 넣어서 결과가 짝수인 경우에만 출력되도록 해라 
for i in range(1, 10):
    if i % 2 == 1:
        continue
    print(7*i, end='')           # 14 28 42 56
    
 # 문제 3-1 맞는답!   
for i in range(1, 10):
    if (7*i) % 2:                # 0 -> false(출력), 홀수 continue  
        continue
    print ( 7*i, end='')         

# 문제 3-2) 2이상 100미만의 정수 중에서 2로도 나누어지지않고, 동시에 3으로도 나누어지지않는 수를 찾아서 
# 출력하는 코드를 while 루프 기반으로 작성해보자

n = 1
while n < 100:
    n += 1
    if n % 2 ==0 or n % 3 ==0:     # true일땐 생략(continue), false 출력
        continue
    print(n, end='')
    
# 문제 3-3) 문제 3-2)결과에서 continue를 사용하지 않았다면 이번에는 continue를 사용하는 방식으로 코드수정

n = 1
while n < 100:
    n += 1
    if n % 2 !=0 and n % 3 !=0:
        print(n, end='')

# 문제 4-1) 이중 for루프를 기반으로 구구단을 2단부터 9단까지 전부 출력하는 코드를 만들어보자.
for i in range(2, 10):             # 단
    for j in range(1, 10):         
        print(i*j, end='')
    print('wn', end='')         