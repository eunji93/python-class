# 11 '모듈의 이해' 그리고 '수학모듈' 이용하기
# 11-1) 모듈 - 만들어진 소스코드 (소스파일)
# circle.py - 모듈의 예 (소스파일을 만들어두고 다른거에 가져다 쓰겠다.)
PI = 3.14                   # 원주율 
def ar_circle(rad):         # 원의 넓이를 계산해서 반환 하는 함수
    return rad * rad * PI
def ci_circle(rad):         # 원의 둘레를 계산해서 반환 하는 함수
    return rad * 2 * PI     

# 11-2) 모듈 가져다 쓰는 방법
# circle-t1.py
import circle   # circle.py 모듈을 가져다 쓰겠다는 선언! (import= 가져다쓰겠다/가져다 두겠다 라는 선언)

def main():
    r = float(input("반지름 입력:"))
    ar = circle.ar_circle(r)   # circle.py의 ar_circle 함수 호출
    print("넓이:", ar)
    ci = circle.ci_circle(r)   # circle.py의 ci_circle 함수 호출
    print("둘레:", ci)
main()                         # 반지름 입력: 5.5 -> 넓이 : 94.985/ 둘레 : 34.54 

# circle_t2.py

from circle import ar_circle     # from circle import ar_circle, ci_circle 
from circle import ci_circle     # 출처가 같기때문에 합쳐서 작성도 가능

def main():
    r = float(input("반지름 입력:"))
    ar = ar_circle(r)         # circle.py의 ar.circle 함수 호출
    print("넓이:", ar)    
    ci = ci_circle(r)         # circle.py의 ci.circle 함수 호출
    print("둘레:", ci)
main()