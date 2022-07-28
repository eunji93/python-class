#4-1) 리스트에 저장되어 있는 모든 값의 합을 계산해 그결과를 반환하는 함수를 만들어라
#예를 들어 함수이름 sum_all, sum_all([1,2,3,4,5]) 리스트저장값-> 15

def sum_all(st):
    sum = 0
    for i in range(len(st)):
        sum += st[i]
        return sum
sum_all([1, 2, 3, 4, 5])

#4-2) 인자로 전달된 리스트에 저장되어있는 모든 값들을 역순으로 출력하는 함수를 만들어라
#4-2-1) show_reverse([1,2,3,4,5]) -> 5 4 3 2 1
#4-2-2) show_reverse1("abcdefg") -> g f e d c b a

def show_reverse(st):
    for i in range(len(st)):
        print(st[(i+1)*-1], end= "")        #0을 먼저 만들고 이걸 -1로 만드는 법을 생각 하면 된다!
        
show_reverse([1, 2, 3, 4, 5])
show_reverse("abcdefg")