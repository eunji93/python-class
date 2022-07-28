# 7강  True, False 그리고 if와 그형제들
# 7-1) True(참)과 False(거짓)을 의미하는 값 / 'True/False' 변수가 아니라 그냥 하나의 값(data)이라고 생각하면됨

3>10       # 3이 10보다 크니? -> False (거짓)
3<10       # 3이 10보다 작으니? -> True (참)

# num = true  # 'true/false'가 하나의 값이기 때문에 변수에 넣을수가 있다.

r = 3 < 10  # < 연산의 결과인 true가 변수 r에 저장된다.
r           # True

# type(true)  # <class 'bool'> -> "부울형"
# type(false) # <class 'bool'> -> 'boolean'을 줄여 'bool'이라고 한다.

# int(정수), float(실수), [](리스트), ""(문자열), 부울형 이 있다.

# 7-2) 소스파일에 main 함수 만들기
def main():                   # main 함수의 정의
    print("simple frame")
main()                        # main 함수의 호출을 명령함

# 7-3) if문 : (만약) 조건이 맞으면 실행을 해라/ 만약 오른쪽에 있는 값이 true(참) 라면 문장을 실행하자 라고 읽으면됨
if num > 0 :                       # if의 오른쪽은 조건이라함 (num>0)
    print("양의 정수입니다.")       # if 절/문/블록 이라고 부름

## if_positive.py : 맞을수도 아닐수도!
def main():                        # main 함수의 정의
    num = int(input("정수입력:"))
    if num >0:
        print("양의 정수 입니다.")
main()                              # 위의 main 함수를 실행하라!

num = 2                              # -> 정수 입력: 2, 양의 정수 입니다.
if num>0 : print("양의 정수입니다.")   # if에 속하는 문장이 하나인 경우 이렇게 쭉이어서 사용할수있다.

# 7-4) if~else문 : 이쪽길! 아니면 저쪽길!
## if_else.py                                # if문만 있을경우 참이냐.거짓이냐 이건데, if-else는 둘중하나는 꼭실행된다.
def main():
    num = int(input("정수 입력:"))
    if num > 0:                              # if조건이 true이면 else 문장으로 안감
        print("0보다 큰 수 입니다.")
    else:                                    # if조건이 false이면 else문장이 실행된다.
        print("0보다 크지 않은 수입니다.")
main()
# 예시) 정수 입력: -7, if거짓->else넘어감, 0보다 크지 않은 수입니다.    

# 7-5) if-elif-else : 여러길 중에서 하나의 길만 선택! (조건이 여러가지일때!, 추가 elif가능~)
## if_elif_else.py
def main():
    num = int(input("정수 입력:"))
    if num > 0:                              # if조건이 true이면 else 문장으로 안감/ 참이면 바로 결론
        print("0보다 큰 수 입니다.")    
    elif num < 0:                            # 'else + if' -> elif/ 굳이 따지면 if와 비슷, 조건을 걸어주는
        print("0보다 작은 수 입니다.")         # if조건이 false 이면 elif문을 다시 확인/ 조건을 더추가 하고싶으면 elif를 더추가하면됨
    else:
        print("0으로 판단이 됩니다.")             
main()
# 정수입력: 0 -> 0 으로 판단이됩니다.

# 7-6) true 또는 false를 반환하는 연산들 (사진찍어둠)
# a >= z  a가 z보다 크거나 같으면 트루, 아니면 False
# a == z  a와 z가 같으면 참, 아니면 거짓 / (동등비교연산자! 완전히 같으면)
# a != z  a와 z가 같지않으면 참, 아니면 거짓 (다른언어에서는 !가 반전의 의미를 가지고 있다~)

## if_elif_else2.py : elif가 추가된 예시2
def main():
    num = int(input("정수 입력:"))
    if num == 1:
        print("1을 입력했습니다.")
    elif num ==2:
        print("2를 입력했습니다.")
    elif num == 3:
        print("3을 입력했습니다.")
    else:
        print("1, 2, 3 아닌 정수 입력했습니다.")
main()
# 정수입력:2 -> 2를 입력했습니다. (elif num ==2:)

# 논리 연산 (사진찍어둠) - and/ or/ not이란 연산자를 쓰는거 
# t and t : true / t and f : false
# t or f : true / f or f : false
# not f : true / not t : false      +) not 연산자의 오른쪽에 값이 와야한다.

## if_and_if.py
def main():
    num = int(input("2의 배수이면서 3의 배수인 수 입력: "))
    if num % 2 == 0:               # % 모듈러 연산 -> 나누기의 나머지값
        if num % 3 == 0:           # if_if 중첩 : if 안에 if를 또넣어~  else안에 if/else를 또 넣을수있다.
            print("ok!")           
        else:                      # 6배수 되는 조건문을 하나만 짜도 되지만 예시문으로 이렇게 나타내봄
            print("no!")           
    else:
        print("no!")
main()                             # 6 -> ok, 8-> no

# 위의 예제와 같은건데 and란 문장으로 이어서 한줄로 표시함 (and 연산자를 이용한 표현)
def main():
    num = int(input("2의 배수이면서 3의 배수인 수 입력: "))
if (num % 2) == 0 and (num % 3) ==0:                      # and 연산자에 왼/오른쪽이 true면 true! ex)6
    print("ok!")
else:
    print("no!")              
    
# 7-7) 리스트와 문자열을 대상으로도 ==, != 참/거짓 작동함

# 7-8) True 또는 False로 답하는 함수들
st1 = "123"
st2 = "one two three"
st1.isdigit()           # -> True() / st1에 저장된 객체의 함수를 호출/ isdigit = 숫자로만 이루어져있다
st2.isdigit()           # -> False()   
st1.isalpha()           # -> False()
st2.isalpha()           # -> True()

str = "Supersprit"
str.startswitch("super")    # 문자열 시작을 묻는
str.endswitch('int')        # 문자열 끝을 묻는

## is_phone_num_py
def main():
    pnum = input("스마트폰 번호 입력: ")
    if pnum.isdigit() and pnum.startswitch("010"):     # t and t : t/  t and f : f
        print("정상적인 입력입니다.")
    else:
        print("정상적이지 않은 입력입니다.")
main()               

# 7-9) in, notin
s= "tomato spaghetti"
if s.find("ghe") != -1:              # s.find() : ~을 찾는 함수
    print("있습니다.")
else:
    print("없습니다.")                # 있습니다.
    
if "ghe" in s:             #위의 s.find() = in/  오른쪽에 있는게 왼쪽에 있느냐? -> in 참.거짓
    print("있습니다.")
else:
    print("없습니다.")                # 있습니다.
    
# 3 in [1, 2, 3]   -> true/  in-> not in = false   
# 4 in [1, 2, 3]   -> false/  in-> not in = true     <in/noin 연산자>

# 7-10) 수를 참과 거짓으로 인식하는 방법
num = 1
if num :                              # if 옆엔 true/false가 와야함
    print("0아닙니다.")  # 0아닙니다.
# 파이썬은 0오는경우 false가 온것으로 간주, 0아닌수가 오는경우 true가온것으로 간주 / 0=false, 1=true

# 0 = false/ 1 = true의 예시로 아래 두조건은 같은것으로 봐도된다.
num = 1
if num != 0:
    print("num은 0이 아닙니다.")        # num은 0 아닙니다.
num = 1
if num:
    print("num은 0 아닙니다.")          # num은 0 아닙니다.

# bool 함수로 값을 호출해보면 true/false로 해석할수 있다. -> 직접실행해보기!!!
bool(5)               # true  : 0이 아니면 트루   
bool("what")          # true  
bool("")              # false : 문자열에 내용이없으면 거짓, 하나라도 있으면 참~
bool([1, 2, 3])       # true  : 문자열과 마찬가지로 내용이있으면 참~
bool([])              #false