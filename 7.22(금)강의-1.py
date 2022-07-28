# 14-4) 둘 이상의 예외를 처리하기
def main():
    bread = 10
    try:
        people = int(input("몇명?:"))
        print("1인당 빵의수:", bread/people)
        print("맛있게 드세요.")
    except ValueError:
        print("입력이 잘못되었습니다.")
    except ZeroDivisionError:
        print("0으로는 나눌 수 없습니다.")
        
main()                                     # 몇명? 0/ 0으로는 나눌수 없습니다.

# <책 참고 - 295p> 예외 예시
# BaseException       : 최상위 예외 클래스
# Exception           : 대부분 예외 클래스의 슈퍼 클래스
# ArithmeticError     : 산술 연산에 문제가 있다
# AttributeError      : 잘못된 속성을 참조 했다.
# EOFError            : 파일에서 더이상 읽어 들일 데이터가 없다
# ModuleNotFoundError : import 할 모듈이 없다
# FileNotFoundError   : 존재하지 않는 파일이다
# IndexError          : 잘못된 인덱스를 사용했다
# NameError           : 잘못된 이름을 사용했다
# SyntaxError         : 문법이 틀렸다
# TypeError           : 계산하려는 데이터의 유형이 잘못되었다
# ValueError          : 계산하려는 데이터의 값이 잘못되었다

# 14-5) 예외 메시지 출력하기와 finally
# 14-5-1)
def main():
    bread = 10
    try:
        people = int(input("몇명?"))
        print("1인당 빵의수:", bread/people)
        print("맛있게 드세요.")
    except ValueError as msg:  # 변수 msg에 오류 메시지가 담긴다. (변수는 다른거로 지정해도된다)
        print("입력이 잘못되었습니다.")
        print(msg)             # 오류 메시지 출력
    except ZeroDivisionError as msg:   # 변수 msg에 오류 메시지가 담긴다.
        print("0으로는 나눌 수 없습니다.")
        print(msg)             # 오류 메시지 출력            
main()                     # 결과 : 몇명? 0 / 0으로는 나눌 수 없습니다./ division by zero

# 14-5-2)
def main():
    bread = 10
    try:
        people = int(input("몇명?"))
        print("1인당 빵의수:", bread/people)
        print("맛있게 드세요.")    
    except ValueError:
        print("입력이 잘못되었습니다.")
    finally:                   # 예외가 발생하든 안하든 실행 100% 보장해주는 코드
        print("어쨌든 프로그램은 종료합니다.")
main()        # 몇명? 0 이라고 했을시 try print에 people의 수가 없기에 에러가 남

# 14-5-3)       
def main():
    bread = 10
    try:
        people = int(input("몇명?"))
        print("1인당 빵의수:", bread/people)
        print("맛있게 드세요.")
    except ValueError as msg:  # 변수 msg에 오류 메시지가 담긴다.
        print("입력이 잘못되었습니다.")
        print(msg)             # 오류 메시지 출력
    except ZeroDivisionError as msg:   # 변수 msg에 오류 메시지가 담긴다.
        print("0으로는 나눌 수 없습니다.")
        print(msg)
    finally:
        print("무조건 실행을 합니다")
main()                   # 몇명? 5/ 1인당빵의수:2.0/ 맛있게 드세요/ 무조건 실행을 합니다.

# 14-6) 모든 예외 그냥 무시하기  
def main():
    bread = 10
    try:
        people = int(input("몇명?"))
        print("1인당 빵의수:", bread/people)
        print("맛있게 드세요.")
    except:                        # 이렇게 하면 모든 예외가 다 걸려든다./ 모든 예외 무시
        print("뭔지는 몰라도 예외가 발생했군요")
main()                # 몇명? 글쎄요/ 뭔지는 몰라도 예외가 발생했군요

# 교재 352p) 주소록 만들기 