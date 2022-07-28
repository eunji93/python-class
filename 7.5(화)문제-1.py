# 문제 1-1)
def t_l(t):
    st = []
    for i in t:
        st.append(i)
    return st
ds = (1, 2, 3)
ds = t_l(ds)
ds   #[1, 2, 3]

ds = 'hello'
ds = t_l(ds)
ds   # ['h', 'e', 'l', 'l', 'o']
        
# 문제 2-1)
for i in range(9, 0, -1):
    print(7*i, end=' ')     # 63 56 49 42 35 28 21 14 7 
    
# 문제 2-2) 튜플 1~100 -> 100->1 만들어보자
tp = tuple(range(1, 100)) + tuple(range(100, 0, -1))  

# 문제 1
for i in range(3):
    print(i+1, i+2, i+3, sep=',')

# 문제 2
def add1(li):
    for i in range(len(li)):
        li[i] += 1                 # 뺄 때는 if문 사용 해주면 됨!
        
st = [1, 2, 3, 4, 5]
add1(st)
st                                 #[2, 3, 4, 5, 6]

