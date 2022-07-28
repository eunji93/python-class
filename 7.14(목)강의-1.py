# 12-3) ==연산을 대상으로 관찰하는 딕셔너리의 성격
# 리스트의 '=='연산 (동등비교 연산자)
t1 = [1, 2, 3]
t2 = [1, 2, 3]
t3 = [3, 2, 1]
t1==t2            # True - 리스트는 저장하는 순서, 자료등 모든게 다같아야 됨
t1==t3            # False 
# 딕셔너리의 '=='연산
d1 = {1: 'a', 2: 'b'}
d2 = {1: 'a', 2: 'b'}
d3 = {2: 'b', 1: 'a'}
d1==d2           # True  
d1==d3           # True - 딕셔너리는 저장하는 순서가 중요하지 않기에 같다!/ 데이터만 같으면 됨

# 12-4) in/ not in 연산
# if in -> true 수정
if '새우깡' in dc2:          # 있으면 true -> 수정/ 없으면 false -> 수정x (if문 탈출)
    dc2['새우깡'] = 950      # 수정 - 새우깡에대한 정보가 있다면 새우깡이란 정보를 950으로 변경하고 싶다./ 단, 없으면 말고
# if not in -> true 수정
if '카페라떼' not in dc1:    # 없으면 true -> 추가 / 있으면 false -> 탈출x 
    dc1['카페라떼'] = 1200   # 추가 - 카페라떼에 대한 정보가 없다면 '카페라떼 1200원' 정보를 추가 하고 싶어

# 12-5) 딕셔너리와 for루프
dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
for i in dc:             # key 값만 배출
    print(i, end = '')   # 새우깡 콘치즈 꼬깔콘 / 콘치즈 꼬깔콘 새우깡 이여도 이상무 - 순서유지 놉
    
dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}
for i in dc:
    dc[i] += 70         # 인덱싱 연산을 통한 데이터 일괄적 수정
dc                      # {'새우깡': 770, '콘치즈': 920, '꼬깔콘': 820}

# 13강 클래스와 객체

# 13-1) 전역변수와 지역변수
# 함수 안에 선언된 변수 - 지역변수(함수지역에서 벗어나면 지역변수는 소멸된다./지역변수 = 임시변수)
def func(n):        # 매계변수 : n
    lv = n + 1      # 지역변수 func함수를 벗어나면 lv는 소멸 
    print(lv)       # 지역변수 : lv
func(12)            # 13 

# 함수 밖에 선언된 변수 - 전역변수(소멸되지않고 계속 존재하는 변수)
cnt = 100           # 전역변수 : cnt
cnt += 1
def func():
    print(cnt)
func()              # 101

# 지역변수/전역변수 같이 선언
cnt = 100        # 변수의 선언 / '전역변수'
def func():
    cnt = 0      # 이게 없었다면 func() = 100 이됨 / '지역변수'
    print(cnt)
func()           # 0
print(cnt)       # 100/ cnt=0은 지역변수라서 func함수가 끝나면 소멸되기에 cnt = 100이된다./ print 참조
# cnt = 100 과 cnt = 0 은 파이썬이 받아들일때 다름/ 함수안에 cnt=0(지역변수)가 들어왔기에 
# 휴먼센스 : 사람이 바라볼땐 당연한거지만 파이썬이 받아들일땐 다른거

cnt = 100        # 변수의 선언 / '전역변수'
def func():
    global cnt   # global 선언이 있으면 '전역변수' cnt 값이 바뀐다.
    cnt = 0      # cnt = 100이 0으로 바뀜 (global 때문에)
    print(cnt)
func()           # 0
print(cnt)       # 0

# 13-2) 객체지향 프로그래밍 (object oriented programming)
# 객체 : 기능(함수) / 데이타 
# 다른 언어랑 조금 다르게 객체지향언어로 써야지만 파이썬 코드를 사용할수 있는건 아님! 

# 13-3) 객체 이전의 프로그램에 대한 반성
fa = 20
def up_fa():                       # 이 함수를 호출하면 아빠 나이 올라감
    global fa
    fa += 1
def get_fa():                      # 이 함수 호출하면 아빠 나이 반환함
    return fa
def main():
    print("2022년")
    print("아빠:", get_fa())
    print("2023년")
    up_fa()                         # 아빠 나이 1살증가
    print("아빠:", get_fa())

main()                              # 2022년/아빠:20, 2023년/아빠:21

# 13-3-2)
fa = 20
def up_fa():                       # 이 함수를 호출하면 아빠 나이 올라감
    global fa
    fa += 1
def get_fa():                      # 이 함수 호출하면 아빠 나이 반환함
    return fa

mo = 20                            # 엄마꺼도
def up_mo():                       
    global mo
    fa += 1
def get_mo():                      
    return mo

def main():
main()

# 13-4) 클래스와 객체의 이해
# 자동차 설계도 - 클래스 (호출불가/틀자체로만 사용불가)
# 설계도 기반으로 만들어진 실제 자동차 - 객체 (객체로 뭘 만들수 있는거!)
# class_ object.py
class ageinfo:                    # 클래스 ageinfo의 정의 
    def up_age(self):             # 클래스안에 담김 up_age 함수 / up_age - 인스턴스 메소드
        self.age += 1
    def get_age(self):            # 클래스안에 담김 get_age 함수/ age - 인스턴스 변수, get_age - 인스턴스 메소드
        return self.age           # 인스턴스 변수는 파이썬이 정해주니, 인스턴스 메소드를 잘짜주면 된다
def main():
    fa = ageinfo()                 # ageinfo 객체생성
    fa.age = 20                    # fa에 저장된 객체의 변수 age에 20을 저장
    print("현재아빠나이")
    print("아빠:", fa.get_age())     # get_age 호출할때 self에 값 전달하지 않음
    print("1년뒤")
    fa.up_age()                      # up_age 호출할때 self에 값 전달하지 않음
    print("아빠:", fa.get_age())     # get_age 호출할때 self에 값 전달하지 않음 
main()

# 인스턴스 / 객체 표현은 거진 동일!
# 인스턴스 변수 - 인스턴스(객체) 안에 존재하는 변수
# 인스턴스 메소드 - 인스턴스(객체) 안에 존재하는 메소드(함수)

# 13-5) 이전 예제의 수정결과
# family_age3.py (사진찍어둠)
class ageinfo:                     
    def up_age(self):            
        self.age += 1
    def get_age(self):            
        return self.age           # 변수 age/ self는 없이 봐도 된다.
def main():
    fa = ageinfo()  # 아빠 나이 객체 생성
    mo = ageinfo()  # 엄마 나이 객체 생성
    me = ageinfo()  # 나의 나이 객체 생성 / ageinfo()에 세개의 객체함수가 있다.
    fa.age = 20     # 아빠 현재 나이
    mo.age = 20     # 엄마 현재 나이
    me.age = 9      # 나의 현재 나이 / me에 존재하고있는 객체에 
    sum = fa.get_age() + mo.get_age() + me.get_age()  # 각각 get_age메소드를 호출
    print("가족나이합:", sum)   # 49
    fa.up_age()     # 아빠 나이 한살 올림 / up_age() 함수 호출
    mo.up_age()   
    me.up_age()
    sum = fa.get_age() + mo.get_age() + me.get_age()
    print("1년 후의 합:", sum)  
    
# 13-6) self
# family_age3.py - 클래스(설계도) 
class ageinfo:                     
    def up_age(self):            # 매계변수: self 
        self.age += 1
    def get_age(self):            
        return self.age 
# self 매계변수에 따로 값을 전달하지 않기에 눈에는 있지만 하는일이 없는거 같아서 지우고 봐도된다.
# 클래스 안에 메소드를 넣을때 첫번째 매계변수는 self로 넣어라 라고 파이썬의 요구사항
# 함수 안에 변수가 들어가게되면 (파이썬이 넣어주면) self.변수로 넣어달라고 파이썬의 요구사항 
# family age의 객체 age는 다 다르다 (fa/mo/me의 객체 age는 다 다른것)
# 설계도는 같아도 그안에 들어간 의미는 (함수/객체/)는 다르다. 
# 함수가 하는 일은 같다 (up_age들의 의미는 객체 마다 하는 일이 같다/ get_age)
# self에 객체가 저장되었다고 무방하다.
# 변수의 진실은 이름표떼기~ (이름표변경이든,,삭제든...뭐든)

# self test.py
class ageinfo:                     
    def up_age(self):            # 매계변수: self 
        self.age += 1
    def get_age(self):            
        return self.age 
def main():
    fa = ageinfo()
    fa.age = 20
    fa.up_age()  # 이렇게 작성해야함
    ageinfo.up_age(fa) # 제시된사항
    print(fa.get_age()) # 이렇게 작성
    print(ageinfo.get_age(fa)) # 틀리진 않지만 이렇게 작성 ㄴㄴ
main()