# 내용이 달라지거나 추가할때는 아래 작업 거치면 github에 변경됨
# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git init        <- 변경할래
# Reinitialized existing Git repository in C:/python ej/.git/

# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git add .    <- 추가되거나.새로운거

# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git status      

# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git commit -m "second commit"                 <- 푸쉬할때 내가 어떤거에 저장할껀지

# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git remote add origin https://github.com/eunji93/python-class.git  <- 오류남/ 이미 연결된게 있어서
# error: remote origin already exists.

# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git remote -v                      <- 내가 연결된 주소 확인 하는 법 (origin이 같으면 아래 단계로 감)
# origin  https://github.com/eunji93/python-class.git (fetch)
# origin  https://github.com/eunji93/python-class.git (push)

# User@DESKTOP-M7O6P7G MINGW64 /c/python ej (master)
# $ git push origin master      <- 연결되어 있는걸 확인 했으니 새로운걸 바로 push 하겠다.!
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 16 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 276 bytes | 276.00 KiB/s, done.
# Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
# remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# To https://github.com/eunji93/python-class.git
#   915315a..f11aaf5  master -> master                      <- 마지막 'master -> master' 확인되면 됨

# 깃허브에서 파일 vscode에 옮기는 방법 -> 새로운 파일에 git bash에서 코드 입력
# User@DESKTOP-M7O6P7G MINGW64 /c/python
# $ git clone https://github.com/eunji93/python-class.git  <- git clone에 열고자하는 코드 복사(깃허브 사이트에서 내코드 따는것)
# Cloning into 'python-class'...
# remote: Enumerating objects: 47, done.
# remote: Counting objects: 100% (47/47), done.
# remote: Compressing objects: 100% (42/42), done.
# remote: Total 47 (delta 5), reused 46 (delta 4), pack-reused 0Receiving objects:  57% (27/47)
# Receiving objects: 100% (47/47), 31.39 KiB | 3.92 MiB/s, done.
# Resolving deltas: 100% (5/5), done.

# 7.28(목) 강의2 
# v1 == v2 : 변수 v1과 변수 v2가 참조하는 객체의 내용이 같냐?  (내용물만 같으면 됨)
# v1 is v2 : 변수 v1과 변수 v2가 참조하는 객체는 동일한 객체냐? (동일한 대상이냐?)
r1 = [1, 2, 3]
r2 = [1, 2, 3]
r1 == r2       # true
r1 is r2       # false -> 참조값이 다름 id(r1) / id(r2) 주소값이 다름
id(r1) / id(r2)

# 복사하는 코드
t1 = [1, 2, 3]
t2 = t1
t1 is t2     # true 