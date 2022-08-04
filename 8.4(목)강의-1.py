h2022 = ["허지훈", ('남성','한국'),["잘생김", 20]]
import copy
h2023 = copy.deepcopy(h2022) 
h2023   # ['허지훈', ('남성','한국'),['잘생김', 20]]
h2023[2][1] += 1
h2023   # ['허지훈', ('남성', '한국'), ['잘생김', 21]]
(h2022[0] is h2023[0]) and (h2022[1] is h2023[1])    # true (얕은복사확인)
h2022[2] is h2023[2]  # false (깊은복사확인)

# 빈 리스트 r1을 만들고, 리스트 내용을 1~10까지 채워주세요. 
# 그다음에 리스트에 저장된 내용을 2배씩 증가시키는 내용이 들어있는 리스트를 r2 작성
# main 함수에 담아서 실행하는 형태
r1 = []
r1 = [x for x in range (1, 11)]
r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r2 = [x * 2 for x in r1]
print(r2)
def main():
    print(r2) 

# 이게 정답
def main():
    r1 = []
    r1 = [x for x in range (1, 11)]
    r2 = [x * 2 for x in r1]
    print(r1)
    print(r2)

# for range 사용    
r1 = []
for i in range (1, 11):
    r1.append(i)   

def main():
    r1= []
    r1 = [x for x in range (1, 11) ]
    r2 = [x for x in r1 if x % 2] 
    print(r1)
    print(r2)
    
r1= []
r1 = [x for x in range (1, 11) if x % 2]
    
# Iterable과 Iterator 객체
ds = [1, 2, 3, 4]
for i in ds:
    print(i)   # 리스트의 값들을 하나씩 빼서 출력하는 함수
iter()         # Iterator 객체를 얻어내는 함수
ir = iter(ds)  # iter함수를 통해 ds라는 리스트를 받아 값을 하나씩 꺼냄/ 
next(ir)  # 1
next(ir)  # 2
next(ir)  # 3
next(ir)  # 4
next(ir)  # 오류 / 오류를 없애려면 다시 함수를 정의해주면된다.

# Iterable 객체 : iter 함수에 인자로 전달이 가능한 객체
# Iterator 객체 : iter 함수가 생성해서 반환하는 객체 -> 리모컨
# Iterable 객체를 대상으로 iter 함수를 호출해서 Iterator 객체를 만든다.
# Iterator 객체를 생성할 수 있는 대상이 되는 것이 Iterable 객체이다
ds = [1, 2]
ir = iter(ds)  # ir = iter() : Iterator 객체/ ds : Iterable 객체 
next(ir) # 1   # ir : 객체에 포함된 함수/ next() : 버튼
next(ir) # 2

r = [1, 2, 3, 4, 5]
next(r)  #오류 (TypeError)

ds = [1, 2, 3]
ir = iter(ds)
next(ir) # 1
next(ir) # 2
next(ir) # 3 
# 파이썬이 실제 처리하는 코드!
ds = [1, 2, 3]
ir = ds.__iter__()
ir.__next__()  # 1
ir.__next__()  # 2
ir.__next__()  # 3
# 스페셜 메소드 : 파이썬 인터프리터에 의해서 호출되는 메소드 / ex) __next__(), __init__

st = "abcdefg"  # 문자열도 가능 (iterable 객체)
sr = iter(st)
next(sr)  # 'a'
next(sr)  # 'b'
next(sr)  # 'c' ....

tp = (1, 2, 3, 4, 5) # 튜플도 가능 (iterable 객체-리모컨을 만들수있는 객체)
tr = iter(tp)
next(tr) # 1
next(tr) # 2
next(tr) # 3 .....

r1 = [1, 2, 3]
dir(r1)  # 객체안에 존재하는 함수를 다보여달란 함수

for i in [1, 2, 3]:     #[] 리스트는 iterable객체 이다
    print(i, end ='')
    
ir = iter([1, 2, 3])    # 실제 for루프의 구조 / ds = [1, 2, 3]/ ir = ds.__iter__()
while True:
    try:
        i = next(ir)
        print(i, end=" ")
    except StopIteration:
        break
    
ir = iter([1, 2, 3])  # ir = Iterator / Iterator객체 는 Iterator다시 나감 /
for i in ir:
    print(i, end=" ")   # 1 2 3