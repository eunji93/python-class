# circle_s2.py
from circle import ar_circle
from circle import ci_circle as cc

def ci_circle(rad):
    return rad

def main():
    r = float(input("반지름 입력:"))
    ar = ar_circle(r)         # circle.py의 ar.circle 함수 호출
    print("넓이:", ar)    
    ci = cc(r)         # circle.py의 ci.circle 함수 호출
    print("둘레:", ci)
    
main()
