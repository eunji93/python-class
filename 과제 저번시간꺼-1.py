#문제1

def int_div(n1, n2):
    print("몫:", n1//n2)
    print("나머지:", n1%n2)
int_div(5,2)

#문제2
def bet_sum(n1,n2):
    sum=0
    for i in range(n1+1, n2):
        sum += i
    print(sum)
bet_sum(2,5)