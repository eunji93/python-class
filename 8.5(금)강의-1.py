x = 3.0
type(x)         # <class 'float'> - float라는 틀을가지고 만들어진 객체 (객체 = data + function)
x.is_integer()  # True - 3.0이라는 기능이있다 = 객체이다

def func1(n):
    return n

def func2():
    print("adios")

type(func1)  # <class 'function'> -> 함수도 객체이다.
type(func2)  # <class 'function'>

func1(10)    #10
func2()      # adios

# 함수에선 인자를 객체로 받아야 한다. 그렇다면 함수도 객체라면 함수인자를 객체로 받을수 있을까?
def say1():
    print("Hola")

def say2():
    print("adios")  

def caller(fct):
    fct()

caller(say1)  # Hola
caller(say2)  # adios   -> 함수안에서 함수를 객체로 받아도 실행이 된다.

# 파이썬에선 함수도 객체로 본다 = 즉,파이썬에선 모든게 객체이다
# 함수도 변수랑 차이가 없다. (함수: 이름이 있는 파이썬코드를 담는 상자)
def fac_fac(n):
    def exp(x):         # 함수안에서 함수를 다시 정의
        return x ** n   # x 거듭제곱 n
    return exp

f1 = fac_fac(2)
f2 = fac_fac(3)
f1(4)  # 4의 거듭제곱은? -> 16 / + 실행되는게 함수라서 ()이걸 붙여줘야함
f2(4)  # 4의 세제곱은 ? -> 64

## 람다 (lambda) 
# 이름없는 함수 정의 하는 방법
def show(s):  # 전달받은 인자를 출력하는 함수의 정의
    print(s)

ref = show       # ref를 가지고 show 함수실행
ref("adios~")    # adios~

ref = lambda s: print(s)  # 람다기반 함수정의 / show라는 함수 이름을 없앨뿐더러, 코드를 단순하게/ 람다 함수의 매개변수는 s
ref("adios~")    # adios~

f1 = lambda n1, n2: n1 + n2  # 매개변수가 2개인 경우
f1(10, 8)  # 18

# 예1)
def ref1(s):
    return s
ref1("adios~")  # 'adios~'
# 예2)
ref = lambda s: s   # ref = lambda s: return s 와 같은 코드 (하지만 람다에선 return을 직접쓰면 오류가 남/ 이미 내포되어있음)
ref('adios~')   # 'adios~'  * 예1, 예2 같은 것

f2 = lambda s: len(s)  # 길이 값을 반환하는 람다 함수정의
f2("adios~")  # 6

f3 = lambda : print("adios~")  # 매개변수 사용안하는 경우~
f3()   # adios~

# 아래의 코드를 람다기반 함수정의로 변경
def fac_fac(n):
    def exp(x):         #이부분을 람다기반으로 변경해야 하는것
        return x ** n   
    return exp

f1 = fac_fac(2)
f2 = fac_fac(3)
print("4의 거듭제곱은?", f1(4))  # 16
print("4의 세제곱은?", f2(4))  # 64
print("--------구분선---------")

# 람다식기반 함수로 변경한 코드
def fac_fac(n):
    return lambda x: x**n
f1 = fac_fac(2)
f2 = fac_fac(3)
print("4의 거듭제곱은?", f1(4))  # 16
print("4의 세제곱은?", f2(4))  # 64
print("--------구분선---------")