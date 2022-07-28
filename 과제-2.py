#3-1) 다음예의 실행 결과를 보자
str = "hello"
str = str + "python"
str  # -> 'hello python' 새로운 문자열 만드는 과정
# 그러면 += 연산자를 이용 하는 형태로 바꾸어 표현해라 
str = "hello"
str += "python"
print(str)  # 'hellopython'

#4-1) 리스트에 저장되어 있는 모든 값의 합을 계산해 그결과를 반환하는 함수를 만들어라
#예를 들어 함수이름 sum_all, sum_all([1,2,3,4,5]) 리스트저장값-> 15
s_a = [1, 2, 3, 4, 5]
def s_a(s):
    s = 0
    for i in range(1, 6):
        s = s + i
        return s    
        print(s)     # 잘모르겠다.  
                

#4-2) 인자로 전달된 리스트에 저장되어있는 모든 값들을 역순으로 출력하는 함수를 만들어라
#4-2-1) show_reverse([1,2,3,4,5]) -> 5 4 3 2 1
#4-2-2) show_reverse1("abcdefg") -> g f e d c b a
def s_r(x):
    for i in range(len(x) -1, -1, -1):
        print(x[i], end = "")
print(s_r([1,2,3,4,5]))

def s_r(x):
    for i in range(len(x) -1, -1, -1):
        print(x[i], end = "")
print(s_r("abcdefg"))

