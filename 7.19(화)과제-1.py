# 문제1) 친구의 이름과 전화번호 정보를 담을 수 있는 클래스만들기
# 생성자 __init__ / get_name, get_phone, set_phone, show_info 함수 이용
class friend:
    def __init__(self, get_name, get_phone):
        self.get_name = get_name
        self.get_phone = get_phone
    def get_name(self):
        print(self.get_name)
    def get_phone(self):
        print(self.get_phone) 
    def set_phone(self):                  # 전화번호 수정 어떻게?
        self.set_phone = set_phone
        print(self.set_phone)
    def show_info(self):
        print("이름:", self.get_name)     # 수정한 번호로 출력되어야 하는데...
        print("전화번호:", self.get_phone)
                                    
def main():
    f = friend("허지훈","010-1234-1234")
    print(f.show_info())

# 문제2)
class friend:
    def __init__(self, get_name, get_phone):
        self.get_name = get_name
        self.get_phone = get_phone
    def get_name(self):
        print(self.get_name)
    def get_phone(self):
        print(self.get_phone) 
    def set_phone(self):                  
        self.set_phone = set_phone
        print(self.set_phone)
    def show_info(self):
        print("이름:", self.get_name)   
        print("전화번호:", self.get_phone)
                                    
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
    friend_list.append(f, r, i ,e)
    for i in friend_list:
        print(i)   
