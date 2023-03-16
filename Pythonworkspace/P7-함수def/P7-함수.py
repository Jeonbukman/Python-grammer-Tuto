# #함수 "def 함수이름(전달값):"" 으로 시작
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# # open_account()

# #전달값과 반환값
# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance,money): #출금
#     if balance >= money: #잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 #수수료 100원
#     return commission, balance - money - commission

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance,500)
# print("수수료는 {0}원이며, 잔액은{1}원입니다.".format(commission, balance))


# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호",25,"java")

# 같은 학교, 학년, 반, 수업

# def profile(name, age=17, main_lang="python"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

#키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25,name="김태호")

#가변인자 == "*" / 변수를 원하는 만큼 넣을 수 있음
# def profile(name, age, lang1, lang2, lang3, lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
#(end=" "로 끝내면 열바꿈처리를 안함, 계속 이어서 출력됨)

# def profile(name, age, *language): 
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "java", "C","C++","C#","javaScript")
# profile("김태호",25,"kotlin","Swift")


