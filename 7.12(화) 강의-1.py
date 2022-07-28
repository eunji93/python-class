# 11-2) 모듈을 가져다 쓰는 방법 (7/5(화) 강의 이어서)
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

# 11-3) 모듈을 가져다 쓰는 방법2
# circle_s2.py

from circle import ci_circle as cc   # ci_circlefmf circle로부터 모듈을 쓸껀데 이때 cc로 바꿔서 읽을꺼야 -> 'as' 라는 코드로 인해
                                     # circle.py 파일중 def ci_circle(rad): <- cc로 이름바꾸자 (가져다 쓰는 순간만 바꿔서)
def ci_circle(rad):
    print("둘레:", rad * 2 * 3.14)

def main():
    r = float(input("반지름 입력:"))
    ci_circle(r)      # circle_s2.py 
    cc(r)             # circle.py
main()

# circle_t3.py

import circle as cc                 # ar에 가져다 쓸때 잠깜만 이름을 바꿔쓰는거!
def main():
    r = float(input("반지름 입력:"))
    ar = cc.ar_circle(r)            # 모듈의 이름을 바꿔쓴걸 이용해서 코드 작성
    
# 11-5) 수학관련 모듈
# 빌트인 함수 - import 선언 없이 그냥 언제든 호출 가능한 함수
print     # <bilt-in function print>   <- idle에서 print 쓰고 엔터치면 
input     # <bilt-in function input>

# 빌트인 모듈 - 위치 신경 쓰지 않고 언제는 import 할 수 있는 모듈
import math
math.fabs(-10)        # 10.0 (fabs= 절대값) /  추가 내용 사진 찍어둠

# 12. 딕셔너리(dictionary) - 자료형의 하나인데 단어의 의미와 비슷한 '사전'을 만들어 그내용을 참고해쓰는것
# key(데이터를 지칭할수 있는 값), value(데이터 값 자체) 개념을 통해 저장 -> [key : value]

# 12-1) 딕셔너리의 이해 -> {key : value}  
dc = {'코카콜라':900, '바나나맛우유': 750, '비타500': 600}
dc    # {'코카콜라':900, '바나나맛우유': 750, '비타500': 600}

# +) key에는 (거진) 무엇이든 올수있다, value에는 제한이 없다(실수든, 정수든, 튜플이든, 리스트이든)
#    ex) {'이름':'이순둥', '나이':20, '직업':'학생', '키':168.7 } 
# +) 딕셔너리에서 key의 정보는 중복이 불가능 하다. ex) 이름: 이순둥, 이름: 김순둥 <- 불가능 어떤 정보를 줘야 할지 모르니깐
# +) value의 값은 중복 가능!
# +) 저장순서가 필요하지 않다. key 순서가 중요하지 않다~ 그러니 순서가 중요한건 딕셔너리를 쓰면 안된다./(저장순서의 의미를 갖지않는다)/리스트나 튜플은 저장순서가 의미가 있다.

# 12-2) 참조, 수정, 추가, 삭제
# 1. 참조
dc = {'코카콜라':900, '바나나맛우유': 750, '비타500': 600}
v = dc['비타500']   # 인덱싱연산을 통해 인덱스 값과 (key값) value값을 참조
v                   # 600 (비타500의 value 값이 출력)

# 2. 수정 - value를 인덱싱 연산을 통해 수정 가능하다. / 가지고 있는 내용을 바꾸면 수정
dc = {'코카콜라':900, '바나나맛우유': 750, '비타500': 600}
dc['비타500'] = 650   # 키는 수정불가, value는 수정가능
dc                    # {'코카콜라':900, '바나나맛우유': 750, '비타500': 650}   

# 3. 추가 - 사전에 없는 내용을 넣으면
dc = {'코카콜라':900, '바나나맛우유': 750, '비타500': 600}
dc['삼다수'] = 650
dc                   # {'코카콜라':900, '바나나맛우유': 750, '비타500': 600, '삼다수':650}

# 4. 삭제
dc = {'코카콜라':900, '바나나맛우유': 750, '비타500': 600, '삼다수':650}
del dc['삼다수']      # del 사용해서 삭제
dc                   # {'코카콜라':900, '바나나맛우유': 750, '비타500': 650}