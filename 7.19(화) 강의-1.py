# 13-7) self 이외의 매개변수 갖는 함수
# family_age4.py
class ageinfo:                     
    def up_age(self):            # 매계변수: self 
        self.age += 1
    def get_age(self):            
        return self.age
    def set_age(self, age):      # age를 매계변수로 받겠다 / 직접정의한 age
        self.age = age           # 직접정의한 age/ 앞의 age는 필요 없! 

def main():
    fa = ageinfo()
    fa.set_age(20)
    fa.up_age()
    print("1년 후 아빠 나이:", fa.get_age())
main()

# 13-8) 생성자(초기화 메소드)
# ctor1.py
class const:
    def __init__(self):       #_ _init_ _ : 생성메소드(생성자) - 직접호출이 아닌 자동호출  /constructor:생성자/ initializer:생성자(초기화 함수)/ generator: 생성자
        print("new~")
def main():
    o1 = const()           # 생성자가 객체 하나 생성될때 마다 print실현
    o2 = const()
main()                # new~ new~

# self test.py - 참고
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

# ctor2.py
class const:
    def __init__(self):
        self.n1 = n1            # self.n1은 인스턴스 변수, n1은 매개변수
        self.n2 = n2            # self.n2은 인스턴스 변수, n2은 매개변수
    def show_data(self):
        print(self.n1, self.n2)
def main():
    o1 = const(1, 2)
    o2 = const(3, 4)
    o1.show_data()
    o2.show_data()
main()                 

# 13-9) 파이썬의 모든 값은 객체
n = 1000
n.bit_length()     # 10/ 변수 n에 담긴 정수도 객체라는 증거, n이라는 함수가 존재하는 객체의 bit_length의 값을 구하여라(라고 읽는다.)

f = 3.14
f.is_integer()     # false/ 변수 f에 담긴 실수도 객체라는 증거