# 8강 for루프 와 while루프 : 자신들에게 속해있는걸 반복하는 루프 / 서로 변환이 가능하다.
# for루프 -> 반복에 대한 횟수가 정해진것 
# while루프 -> ~까지 반복 

# 8-1) for루프에 대한 복습
def main():
    sum = 0
    for i in range(1, 11):              # 범위는 0이 시작이 관례, 0~몇번째까지일땐 0생략 가능 ex) range(10)
        sum = sum + i
    print("sum=", sum, end="")
main()                                  # sum=55

# 8-2) true가 될때까지 반복하는 while루프
## while_basic.py
def main():
    cnt = 0
    while cnt<3:
        print(cnt, end='')
        cnt = cnt + 1                    # cnt = cnt + 1(주석처리하면)라고 하면 cnt는 계속 0 / 무한루프됨
main()                                   # 0, 1, 2 (3미만이니깐 2까지만 나오고 종료~)

# for i(변수) in <반복범위>:         <for에 속하는 문장들>
# while <반복조건>:

## while_sum.py
def main():
    i = 1
    sum = 0
    while i < 11:
        sum = sum + i
        i = i + 1
        print("sum=", sum, end='')
main()                                  # sum = 55

def main():
    sum = 0
    for i in range(1, 11):
        sum = sum + i                   # sum += i
    print("sum=", sum, end='')
main()                                  # while루프를 for루프로 변환 / main()-> sum=55

## while_over100.py
def main():
    i = 1
    sum = 0
    while sum <= 100:
        sum = sum + i
        i = i + 1                               # i = 15까지 만들어서 다시 while 반복후 false라고 알게됨
    print(i-1, "더했을때의 합", sum, end='')     # false값 전의 수 이기에 -> i-1
main()                                          #14 더했을때의 합 105 (i=14)

## while_break.py
def main():
    i = 0 
    while i < 100:                     
        print(i, end='')
        i = i + 1
        if i == 20:                    # 만약 if문이 없었다면 i가 100이 되는 순간 탈출함
            break                      # 반복문에서 제동걸어주는것! / i값이 20이면 탈출해라~-> i가 20프린트 되기전에 이미 탈출
main()                                 # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

# -> break 걸렸을땐 true로 변환 해도 됨
def main():
    i = 0
    while True:
        print(i, end='')
        i = i + 1
        if i == 20:                    
            break
main()                                # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

## while_over100_break.py
def main():
    i = 1
    sum = 0
    while True:
        sum = sum + i
        if sum > 100:
            print(i, "더했을때의 합", sum, end ='')
            break
        i = i + 1
main()                                 #14 더했을때의 합 105 (i=14)

# 8-5) continue : 뒤에 반복되는 횟수는 그대로 하되 true일땐 생략
for i in range(1,11):                # 1~10까지 반복하는 루프
    print(i, end='')                 # 1 2 3 4 5 6 7 8 9 10
    
for i in range(1,11):
    if i % 2 ==0:                    # if i % 2 ==0: continue 
        continue                     # break = 탈출, continue = 생략 (true값) 
    print(i, end='')                 # 1 3 5 7 9 (false값만)

i = 0
while i < 10:
    i = i + 1 
    print              # 8:33분 영상보고 다시 채워넣기

# 8-6) 이중 for루프    
for i in [1, 2]:
    for j in ['a', 'b', 'c']:
        print(j*i, end='')             # a b c aa bb cc, 이런건 구구단 출력할때 많이 씀! 

sr = ['father', 'mother', 'brother']
cnt = 0
for s in sr:
    for c in s:              # c in s : s에 c가 있냐 
        if c == 'r':         # if c == 'r': cnt += 1 로 한줄을 줄일수있다. / 총 if문이 19번 실행됨!
            cnt += 1         # r 이 들어있을때만 cnt 값을 올리니깐 r = 4
cnt                          # 4