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
#   915315a..f11aaf5  master -> master                      <- 마지막 master -> master 확인되면 됨