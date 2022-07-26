# 변수 s 가 "pc"(문자열 pc)를 참조 한다 -> 변수 s가 가르키는 것은 "pc"이다. (s="pc")
# 참조 = reference / reference count(r/c) 
# C python / J python/ iron python -> 인터프린터 (파이썬을 어떤 환경에 접근성있게 만들었냐~/해석기) 
# 수정이 가능한 객체 와 불가능한 객체 (파이썬은 모든게 객체)
# 수정이 가능한 객체(mutable) : 리스트 -> 값이 바껴도 id()의 값은 바뀌지않는다
# 수정이 불가능한 객체(immutable) : 튜플, 문자열 -> 값이 바뀌면 id()의 값은 바뀐다
# id(매개변수) -> 주소를 찾는 함수
# 리스트의 id()
r = [1, 2]
id(r)
1819606150912
r += [3, 4]
r
[1, 2, 3, 4]
id(r)
1819606150912  # 주소값 안바뀜
# 튜플의 id()
t=(1, 2)
id(t)
1819606150144
t += (3, 4)
t
(1, 2, 3, 4)
id(t)
1819606166448   # 주소값 바뀜
# 문자열은 수정이 불가능한 객체라 수정/삭제 불가능 하다. (변경이 아닌 새로운값을 생성 하느것 )
t1 = "신"
t2 = "주"
t3 = "아"
t = t1 + t2 + t3
t
'신주아'
t1 =t1 + t2 + t3
t1
'신주아'

def add_last(m, n):
    m += n

r = [1, 2]
add_last(r, [3, 4])
print(r)             # [1, 2, 3, 4]

def add_last(m, n):
    m += n

t = (1, 3)
add_last(t, (5, 7))
print(t)             # (1, 3)

# 변경안되는 기본 이뮤터블
def add_last1(m1, n1):
    m1 += n1

t1 = (1, 3)
add_last1(t1, (5, 7))
print(t1)               # (1, 3)
# 이뮤터블 안에 리턴함수가 필요하고 수식도 변경이 필요하다 (값을 추가하는 생성법)
def add_last2(m, n):
    m += n
    return m

t2 = (1, 3)
t2 = add_last2(t2, (5, 7))
print(t2)                    # (1, 3, 5, 7)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0], a[-1])                  # 1, 10

# 무작위 리스트 값을 정렬 하는 법
a = []
a.append(1)
a.append(10)
a.append(25)
a.append(7)
a.append(99)
a.append(8)
a.append(57)
a.append(33)
a.append(96)
a.append(2)                
print(a)                   # a = [1, 10, 25, 7, 99, 8, 57, 33, 96, 2]
a.sort()                   # 무작위 리스트를 순서대로 정렬 하는 함수
print(a)                   # a = [1, 2, 7, 8, 10, 25, 33, 57, 96, 99]

# 다음에 나와있는 리스트에서 가장큰 값과 가장 작은 값을 출력하는 함수를 정의 하세요
i = [3, 1, 5, 4, 7, 6]
def min_max(a):
    a. sort()                     # [1, 3, 4, 5, 6, 7]
    print(a[0], a[-1], sep = ',')
min_max(i)                        # 1 7
print(i)                          # [1, 3, 4, 5, 6, 7]

# 다음에 나와있는 리스트에서 가장큰 값과 가장 작은 값을 출력하는 함수를 정의 하세요
# 추가 단, 원본의 순서를 변경하지 않아야 합니다.
b = [3, 1, 5, 4, 7, 6]
def minMax(a):
    a = list(a)                 # 리스트화 시켜 a 에 저장 (복사를 해두는것)
    a.sort()                     
    print(a[0], a[-1], sep = ',')
minMax(b)                       # 1 7   
print(b)                        # [3, 1, 5, 4, 7, 6]

c = (3, 1, 5, 4, 7, 6)
minMax(c)                  # 1 7                  
print(c)                   # (3, 1, 5, 4, 7, 6)