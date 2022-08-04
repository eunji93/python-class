# a1 == a2  변수 a1과 변수 a2가 참조하는 객체의 내용이 같냐? (내용물만 같으면 됨)
# a1 is a2  변수 a1과 변수 a2가 참조하는 객체는 동일한 객체냐? (동일한 대상이냐?)

# 문자열 
v1 = "abc"
v2 = "abc"
v1 == v2   # true
v1 is v2   # true

# 리스트 ex1)
v1 = [1, 2, 3]
v2 = [3, 2, 1]
v1 == v2       # false -> 리스트는 순서가 중요하기 때문에
v1 is v2       # false -> 참조값이 다름 id(r1) / id(r2) 주소값이 다름

# 리스트 ex2)
r1 = [1, 2, 3]
r2 = [1, 2, 3]
r1 == r2       # true
r1 is r2       # false -> 참조값이 다름 id(r1) / id(r2) 주소값이 다름

# 문자열은 참조만 가능/ 변경불가능 (immutable) <-> list 변경가능 (mutable)
# immutable 변경이 불가능하기때문에(원본변경불가) 객체가 여럿이 참조해도 문제가 되지않는다 (새로만들기때문에)
# mutable 은 변경이 가능(원본변경가능) 

r1 = ["ji hun", ('man', 'kr'), [180, 20]]
r2 = list(r1)    # r1의 내용으로 새로운 리스트를 만들었다./ 얕은복사 
r1 is r2   # false / r1과 r2는 동일한 객체인가?/ 변경이 가능하기때문에 false!
r1 == r2   # true
r1[0] is r2[0] # true
r1[1] is r2[1] # true
r1[2] is r2[2] # true

# 얕은복사 : 내용이 변경불가능 원본같음(튜플, 문자열) 
# 깊은복사 : 내용변경가능 원본이 달라짐(리스트)

# 깊은복사를 하는 방법 
h2022 = ["ji hun",('man', 'kr'), [180, 20]] #2022년도 지훈의 정보
h2023 = list(h2022) # 필요에 의해서 지훈의 정보를 하나 복사함
h2023[2][1] += 1
h2023[2][0] += 5
h2022 # ['ji hun', ('man', 'kr'), [185, 21]]
h2023 # ['ji hun', ('man', 'kr'), [185, 21]]
import copy
h2022 = ["ji hun",('man', 'kr'), [180, 20]]
h2023 = copy.deepcopy(h2022)  # 깊은복사
h2023[2][1] += 1
h2022  # ["ji hun",('man', 'kr'), [180, 20]]
h2023  # ["ji hun",('man', 'kr'), [180, 21]]
(h2022[0] is h2023[0]) and (h2022[1] is h2023[1]) # 얕은복사. 같은 객체를 참조하니? -> true
h2022[2] is h2023[2] # false

# 얕은복사의 대상 (튜플, 문자열) / 깊은복사의 대상(리스트)
d1 = (1, 2, 3)
d2 = "python"
c1 = tuple(d1) # d1을 기반으로 튜플을 생성, 사실상 튜플 복사
c2 = str(d2)   # d2를 기반으로 문자열 생성, 사실상 문자열 복사
d1 is c1 # d1과 c1이 같은 객체를 참조하냐? -> true
d2 is c2 # d2외 c2가 같은 객체를 참조하냐? -> true

# 리스트 생성하는 방법
a1 = [1, 2, 3, 4, 5, 6]      # 통상적 리스트 생성방법
a2 = []                      # 통상적인 빈리스트 생성방법
a3 = [1, 2, [3, 4], [5, 6]]  # 통상적인 리스트 안에 리스트를 만드는 방법/ # 리스트 다른언어에선 배열이라고도 한다.
a4 = list("python")
a5 = list((1,2,3,4,5,6))     # [1, 2, 3, 4, 5, 6] 
a6 = list(range(1,7))        # [1, 2, 3, 4, 5, 6] 

# r1의 값을 2배씩 늘리는 방법 1)
r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1:         
    r2.append(i*2)
r2                   # [2, 4, 6, 8, 10] 
# r1의 값을 2배씩 늘리는 방법 2)
r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1]  # 리스트 컨프리헨션의 기본 구성 / for문 먼저 한뒤 그값을 대입하여 *2
r2  # [2, 4, 6, 8, 10]

# [1, 2, 3, 4, 5]의 리스트 객체를 임의의 변수에 저장해두고 그리스트 값을 10씩 증가시킨 다른 리스트를 생성해봅시다
# 리스트 컨프리 헨션을 이용해서
a1 = [1, 2, 3, 4, 5]
a2 = [x + 10 for x in a1]
a2                         # [11, 12, 13, 14, 15]

# r1에서 홀수만 뽑안낸 값을 r2에 리스트화 하는 방법1
r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r2 = []
for i in r1 :
    if i % 2:          # if i % 2 == 0 이랑 같은수식 (0은 파이썬이 false로 본다)
        r2.append(i)   # 짝수는 건너띄고 홀수만 인식한다.
r2   # [1, 3, 5, 7, 9]

# r1에서 홀수만 뽑안낸 값을 r2에 리스트화 하는 방법2 - 리스트 컨프리 헨션을 이용
r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r2 = [x for x in r1 if x % 2]
r2   # [1, 3, 5, 7, 9]
        
s1 = ['red', 'blue']
s2 = ['green', 'yellow', 'pink']
s3 = []
for i in s1:
    for j in s2:
        s3.append(i+j)       
s3         # ['redgreen', 'redyellow', 'redpink', 'bluegreen', 'blueyellow', 'bluepink']

s1 = ['red', 'blue']
s2 = ['green', 'yellow', 'pink']
s3 = [i+j for i in s1 for j in s2]
s3         # ['redgreen', 'redyellow', 'redpink', 'bluegreen', 'blueyellow', 'bluepink']

gugu = [i * j for i in range(2, 10) for j in range(1, 10)]
gugugu = [i * j for i in range(2, 10) for j in range(1, 10) if  (i*j) % 2] #홀수값만
        