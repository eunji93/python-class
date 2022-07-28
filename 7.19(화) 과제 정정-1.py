# 문제1) 친구의 이름과 전화번호 정보를 담을 수 있는 클래스만들기
# 생성자 __init__ / get_name, get_phone, set_phone, show_info 함수 이용
class friend:
    def __init__(self, name, phone):  # 생성자 초기화
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone 
    def set_phone(self, phone):                  
        self.phone = phone                       # self.phone 원래값, phone 바꿀번호
    def show_info(self):
        print("이름:", self.name)     
        print("전화번호:", self.phone)
                                    
def main():
    f = friend("허지훈","010-1234-1234")
    print(f.show_info())

# 문제2)
class friend:
    def __init__(self, name, phone):  # 생성자 초기화
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone 
    def set_phone(self, phone):                  
        self.phone = phone                       # self.phone 원래값, phone 바꿀번호
    def show_info(self):
        print("이름:", self.name)     
        print("전화번호:", self.phone)
                                    
def main():
    f = friend("허현욱", "010-9876-5432")
    r = friend("이선준", "010-7410-0258")
    i = friend("장지우", "010-9630-0258")
    e = friend("허진욱", "010-4321-1234")
    friend_list = []
    friend_list.append(f, r, i, e)   #리스트 어떻게 만들지...
    print(f.show_info())
    print(r.show_info())
    print(i.show_info())
    print(e.show_info())
    print(friend_list)
   
def main():                                    #2-추가
    f = friend("허현욱","010-9876-5432")
    r = friend("이선준","010-7410-0258")
    i = friend("장지우","010-9630-0258")
    e = friend("허진욱","010-4321-1234")
    friend_list = []
    friend_list.append(f)
    friend_list.append(r)
    friend_list.append(i)
    friend_list.append(e)
    fl = [f, r, i, e]   # 이렇게 작성해도됨
    for i in friend_list:
        i.show_info() 

# 문제2-1)
friend_list = []
friend_list.append(friend("허현욱","010-9876-5432"))
friend_list.append(friend("이선준","010-7410-0258"))
friend_list.append(friend("장지우","010-9630-0258"))
friend_list.append(friend("허진욱","010-4321-1234"))
for i in friend_list:
    i.show_info()

# 문제3)
for i in friend_list:
    if i.get_name().startswith('허'):
        i.show_info()

# 문제4)
for i in friend_list:
    if i.get_name() == '장지우':
        i.set_phone('010-8520-0147')

for i in friend_list:
    if i.get_name() == '장지우':
        i.show_info()