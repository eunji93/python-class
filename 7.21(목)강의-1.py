# 클래스 / 객체
# 클래스 : 테이타와 기능(메소드)를 기반으로 만들어진 일종의 틀
# 객체 : 클래스라는 틀을 기반으로 만들어 낸 메모리에 존재하는 실제 대상
# 파이썬에선 클래스도 객체로 바라본다
# 객체 생성시 '데이타'와 '기능'이 함께 채워져서 만들어진다.
# 그러나 사실은 객체 속 데이타는 나중에 채워진다
# 모든 변수는 초기화 해줘야 한다 - 값이 들어가야함
# 해당변수에 값이 넣어주는 시점 == 파이썬이 객체에 변수를 넣어주는 시점
# 파이썬의 객체 속에 변수가 생성되는 시점은 첫 대입연산을 진행하는 시점이다. (강의 다시보기)

# 14강) 예외처리
# 14-1) 예외가 발생하는 상황 1)처리가능/2)처리불가능(에러)
st=[1, 2, 3]
st[3]                                         # 인덱스 3번이 없!! 
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    st[3]
IndexError: list index out of range           # 에러가 난 이유에 대한 설명/ 처리가불가능한 코드를 수정해야하는 상황 

st[int(input("0~2 number gogo"))]       # 예외처리가 가능한 예시

3 + "coffe"
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    3 + "coffe"
TypeError: unsupported operand type(s) for +: 'int' and 'str'  # 처리가 불가능한/ 코드의 수정이 필요(에러)

3/0
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    3/0
ZeroDivisionError: division by zero          # 처리가 가능/불가능 상황에 따라 다름

       
# 14-2) 예외의 처리
def main():
    print("안녕하세요")
    age = int(input("나이를 입력하세요:"))
    print("입력하신 나이는 다음과 같습니다.:", age)
    print("만나서 반가웠습니다.")
    
main()
안녕하세요
나이를 입력하세요:스물
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    main()
  File "<pyshell#20>", line 3, in main
    age = int(input("나이를 입력하세요:"))
ValueError: invalid literal for int() with base 10: '스물'  # 숫자를 입력해야하는데 문자를 입력해서 오류

def main():
    print("안녕하세요")
    try:                                          #try 영역에서는 ValuEerror가 발생하면 except영역에서 처리한다/ 따라서 같이 써야한다
        age = int(input("나이를 입력하세요:"))
        print("입력하신 나이는 다음과 같습니다.:", age) # 오류가 일어났을때 문제가 생길수 있는 코드도 같이 묶어줘야 좋은코드이다.
    except ValueError:                            # except 오류이름: -> 즉, 어떤 오류가 일어나는지는 알아야한다.
        print("입력이 잘못되었습니다.")             # 예외가 발생하지않는다면 except영역 가지않고 아래코드로 내려간다.
        
    print("만나서 반가웠습니다")
    
main()
# 위의 예제기본형인데 아까전에 나이'스물'이라 썻을시 오류가 났었다.
def main():
    print("안녕하세요")
    age = int(input("나이를 입력하세요:"))
    print("입력하신 나이는 다음과 같습니다.:", age)
    print("만나서 반가웠습니다")
main()

# 14-3) 보다 적극적인 예외의 처리 (아래 예시는 매우 좋은 예제!)
def main():
    print("안녕하세요")
    while True:
        try:
            age = int(input("나이를 입력하세요:"))
            print("입력하신 나이는 다음과 같습니다:", age)
            break                       # 입력이 정상적이면 while 루프 탈출!/ 입력에 문제가 있다면 except영역으로 가는것
        except ValueError:
            print("입력이 잘못되었습니다.")
    print("만나서 반가웠습니다")
    
main()
